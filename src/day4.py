import typing as tp

from src.common import utils

FILENAME = utils.with_suffix(__file__)

MASKS = [
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],  # top-left
    [(0, 0), (0, -1), (0, -2), (0, -3)],  # top
    [(0, 0), (1, -1), (2, -2), (3, -3)],  # top-right
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # right
    [(0, 0), (1, 1), (2, 2), (3, 3)],  # bottom-right
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # bottom
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)],  # bottom-left
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],  # left
]
WORD = "XMAS"


def check_mask(field: list[str], pos: tuple[int, int], mask: list[tuple[int, int]], word: str) -> bool:
    pos_x, pos_y = pos
    for idx, (dx, dy) in enumerate(mask):
        on_field = 0 <= pos_y + dy < len(field) and 0 <= pos_x + dx < len(field[pos_y + dy])
        if not on_field:
            break
        if field[pos_y + dy][pos_x + dx] != word[idx]:
            break
    else:
        return True
    return False


def yield_xmas(field: list[str], pos: tuple[int, int]) -> tp.Iterator[str]:
    for mask in MASKS:
        if check_mask(field=field, pos=pos, mask=mask, word=WORD):
            yield WORD


def task1(filename: str = FILENAME) -> int:
    field = utils.read_lines(filename)
    res = 0
    for pos_y in range(len(field)):
        for pos_x in range(len(field[pos_y])):
            for _ in yield_xmas(field, (pos_x, pos_y)):
                res += 1
    return res


MASKS_X_MAS = [
    [[(-1, -1), (0, 0), (1, 1)], [(1, -1), (0, 0), (-1, 1)]],  # MMSS
    [[(-1, -1), (0, 0), (1, 1)], [(-1, 1), (0, 0), (1, -1)]],  # MSMS
    [[(1, -1), (0, 0), (-1, 1)], [(1, 1), (0, 0), (-1, -1)]],  # SMSM
    [[(-1, 1), (0, 0), (1, -1)], [(1, 1), (0, 0), (-1, -1)]],  # SSMM
]
WORD_X_MAS = "MAS"


def yield_x_mas(field: list[str], pos: tuple[int, int]) -> tp.Iterator[str]:
    for mask1, mask2 in MASKS_X_MAS:
        flag1, flag2 = False, False
        if check_mask(field=field, pos=pos, mask=mask1, word=WORD_X_MAS):
            flag1 = True
        if check_mask(field=field, pos=pos, mask=mask2, word=WORD_X_MAS):
            flag2 = True
        if flag1 and flag2:
            yield WORD_X_MAS


def task2(filename: str = FILENAME) -> int:
    field = utils.read_lines(filename)
    res = 0
    for pos_y in range(len(field)):
        for pos_x in range(len(field[pos_y])):
            for _ in yield_x_mas(field, (pos_x, pos_y)):
                res += 1
    return res


if __name__ == "__main__":
    print(task1())
    print(task2())
