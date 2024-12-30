import collections

from src.common import utils

FILENAME = utils.with_suffix(__file__)


def task1(filename: str = FILENAME) -> int:
    a_arr, b_arr = utils.read_pairs(filename)
    return sum(abs(a - b) for a, b in zip(a_arr, b_arr, strict=False))


def task2(filename: str = FILENAME) -> int:
    a_arr, b_arr = utils.read_pairs(filename)
    counts = collections.Counter(b_arr)
    return sum(a * counts.get(a, 0) for a in a_arr)


if __name__ == "__main__":
    print(task1())
    print(task2())
