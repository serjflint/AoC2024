import collections

from src.common import utils


def main() -> None:
    a_arr, b_arr = utils.read()
    counts = collections.Counter(b_arr)
    res = sum(a * counts.get(a, 0) for a in a_arr)
    print(res)


if __name__ == "__main__":
    main()
