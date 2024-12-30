import collections
import functools
import math
import typing as tp

from src.common import utils


def stone_blink(val: int) -> tp.Collection[int]:
    if val == 0:
        return (1,)
    if len(str(val)) % 2 == 0:
        str_val = str(val)
        mid = len(str_val) // 2
        left, right = str_val[:mid], str_val[mid:]
        return int(left), int(right)
    return (int(val) * 2024,)


@functools.cache
def fast_blink(val: int) -> tp.Collection[int]:
    if val == 0:
        return (1,)
    digits_1 = int(math.log10(val))
    if digits_1 % 2 == 1:
        mid = (digits_1 + 1) // 2
        divisor = 10**mid
        return val // divisor, val % divisor
    return (val * 2024,)


def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for val in stones:
        new_stones.extend(fast_blink(val))
    return new_stones


def counter_blink(counter: collections.Counter) -> collections.Counter:
    new_counter = collections.defaultdict(int)
    for val, c in counter.items():
        for new_val in stone_blink(val):
            new_counter[new_val] += c
    return collections.Counter(new_counter)


def task1(filename: str = "input.txt") -> int:
    data = utils.read_text(filename)
    stones = utils.to_ints(data)
    for _ in range(25):
        stones = blink(stones)
    return len(stones)


def task2(filename: str = "input.txt") -> int:
    data = utils.read_text(filename)
    counter = collections.Counter(utils.to_ints(data))
    for _ in range(75):
        counter = counter_blink(counter)
    return sum(counter.values())


if __name__ == "__main__":
    print(task1())
    print(task2())
