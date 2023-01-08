from .SubgroupDecider import SubgroupDecider
from .Subgroup import Subgroup

class SubgroupManager:
    def __init__(self, subgroups):
        self.subgroups = dict([(subgroup, subgroup) for subgroup in subgroups])

    def _add_subgroup(self, new_subgroup):
        updated_squares = set()
        
        subgroup_to_use = new_subgroup
        if new_subgroup in self.subgroups:
            subgroup_to_use = self.subgroups[new_subgroup]
            subgroup_to_use.groups.update(new_subgroup.groups)
        else:
            self.subgroups[new_subgroup] = new_subgroup
            for square in new_subgroup.squares:
                square.add_subgroup(new_subgroup)
        print(f'Removing {subgroup_to_use} from {subgroup_to_use.groups}')
        squares_to_use = [square for group in subgroup_to_use.groups for square in group.squares if square not in subgroup_to_use.squares]
        
        for square in squares_to_use:
            if square.remove_nums(subgroup_to_use.get_code()):
                updated_squares.add(square)

        return updated_squares

    def _remove_subgroup(self, old_subgroup):
        del self.subgroups[old_subgroup]
        for square in old_subgroup.squares:
            square.remove_subgroup(old_subgroup)

    def update_subgroups(self, new_subgroups, old_subgroup):
        updated_squares = set()
        self._remove_subgroup(old_subgroup)
        for new_subgroup in new_subgroups:
            updated_squares.update(self._add_subgroup(new_subgroup))
        return updated_squares

    def _get_subgroups_r(self, original_subgroup, squares, updated_squares, starting_squares=None):
        decider = SubgroupDecider(squares, starting_squares)
        decider_ret = decider.find_a_subgroup()
        if decider_ret is None:
            # return [original_subgroup]
            return
        
        initial_subgroup_squares, split_subgroup_squares = decider_ret
        initial_subgroup = Subgroup(initial_subgroup_squares, original_subgroup.groups)
        split_subgroup = Subgroup(split_subgroup_squares, original_subgroup.groups)

        updates = self.update_subgroups([initial_subgroup, split_subgroup], original_subgroup)
        updated_squares.update(updates)

        left_ret = self._get_subgroups_r(initial_subgroup, initial_subgroup_squares, updated_squares)
        right_ret = self._get_subgroups_r(split_subgroup, split_subgroup_squares, updated_squares)

        # return left_ret + right_ret

    def _get_subgroups(self, subgroup, starting_squares=None):
        updated_squares = set()
        if starting_squares is not None:
            starting_squares = self._get_starting_intersect(subgroup.squares, starting_squares)

        new_subgroups = self._get_subgroups_r(subgroup, subgroup.squares, updated_squares, starting_squares)
        return updated_squares

    def get_updates_on_subgroups(self, subgroups, starting_squares):
        return {square for subgroup in subgroups for square in self._get_subgroups(subgroup, starting_squares)}

    def _get_starting_intersect(self, squares, starting_squares):
        square_set = set(squares)
        return [square for square in starting_squares if square in square_set]
    