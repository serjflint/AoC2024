from src.common import utils


def main() -> None:
    a_arr, b_arr = utils.read_pairs()
    res = sum(abs(a - b) for a, b in zip(a_arr, b_arr, strict=False))
    print(res)


if __name__ == "__main__":
    main()
