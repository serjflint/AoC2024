import itertools

from src.common import utils


def is_safe(report: list[int]) -> bool:
    jumps = [a - b for a, b in itertools.pairwise(report)]
    min_jump, max_jump = min(jumps), max(jumps)
    is_monotonic = min_jump * max_jump > 0
    at_least = min(abs(min_jump), abs(max_jump))
    at_most = max(abs(min_jump), abs(max_jump))
    return is_monotonic and at_least >= 1 and at_most <= 3  # noqa: PLR2004


def task1() -> int:
    reports = utils.read_lists()
    return sum(is_safe(report) for report in reports)


def problem_dampener(report: list[int]) -> bool:
    if is_safe(report):
        return True
    for idx in range(len(report)):
        dampened_report = report[:idx] + report[idx + 1 :]
        if is_safe(dampened_report):
            return True
    return False


def task2() -> int:
    reports = utils.read_lists()
    return sum(problem_dampener(report) for report in reports)


if __name__ == "__main__":
    print(task1())
    print(task2())
