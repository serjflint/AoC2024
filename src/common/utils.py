import pathlib


def read(
    filename: str = "input.txt", *, length: int = 1000, sort: bool = True
) -> tuple[list, list]:
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
