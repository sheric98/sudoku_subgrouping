from .Subgroup import Subgroup

class Group:
    def __init__(self, squares):
        self.squares = squares

    def __eq__(self, __o: object) -> bool:
        return id(self) == id(__o)

    def __hash__(self) -> int:
        return hash(id(self))

    def __repr__(self) -> str:
        return f'Group(squares={self.squares})'

    def _add_init_group_to_square(self, init_subgroup, square):
        square.add_initial_group(self, init_subgroup)

    def add_init_group_to_squares(self):
        init_subgroup = Subgroup(self.squares, {self})
        for square in self.squares:
            self._add_init_group_to_square(init_subgroup, square)
        return init_subgroup
