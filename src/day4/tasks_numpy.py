"""Taken from Pavel Polyakov's solution."""

import typing as tp

import numpy as np

from src.common import utils


def count(line: tp.Iterable[str]) -> int:
    line = "".join(line)
    return line.count("XMAS") + line.count("SAMX")


def task1() -> int:
    arr = np.array([list(line.strip()) for line in utils.read_lines()])
    res = 0

    # rows and columns
    for line in arr:
        res += count(line)
    for line in arr.T:
        res += count(line)

    # diags
    d = max(len(arr), len(arr[0]))
    for i in range(-d, d):
        res += count(np.diag(arr, i))
    arr90 = np.rot90(arr)
    for i in range(-d, d):
        res += count(np.diag(arr90, i))

    return res


X_MAS = ["MAS", "SAM"]


def task2() -> int:
    arr = np.array([list(line.strip()) for line in utils.read_lines()])
    res = 0

    max_x, max_y = len(arr[0]), len(arr)
    for pos_x in range(max_x - 2):
        for pos_y in range(max_y - 2):
            if arr[pos_x + 1, pos_y + 1] != "A":
                continue
            square = arr[pos_x : pos_x + 3, pos_y : pos_y + 3]
            diag1 = "".join(np.diag(square))
            diag2 = "".join(np.diag(np.rot90(square)))
            if diag1 in X_MAS and diag2 in X_MAS:
                res += 1
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
