import collections
import itertools
import typing as tp

from src.common import utils

FILENAME = utils.with_suffix(__file__)

TFence = tuple[utils.TPoint, utils.TPoint]
TSide = set[TFence]
TField = list[list[str]]


def task1(filename: str = FILENAME) -> int:
    data = utils.read_lines(filename)
    field = [list(line.strip()) for line in data]
    regions = get_regions(field)

    areas: dict[int, int] = collections.defaultdict(int)
    perimeters: dict[int, int] = collections.defaultdict(int)
    for y, row in enumerate(field):
        for x, ch in enumerate(row):
            p = x, y
            idx = regions[p]

            areas[idx] += 1
            for _ in get_fences(field, p, ch):
                perimeters[idx] += 1

    return sum(areas[idx] * perimeters[idx] for idx in areas)


def task2(filename: str = FILENAME) -> int:
    data = utils.read_lines(filename)
    field = [list(line.strip()) for line in data]
    regions = get_regions(field)

    areas: dict[int, int] = collections.defaultdict(int)
    perimeters: dict[int, list[TFence]] = collections.defaultdict(list)
    for y, row in enumerate(field):
        for x, ch in enumerate(row):
            p = x, y
            idx = regions[p]

            areas[idx] += 1
            for fence in get_fences(field, p, ch):
                perimeters[idx].append(fence)

    sides: dict[int, int] = collections.defaultdict(int)
    for idx, perimeter in perimeters.items():
        distinct_sides = get_distinct_sides(grow_sides(perimeter))
        sides[idx] = len(distinct_sides)

    return sum(areas[idx] * sides[idx] for idx in areas)


def same_plant(field: TField, prev: utils.TPoint, curr: utils.TPoint) -> bool:
    (prev_x, prev_y), (curr_x, curr_y) = prev, curr
    prev_val, curr_val = field[prev_y][prev_x], field[curr_y][curr_x]
    return prev_val == curr_val


def get_regions(field: TField) -> dict[utils.TPoint, int]:
    counter = itertools.count()
    regions = {}
    for y, row in enumerate(field):
        for x in range(len(row)):
            p = x, y
            if p in regions:
                continue
            idx = next(counter)
            regions[p] = idx
            for pos_x, pos_y in utils.bfs(field, p, cond=same_plant, check_seen=True):
                new_p = pos_x, pos_y
                regions[new_p] = idx
    return regions


def get_fences(field: TField, p: utils.TPoint, ch: str) -> tp.Iterator[TFence]:
    x, y = p
    max_x, max_y = len(field[0]), len(field)
    for dx, dy in utils.DIRS:
        new_p = new_x, new_y = x + dx, y + dy
        if 0 <= new_x < max_x and 0 <= new_y < max_y:
            if field[new_y][new_x] != ch:
                yield p, new_p
        else:
            yield p, new_p


def grow_sides(perimeter: list[TFence]) -> list[TSide]:
    sides: list[TSide] = []
    for fence in perimeter:
        found = False
        for side in sides:
            for neighbor in get_neighbors(fence):
                if neighbor in side:
                    found = True
                    side.add(fence)
        if not found:
            sides.append({fence})
    return sides


def get_neighbors(fence: TFence) -> tp.Iterator[TFence]:
    (x, y), (new_x, new_y) = fence
    if x == new_x:
        yield (x - 1, y), (new_x - 1, new_y)
        yield (x + 1, y), (new_x + 1, new_y)
    elif y == new_y:
        yield (x, y - 1), (new_x, new_y - 1)
        yield (x, y + 1), (new_x, new_y + 1)


def get_distinct_sides(sides: list[TSide]) -> list[TSide]:
    distinct_sides: list[TSide] = []
    for raw_side in sides:
        for d_side in distinct_sides:
            if d_side & raw_side:
                d_side.update(raw_side)
                break
        else:
            distinct_sides.append(raw_side)
    assert len(sides) == len(distinct_sides)  # noqa: S101
    return distinct_sides


if __name__ == "__main__":
    print(task1())
    print(task2())
