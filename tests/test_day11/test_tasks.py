import pytest

from src.common import utils
from src.day11 import tasks


@pytest.mark.parametrize(
    ("initial", "blinks", "expected_res"),
    [
        pytest.param("125 17", 1, "253000 1 7", id="1 blink"),
        pytest.param("125 17", 2, "253 0 2024 14168", id="2 blinks"),
        pytest.param("125 17", 3, "512072 1 20 24 28676032", id="3 blinks"),
        pytest.param("125 17", 4, "512 72 2024 2 0 2 4 2867 6032", id="4 blinks"),
        pytest.param("125 17", 5, "1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32", id="5 blinks"),
        pytest.param(
            "125 17", 6, "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2", id="6 blinks"
        ),
    ],
)
def test_blink(initial: str, blinks: int, expected_res: str) -> None:
    stones = utils.to_ints(initial)
    for _ in range(blinks):
        stones = tasks.blink(stones)
    assert stones == utils.to_ints(expected_res)


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("example.txt", 55312, id="example"),
    ],
)
def test_task1(file: str, expected_res: int) -> None:
    assert tasks.task1(file) == expected_res
