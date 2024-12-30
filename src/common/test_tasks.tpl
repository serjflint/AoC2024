import pytest

from src.day import tasks


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("example.txt", 0, id="example"),
    ],
)
def test_task1(file: str, expected_res: int) -> None:
    assert tasks.task1(file) == expected_res


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("example.txt", 0, id="example"),
    ],
)
def test_task2(file: str, expected_res: int) -> None:
    assert tasks.task2(file) == expected_res
