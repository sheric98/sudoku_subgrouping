DEFAULT_CODE = (2 ** 9) - 1
MASKS = [DEFAULT_CODE - (2 ** i) for i in range(9)]

SINGLE_NUM_CODE = [2 ** i for i in range(9)]

MASK_TO_COUNT = dict([(i, bin(i).count("1")) for i in range(512)])
