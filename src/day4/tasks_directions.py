import itertools as it

from src.common import utils

DIRECTIONS = [d for d in it.product((-1, 0, 1), repeat=2) if d != (0, 0)]
XMAS = "XMAS"


def task1() -> int:
    field = utils.read_lines()
    res = 0
    max_x, max_y = len(field[0]), len(field)
    for pos_x, pos_y in it.product(range(max_x), range(max_y)):
        for dir_x, dir_y in DIRECTIONS:
            for idx, char in enumerate(XMAS):
                new_x, new_y = pos_x + dir_x * idx, pos_y + dir_y * idx
                if new_x not in range(max_x) or new_y not in range(max_y):
                    break
                if field[new_y][new_x] != char:
                    break
            else:
                res += 1
    return res

SLASHES = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]

def task2() -> int:
    field = utils.read_lines()
    res = 0
    max_x, max_y = len(field[0]), len(field)
    for pos_x, pos_y in it.product(range(1, max_x-1), range(1, max_y-1)):
        if field[pos_y][pos_x] != "A":
            continue
        chars = [{field[pos_y + dir_y][pos_x + dir_x] for dir_x, dir_y in slash} for slash in SLASHES]
        if chars[0] == chars[1] == {'M', 'S'}:
            res += 1
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
