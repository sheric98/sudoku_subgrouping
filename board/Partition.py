from .Codes import MASK_TO_COUNT

class Partition:
    def __init__(self, code_to_idx, all_squares_num):
        self.code_to_idx = code_to_idx
        self.all_squares_num = all_squares_num
        self.squares = []
        self.code = 0
        self.partition_id = 0

    def _get_id_additive(self, code):
        return 9 ** (self.code_to_idx[code])

    def try_partition_id(self, code, num):
        return self.partition_id + (num * self._get_id_additive(code))

    def add_square(self, square, partition_id=None):
        self.squares.append(square)
        self.code |= square.code

        if partition_id is None:
            self.partition_id += self._get_id_additive(square.code)
        else:
            self.partition_id = partition_id

    def is_group(self):
        return len(self.squares) == MASK_TO_COUNT[self.code]

    def _count(self):
        return MASK_TO_COUNT[self.code]

    def is_dead(self, remaining_viable):
        return self._count() > remaining_viable or len(self.squares) == self.all_squares_num

    def copy(self):
        part = Partition(self.code_to_idx, self.all_squares_num)
        part.squares = self.squares.copy()
        part.code = self.code
        part.partition_id = self.partition_id

        return part
