import re

from src.common import utils

# "mul(123, 456)" -> ("123", "456")
MUL_OP = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def task1() -> int:
    instructions = utils.read_text()
    res = 0
    for m in MUL_OP.finditer(instructions):
        a, b = int(m.group(1)), int(m.group(2))
        res += a * b
    return res


# "do()|don't()|mul(123, 456)"  # noqa: ERA001
# the pattern is a literal for syntax highlight
COND_OP = re.compile(r"do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)")


def task2() -> int:
    instructions = utils.read_text()
    res = 0
    do_flag = True
    for m in COND_OP.finditer(instructions):
        if m.group(0) == "do()":
            do_flag = True
        elif m.group(0) == "don't()":
            do_flag = False
        else:
            a, b = int(m.group(1)), int(m.group(2))
            if do_flag:
                res += a * b
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
