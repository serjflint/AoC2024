import collections
import typing as tp

import numpy as np
from tqdm import tqdm

from src.common import utils

MASKS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def gen_steps(arr: np.ndarray, pos: tuple[int, int]) -> tp.Iterator[tuple[int, int]]:
    x, y = pos
    max_x, max_y = len(arr[0]), len(arr)
    d = 0
    while True:
        dir_x, dir_y = MASKS[d]
        new_x, new_y = x + dir_x, y + dir_y
        if not (0 <= new_x < max_x and 0 <= new_y < max_y):
            break
        if arr[new_x, new_y] == "#":
            d = (d + 1) % 4
            continue
        yield new_x, new_y
        x, y = new_x, new_y


def print_arr(arr: np.ndarray) -> None:
    print("\n".join(["".join(row) for row in arr]))
    print()


def task1() -> int:
    arr = np.array([list(line.strip()) for line in utils.read_lines()])
    pos_x, pos_y = np.argwhere(arr == "^")[0]
    arr[pos_x, pos_y] = "X"
    for x, y in gen_steps(arr, (pos_x, pos_y)):
        arr[x, y] = "X"
    return len(np.argwhere(arr == "X"))


CYCLE_COUNTER = 4


def task2(filename: str = 'input.txt') -> int:
    arr = np.array([list(line.strip()) for line in utils.read_lines(filename)])
    pos_x, pos_y = np.argwhere(arr == "^")[0]
    max_x, max_y = len(arr[0]), len(arr)

    choices = {(x, y) for x, y in gen_steps(arr, (pos_x, pos_y))}
    choices.discard((pos_x, pos_y))
    blocks = {(x, y) for x, y in np.argwhere(arr == "#")}

    res = 0
    for obstacle in tqdm(choices):
        d = 0
        x, y = pos_x, pos_y
        counter = collections.defaultdict(int)
        blocks.add(obstacle)
        while True:
            dir_x, dir_y = MASKS[d]
            new_x, new_y = x + dir_x, y + dir_y
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
