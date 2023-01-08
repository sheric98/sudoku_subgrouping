from .Square import Square
from .Group import Group
from .SubgroupManager import SubgroupManager

class Board:
    def __init__(self):
        self.squares = [[Square(x, y) for x in range(9)] for y in range(9)]
        self.groups = self._add_groups()
        init_subgroups = []
        for group in self.groups:
            init_subgroups.append(group.add_init_group_to_squares())
        self.subgroup_manager = SubgroupManager(init_subgroups)

    def _add_groups(self):
        ret = []
        ret.extend(self._add_rows())
        ret.extend(self._add_cols())
        ret.extend(self._add_square_groups())
        return ret

    def _add_rows(self):
        ret = []
        for row in self.squares:
            ret.append(Group(row))
        return ret
    
    def _add_cols(self):
        ret = []
        for i in range(9):
            col = [row[i] for row in self.squares]
            ret.append(Group(col))
        return ret
    
    def _add_square_groups(self):
        ret = []
        for i in range(0, 9, 3):
            rows = [row[i:i+3] for row in self.squares]
            for j in range(0, 9, 3):
                cols = rows[j:j+3]
                squares = [square for row in cols for square in row]
                ret.append(Group(squares))
        return ret

    def _solve_aux(self, squares):
        while len(squares) > 0:
            print('itr')
            subgroups_updated = set([subgroup for square in squares for subgroup in square.subgroups])

            squares = self.subgroup_manager.get_updates_on_subgroups(subgroups_updated, squares)
            # new_squares = set()
            # for subgroup in subgroups_updated:
            #     subgroup_ret = subgroup.find_subgroups(squares)

            #     if subgroup_ret is not None:
            #         new_subgroups, new_updates = subgroup_ret
            #         subgroup.update_squares(new_subgroups)

            #         new_squares.update(new_updates)
                
            # squares = new_squares
            

    def solve(self, startingCoords):
        squares = []
        for startingCoord in startingCoords:
            square = self.squares[startingCoord.y][startingCoord.x]
            square.set_init_num(startingCoord.num)
            squares.append(square)

        print(f'{len(squares)} starting squares')
        for square in squares:
            print(f'Starting square: {square}')
        self._solve_aux(squares)

    def print_all_subgroups(self):
        subgroups = set()
        for row in self.squares:
            for square in row:
                subgroups.update(square.subgroups)

        solved = []
        unsolved = []
        for subgroup in subgroups:
            if len(subgroup.squares) == 1:
                solved.append(subgroup)
            else:
                unsolved.append(subgroup)
        
        print(f'solved subgroups: {solved}')
        print(f'unsolved subgroups: {unsolved}')
        print(f'solved subgroups length: {len(solved)}')
        print(f'unsolved subgroups length: {len(unsolved)}')
