import collections
import itertools

from src.common import utils


def parse(lines: list[str]) -> tuple[dict[int, set[int]], list[list[int]]]:
    rules: dict[int, set[int]] = collections.defaultdict(set)
    it = iter(lines)
    for line in it:
        line = line.strip()  # noqa: PLW2901
        if not line:
            break
        a, b = line.split("|")
        rules[int(a)].add(int(b))

    updates: list[list[int]] = []
    for line in it:
        line = line.strip()  # noqa: PLW2901
        if not line:
            break
        updates.append([int(a) for a in line.split(",")])
    return rules, updates


def is_ordered(update: list[int], rules: dict[int, set[int]]) -> bool:
    for page in update:
        if page not in rules:
            continue
        for other in rules[page]:
            if other not in update:
                continue
            if not update.index(page) < update.index(other):
                return False
    return True


def task1() -> int:
    rules, updates = parse(utils.read_lines())
    res = 0
    for update in updates:
        if not is_ordered(update, rules):
            middle = (len(update) - 1) // 2
            res += update[middle]
    return res


def task2() -> int:
    rules, updates = parse(utils.read_lines())
    res = 0
    for update in updates:
        if is_ordered(update, rules):
            continue
        while not is_ordered(update, rules):
            for a, b in itertools.permutations(update, 2):
                if a==b: continue
                pos_a, pos_b = update.index(a), update.index(b)
                if pos_a < pos_b:
                    if b in rules and a in rules[b]:
                        update[pos_a], update[pos_b] = update[pos_b], update[pos_a]
                elif pos_a > pos_b:
                    if a in rules and b in rules[a]:
                        update[pos_a], update[pos_b] = update[pos_b], update[pos_a]
        middle = (len(update) - 1) // 2
        res += update[middle]
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
