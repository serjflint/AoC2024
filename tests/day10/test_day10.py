import pytest

from src import day10 as tasks


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("simple_trail.txt", 2, id="simple_trail"),
        pytest.param("complex_trail.txt", 4, id="complex_trail"),
        pytest.param("two_trails.txt", 3, id="two_trails"),
        pytest.param("larger_example.txt", 36, id="larger_example"),
    ],
)
def test_task1(file: str, expected_res: int) -> None:
    assert tasks.task1(file) == expected_res


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("simple_rating.txt", 3, id="simple_rating"),
        pytest.param("complex_trail.txt", 13, id="complex_trail"),
        pytest.param("huge_rating.txt", 227, id="huge_rating"),
        pytest.param("larger_example.txt", 81, id="larger_example"),
    ],
)
def test_task2(file: str, expected_res: int) -> None:
    assert tasks.task2(file) == expected_res
