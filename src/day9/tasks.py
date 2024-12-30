import msgspec

from src.common import utils


def index(lst: list[int], value: int | None, start: int = 0) -> int:
    for idx in range(start, len(lst)):
        if lst[idx] == value:
            return idx
    return -1


def rindex(lst: list[int], value: int | None, start: int | None = None) -> int:
    if start is None:
        start = len(lst) - 1
    for idx in range(start, -1, -1):
        if lst[idx] != value:
            return idx
    return -1


def task1() -> int:
    cd = utils.read_text().strip()
    disk = []
    for idx, size in enumerate(cd):
        if idx % 2 == 0:
            disk.extend([idx // 2] * int(size))
        else:
            disk.extend([None] * int(size))

    left, right = index(disk, None), rindex(disk, None)
    while left < right:
        disk[left], disk[right] = disk[right], disk[left]
        left, right = index(disk, None, start=left), rindex(disk, None, start=right)

    res = 0
    for idx, id_ in enumerate(disk):
        if id_ is not None:
            res += idx * id_
    return res


class File(msgspec.Struct):
    size: int
    pos: int


def task2() -> int:
    cd = utils.read_text().strip()
    disk, free = [], []
    pos = 0
    for idx, size in enumerate(cd):
        store = disk if idx % 2 == 0 else free
        store.append(File(size=int(size), pos=pos))
        pos += int(size)
    for file in reversed(disk):
        for space in free:
            if space.pos > file.pos:
                break
            if file.size <= space.size:
                file.pos = space.pos
                space.pos += file.size
                space.size -= file.size
                break
    res = 0
    for idx, file in enumerate(disk):
        for x in range(file.size):
            res += idx * (file.pos + x)
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
