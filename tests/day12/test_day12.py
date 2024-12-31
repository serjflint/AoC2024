import pytest

from src import day12 as tasks


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("continuous.txt", 140, id="continuous"),
        pytest.param("separate.txt", 772, id="separate"),
        pytest.param("larger.txt", 1930, id="larger"),
    ],
)
def test_task1(file: str, expected_res: int) -> None:
    assert tasks.task1(file) == expected_res


@pytest.mark.parametrize(
    ("file", "expected_res"),
    [
        pytest.param("continuous.txt", 80, id="continuous"),
        pytest.param("separate.txt", 436, id="separate"),
        pytest.param("eshaped.txt", 236, id="eshaped"),
        pytest.param("abba.txt", 368, id="abba"),
        pytest.param("larger.txt", 1206, id="larger"),
    ],
)
def test_task2(file: str, expected_res: int) -> None:
    assert tasks.task2(file) == expected_res
