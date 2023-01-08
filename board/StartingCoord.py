# x is left to right, y is top to bot
class StartingCoord:
    def __init__(self, x, y, num):
        assert x >= 0 and x < 9
        assert y >= 0 and y < 9
        assert num > 0 and num <= 9
        self.x = x
        self.y = y
        self.num = num
