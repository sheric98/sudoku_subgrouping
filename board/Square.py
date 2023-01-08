from .Codes import DEFAULT_CODE, SINGLE_NUM_CODE, MASK_TO_COUNT

class Square:
    def __init__(self, x, y):
        self.code = DEFAULT_CODE
        self.groups = []
        self.subgroups = set()
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash(id(self))

    def __eq__(self, __o: object) -> bool:
        return id(self) == id(__o)

    def _code_str(self):
        return '{:b}'.format(self.code)

    def __repr__(self):
        return f'Square(x={self.x}, y={self.y}, code={self._code_str()})'

    def add_initial_group(self, group, subgroup):
        self.groups.append(group)
        self.subgroups.add(subgroup)

    def remove_nums(self, code):
        mask = DEFAULT_CODE ^ code
        new_code = self.code & mask
        updated = new_code != self.code
        self.code = new_code
        return updated

    def add_subgroup(self, new_subgroup):
        self.subgroups.add(new_subgroup)

    def remove_subgroup(self, old_subgroup):
        self.subgroups.remove(old_subgroup)

    def update_subgroup(self, old_subgroup, new_subgroups):
        self.subgroups.remove(old_subgroup)
        self.subgroups.update(new_subgroups)

    def set_init_num(self, num):
        self.code = SINGLE_NUM_CODE[num - 1]

    def count(self):
        return MASK_TO_COUNT[self.code]
