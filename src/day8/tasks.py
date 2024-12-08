import collections
import itertools as it

from src.common import utils


def get_freq(arr: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    max_x, max_y = len(arr[0]), len(arr)
    frequencies = collections.defaultdict(list)
    for x in range(max_x):
        for y in range(max_y):
            freq = arr[y][x]
            if freq == ".":
                continue
            frequencies[freq].append((x, y))
    return frequencies


def task1() -> int:
    lines = [list(line.strip()) for line in utils.read_lines()]
    max_x, max_y = len(lines[0]), len(lines)
    frequencies = get_freq(lines)

    antinodes = [["." for _ in range(max_x)] for _ in range(max_y)]
    for points in frequencies.values():
        for one, two in it.permutations(points, 2):
            dx, dy = two[0] - one[0], two[1] - one[1]
            ax, ay = two[0] + dx, two[1] + dy
            if 0 <= ax < max_x and 0 <= ay < max_y:
                antinodes[ay][ax] = "#"

    return sum(1 for _ in utils.where(antinodes, "#"))


def task2() -> int:
    lines = [list(line.strip()) for line in utils.read_lines()]
    max_x, max_y = len(lines[0]), len(lines)
    frequencies = get_freq(lines)

    antinodes = [["." for _ in range(max_x)] for _ in range(max_y)]
    for points in frequencies.values():
        for one, two in it.permutations(points, 2):
            dx, dy = two[0] - one[0], two[1] - one[1]
            ax, ay = one
            while True:
                ax, ay = ax + dx, ay + dy
                if 0 <= ax < max_x and 0 <= ay < max_y:
                    antinodes[ay][ax] = "#"
                else:
                    break

    return sum(1 for _ in utils.where(antinodes, "#"))


if __name__ == "__main__":
    print(task1())
    print(task2())
