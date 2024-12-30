import collections
import typing as tp

from tqdm import tqdm

from src.common import utils

FILENAME = utils.with_suffix(__file__)

MASKS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def gen_steps(arr: list[list[str]], pos: tuple[int, int]) -> tp.Iterator[tuple[int, int]]:
    x, y = pos
    max_x, max_y = len(arr[0]), len(arr)
    d = 0
    while True:
        dir_x, dir_y = MASKS[d]
        new_x, new_y = x + dir_x, y + dir_y
        if not (0 <= new_x < max_x and 0 <= new_y < max_y):
            break
        if arr[new_y][new_x] == "#":
            d = (d + 1) % 4
            continue
        yield new_x, new_y
        x, y = new_x, new_y


def task1(filename: str = FILENAME) -> int:
    arr = [list(line.strip()) for line in utils.read_lines(filename)]
    pos_x, pos_y = next(utils.where(arr, "^"))

    arr[pos_y][pos_x] = "X"
    for x, y in gen_steps(arr, (pos_x, pos_y)):
        arr[y][x] = "X"
    return len(list(utils.where(arr, "X")))


CYCLE_COUNTER = 4


def task2(filename: str = FILENAME) -> int:
    arr = [list(line.strip()) for line in utils.read_lines(filename)]
    pos_x, pos_y = next(utils.where(arr, "^"))

    max_x, max_y = len(arr[0]), len(arr)
    choices = set(gen_steps(arr, (pos_x, pos_y)))
    choices.discard((pos_x, pos_y))
    blocks = set(utils.where(arr, "#"))

    res = 0
    for obstacle in tqdm(choices):
        d = 0
        x, y = pos_x, pos_y
        counter = collections.defaultdict(int)
        blocks.add(obstacle)
        while True:
            new_x, new_y = x + MASKS[d][0], y + MASKS[d][1]
            if not (0 <= new_x < max_x and 0 <= new_y < max_y):
                break
            if (new_x, new_y) in blocks:
                d = (d + 1) % 4
                continue
            x, y = new_x, new_y
            if (x, y, d) in counter:
                res += 1
                break
            counter[x, y, d] = 1
        blocks.discard(obstacle)

    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
