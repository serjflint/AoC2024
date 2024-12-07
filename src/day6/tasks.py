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
        if new_x not in range(max_x) or new_y not in range(max_y):
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


def task2() -> int:
    arr = np.array([list(line.strip()) for line in utils.read_lines()])
    pos_x, pos_y = np.argwhere(arr == "^")[0]
    backup = np.copy(arr)

    for x, y in gen_steps(arr, (pos_x, pos_y)):
        arr[x, y] = "X"
    choices = np.argwhere(arr == "X")

    res = 0
    for obstacle in tqdm(choices):
        if obstacle[0] == pos_x and obstacle[1] == pos_y:
            continue

        arr = np.copy(backup)
        arr[obstacle[0], obstacle[1]] = "#"

        counter = collections.defaultdict(int)
        for x, y in gen_steps(arr, (pos_x, pos_y)):
            arr[x, y] = "X"
            counter[x, y] += 1
            if counter[x, y] > CYCLE_COUNTER:
                res += 1
                break
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
