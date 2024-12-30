from src.common import utils

FILENAME = utils.with_suffix(__file__)


def task1(filename: str = FILENAME) -> int:
    data = utils.read_text(filename)
    return len(data)


def task2(filename: str = FILENAME) -> int:
    data = utils.read_text(filename)
    return len(data)


if __name__ == "__main__":
    print(task1())
    print(task2())
