import typing as tp

from src.common import utils

FILENAME = utils.with_suffix(__file__)

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def bfs(
    field: list[list[int]], pos: tuple[int, int], cond: tp.Callable, *, check_seen: bool = False
) -> tp.Iterator[tuple[int, int]]:
    max_x, max_y = len(field[0]), len(field)
    buffer = [pos]
    seen = set()
    while buffer:
        prev = x, y = buffer.pop()
        for dir_x, dir_y in DIRS:
            curr = new_x, new_y = x + dir_x, y + dir_y
            if check_seen and curr in seen:
                continue
            if 0 <= new_x < max_x and 0 <= new_y < max_y and cond(field, prev, curr):
                buffer.append(curr)
                seen.add(curr)
                yield curr


TRAILHEAD = 0
PEAK = 9


def uphill_slope(field: list[list[int]], prev: tuple[int, int], curr: tuple[int, int]) -> bool:
    (prev_x, prev_y), (curr_x, curr_y) = prev, curr
    prev_val, curr_val = field[prev_y][prev_x], field[curr_y][curr_x]
    if prev_val is None or curr_val is None:
        return False
    return prev_val + 1 == curr_val


def task1(filename: str = FILENAME) -> int:
    field = utils.read_lists_opt(filename)

    res = 0
    for x in range(len(field[0])):
        for y in range(len(field)):
            if field[y][x] == TRAILHEAD:
                for pos_x, pos_y in bfs(field, (x, y), cond=uphill_slope, check_seen=True):
                    if field[pos_y][pos_x] == PEAK:
                        res += 1
    return res


def task2(filename: str = FILENAME) -> int:
    field = utils.read_lists_opt(filename)

    res = 0
    for x in range(len(field[0])):
        for y in range(len(field)):
            if field[y][x] == TRAILHEAD:
                for pos_x, pos_y in bfs(field, (x, y), cond=uphill_slope, check_seen=False):
                    if field[pos_y][pos_x] == PEAK:
                        res += 1
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
