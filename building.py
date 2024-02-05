from itertools import permutations
from pprint import pprint


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
    option_row_1: tuple[int, ...],
    option_row_2: tuple[int, ...],
    option_row_3: tuple[int, ...],
    option_row_4: tuple[int, ...],
    clue: list[int],
    paralel_clue: list[int],
) -> bool:
    for i in range(len(option_row_1)):
        column = (option_row_1[i], option_row_2[i], option_row_3[i], option_row_4[i])
        if not check_row(column, clue[i]) or not check_row(
            column[::-1], paralel_clue[::-1][i]
        ):
            return False
    return True


def generate_options(clue: int, paralel_clue: int) -> list[tuple[int, ...]]:
    building_types = [1, 2, 3, 4]
    valid_options = []

    for option in permutations(building_types):
        if check_row(option, clue) and check_row(option[::-1], paralel_clue):
            valid_options.append(option)

    return valid_options


def solve_puzzle(clues: list[int]) -> list[tuple[int, ...]] | None:
    total_options = [generate_options(clues[15 - i], clues[i + 4]) for i in range(0, 4)]
    valid_solutions = []

    for option_row_1 in total_options[0]:
        for option_row_2 in total_options[1]:
            for option_row_3 in total_options[2]:
                for option_row_4 in total_options[3]:
                    if check_grid(
                        option_row_1,
                        option_row_2,
                        option_row_3,
                        option_row_4,
                        clues[:4],
                        clues[8:12],
                    ):
                        valid_solutions.append(
                            [option_row_1, option_row_2, option_row_3, option_row_4]
                        )

    if valid_solutions:
        return valid_solutions[0]
    return None


if __name__ == "__main__":
    initial_clues = [0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0]
    pprint(solve_puzzle(initial_clues))
