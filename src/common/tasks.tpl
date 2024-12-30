from src.common import utils

def task1(filename: str = "input.txt") -> int:
    data = utils.read_text(filename)
    return len(data)


def task2(filename: str = "input.txt") -> int:
    data = utils.read_text(filename)
    return len(data)


if __name__ == "__main__":
    print(task1())
    print(task2())
