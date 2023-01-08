from .Codes import MASK_TO_COUNT
from .Partition import Partition
from .Subgroup import Subgroup




class SubgroupDecider:
    def __init__(self, squares, starting_squares=None):
        self.n = len(squares)
        self.remaining_squares = self.n
        self.squares = sorted(squares, key=lambda x: -MASK_TO_COUNT[x.code])
        if starting_squares is None:
            self.starting_squares = self.squares
        else:
            self.starting_squares = starting_squares
        self.starting_squares = set([square.code for square in self.starting_squares])
        self.code_to_squares = self._get_code_to_squares()
        self.code_to_idx = dict([(code, idx) for idx, code in enumerate(self.code_to_squares.keys())])
        self.tested_partitions = set()

    def _is_square_init_viable(self, square, idx):
        cnt = square.count()
        return cnt < self.n and self.n - idx >= cnt

    def _remove_code(self, code):
        self.remaining_squares -= len(self.code_to_squares[code])
        del self.code_to_squares[code]

    def _init_viable_squares(self):
        for idx, square in enumerate(self.squares):
            code = square.code
            if code in self.code_to_squares and not self._is_square_init_viable(square, idx):
                # print('removing unviable square')
                self._remove_code(code)
                if code in self.starting_squares:
                    self.starting_squares.remove(code)
                
    def _get_code_to_squares(self):
        ret = {}
        for square in self.squares:
            code = square.code
            if code not in ret:
                ret[code] = []
            ret[code].append(square)
        
        return ret

    def _add_partition(self, partition, code, partition_id=None):
        for square in self.code_to_squares[code]:
            partition.add_square(square, partition_id)
        
        if partition.is_dead(self._get_reamining_viable_squares()):
            return -1
        elif partition.is_group():
            return 1
        else:
            return 0

    def _test_branch(self, partition, seen):
        for code, squares in self.code_to_squares.items():
            if code in seen:
                continue

            child_partition_id = partition.try_partition_id(code, len(squares))
            if child_partition_id in self.tested_partitions:
                continue
            self.tested_partitions.add(child_partition_id)

            child_partition = partition.copy()
            ret = self._add_partition(child_partition, code, child_partition_id)

            if ret == 1:
                return child_partition
            elif ret == 0:
                copied_seen = seen.copy()
                copied_seen.add(code)
                child_ret = self._test_branch(child_partition, copied_seen)
                if child_ret is not None:
                    return child_ret
        
        return None
            
    def _test_starting_code(self, code):
        partition = Partition(self.code_to_idx, self.n)
        ret = self._add_partition(partition, code)

        self.tested_partitions.add(partition.partition_id)
        if ret == 1:
            return partition
        elif ret == -1:
            return None
        else:
            seen = set()
            seen.add(code)
            return self._test_branch(partition, seen)

    def _split_subgroups(self, partition):
        first_subgroup = set(partition.squares)

        split = [square for square in self.squares if square not in first_subgroup]


        return partition.squares, split

    def _get_reamining_viable_squares(self):
        return self.remaining_squares

    def find_a_subgroup(self):
        self._init_viable_squares()
        for code in self.starting_squares:
            ret = self._test_starting_code(code)

            if ret is not None:
                return self._split_subgroups(ret)
            else:
                self._remove_code(code)
        
        return None
