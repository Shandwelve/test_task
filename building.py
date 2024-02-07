from itertools import permutations, product
from pprint import pprint

GRID_SIZE = 4
TOTAL_CLUES = GRID_SIZE**2
BUILDING_TYPES = [1, 2, 3, 4]


def check_row(row: tuple[int, ...], clue: int) -> bool:
    if len(set(row)) < len(row):
        return False

    vision, current_option = 1, row[0]

    for option in row[1:]:
        if option > current_option:
            current_option = option
            vision += 1

    return vision == clue or clue == 0


def check_grid(
    options: tuple[tuple[int, ...]],
    clue: list[int],
    paralel_clue: list[int],
) -> bool:
    for i in range(len(options[0])):
        column = tuple(options[j][i] for j in range(GRID_SIZE))
        if not check_row(column, clue[i]) or not check_row(
            column[::-1], paralel_clue[::-1][i]
        ):
            return False
    return True


def generate_options(clue: int, paralel_clue: int) -> list[tuple[int, ...]]:
    valid_options = []

    for option in permutations(BUILDING_TYPES):
        if check_row(option, clue) and check_row(option[::-1], paralel_clue):
            valid_options.append(option)

    return valid_options


def solve_puzzle(clues: list[int]) -> list[tuple[int, ...]] | None:
    total_options = [
        generate_options(clues[TOTAL_CLUES - i - 1], clues[GRID_SIZE + i])
        for i in range(0, GRID_SIZE)
    ]
    valid_solutions = []

    for option_rows in product(*total_options):
        if check_grid(
            option_rows,
            clues[:GRID_SIZE],
            clues[GRID_SIZE * 2: GRID_SIZE * 3],
        ):
            valid_solutions.append(option_rows)

    if valid_solutions:
        return valid_solutions[0]
    return None


if __name__ == "__main__":
    initial_clues = [0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0]
    pprint(solve_puzzle(initial_clues))
