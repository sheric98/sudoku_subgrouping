from board.Board import Board
from board.StartingCoord import StartingCoord
import argparse


def convert_input_to_starting_coord(input):
    split = input.split(',')
    nums = [int(num.strip()) for num in split]
    assert len(nums) == 3

    return StartingCoord(nums[0], nums[1], nums[2])


parser = argparse.ArgumentParser()
parser.add_argument('--initial_vals', required=True, nargs='+', type=convert_input_to_starting_coord)


if __name__ == '__main__':
    args = parser.parse_args()
    board = Board()

    board.solve(args.initial_vals)

    board.print_all_subgroups()
