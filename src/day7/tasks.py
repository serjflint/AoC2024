import itertools as it

from src.common import utils


def read_test(line: str) -> tuple[int, list[int]]:
    left, right = line.split(":")
    test = int(left)
    args = [int(arg) for arg in right.split()]
    return test, args


def task1() -> int:
    lines = utils.read_lines()
    res = 0
    for line in lines:
        test, args = read_test(line)
        for pr in it.product((0, 1), repeat=len(args) - 1):
            val = args[0]
            for idx, op in enumerate(pr):
                if op == 0:
                    val += args[idx + 1]
                else:
                    val *= args[idx + 1]
            if val == test:
                res += val
                break
    return res


def task2() -> int:
    lines = utils.read_lines()
    res = 0
    for line in lines:
        test, args = read_test(line)
        for pr in it.product((0, 1, 2), repeat=len(args) - 1):
            val = args[0]
            for idx, op in enumerate(pr):
                if op == 0:
                    val += args[idx + 1]
                elif op == 1:
                    val *= args[idx + 1]
                else:
                    val = int(str(val) + str(args[idx + 1]))
            if val == test:
                res += val
                break
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
