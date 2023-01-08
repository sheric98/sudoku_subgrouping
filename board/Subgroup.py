class Subgroup:
    def __init__(self, squares, group):
        self.squares = set(squares)
        self.groups = set(group)

    def __hash__(self):
        return hash(tuple(self.squares))
    
    def __eq__(self, __o: object) -> bool:
        return set(self.squares) == set(__o.squares)

    def get_code(self):
        code = 0
        for square in self.squares:
            code |= square.code
        return code

    def _get_possible(self):
        code = 0
        for square in self.squares:
            code |= square.code
        return '{:b}'.format(code)

    def __repr__(self):
        return f"Subgroup(squares={self.squares}, code={self._get_possible()}, #groups={len(self.groups)})"

    # def find_subgroups(self, updated_squares):
        
    #     squares_list, updates = get_subgroups(self.squares, updated_squares)
    #     single_squares = set()
    #     for square in self.squares:
    #         if square.count() == 1:
    #             single_squares.add(square)
    #     if len(self.squares) > 1 and len(single_squares) > 0:
    #         print(f'deciding on group with single squares: {self.squares}')

    #     if len(squares_list) == 1:
    #         return None
    #     else:
    #         for squares in squares_list:
    #             for square in squares:
    #                 if square in single_squares and len(squares) > 1:
    #                     print(f'Started with squares: {self.squares}. Single square not isolated: {squares}')
    #         return [Subgroup(squares) for squares in squares_list], updates

    def update_squares(self, updated_subgroups):
        for square in self.squares:
            square.update_subgroup(self, updated_subgroups)
