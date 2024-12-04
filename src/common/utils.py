import pathlib


def read_pairs(filename: str = "input.txt", *, length: int = 1000, sort: bool = True) -> tuple[list[int], list[int]]:
    a_arr, b_arr = [0] * length, [0] * length
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        for idx, line in enumerate(stream):
            if not line:
                continue
            a, b = line.strip().split()
            a_arr[idx], b_arr[idx] = int(a), int(b)
    if sort:
        a_arr.sort()
        b_arr.sort()
    return a_arr, b_arr


def read_lists(filename: str = "input.txt") -> list[list[int]]:
    res = []
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        for line in stream:
            if not line:
                continue
            row = [int(val) for val in line.strip().split()]
            res.append(row)
    return res


def read_text(filename: str = "input.txt") -> str:
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        return stream.read()


def read_lines(filename: str = "input.txt") -> list[str]:
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        return stream.readlines()
