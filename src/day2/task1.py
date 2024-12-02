import itertools

from src.common import utils


def is_safe(report: list[int]) -> bool:
    jumps = [a - b for a, b in itertools.pairwise(report)]
    min_jump, max_jump = min(jumps), max(jumps)
    is_monotonic = min_jump * max_jump > 0
    at_least = min(abs(min_jump), abs(max_jump))
    at_most = max(abs(min_jump), abs(max_jump))
    return is_monotonic and at_least >= 1 and at_most <= 3  # noqa: PLR2004


def main() -> None:
    reports = utils.read_lists()
    res = sum(is_safe(report) for report in reports)
    print(res)


if __name__ == "__main__":
    main()
