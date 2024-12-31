import pathlib
import typing as tp

_T = tp.TypeVar("_T")


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


def to_ints(line: str) -> list[int]:
    return [int(val) for val in line.split()]


def read_lists(filename: str = "input.txt") -> list[list[int]]:
    res = []
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        for line in stream:
            line = line.strip()  # noqa: PLW2901
            if not line:
                continue
            res.append(to_ints(line))
    return res


def read_lists_opt(filename: str = "input.txt", *, fill: str = ".") -> list[list[int | None]]:
    res = []
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        for line in stream:
            line = line.strip()  # noqa: PLW2901
            if not line:
                continue
            row = [(int(val) if val != fill else None) for val in list(line)]
            res.append(row)
    return res


def read_text(filename: str = "input.txt") -> str:
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        return stream.read()


def read_lines(filename: str = "input.txt") -> list[str]:
    with pathlib.Path(filename).open(encoding="utf-8") as stream:
        return stream.readlines()


def print_arr(arr: list[list[str]]) -> None:
    print("\n".join(["".join(row) for row in arr]))
    print()


def where(arr: list[list[_T]], val: _T) -> tp.Iterator[tuple[int, int]]:
    max_x, max_y = len(arr[0]), len(arr)
    for x in range(max_x):
        for y in range(max_y):
            if arr[y][x] == val:
                yield x, y


def with_suffix(file: str, suffix: str = ".txt") -> str:
    path = pathlib.Path(file).with_suffix(suffix)
    return str(path)


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
TPoint = tuple[int, int]


def bfs(
    field: tp.Sequence[tp.Sequence[tp.Any]], pos: TPoint, cond: tp.Callable, *, check_seen: bool = False
) -> tp.Iterator[TPoint]:
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
