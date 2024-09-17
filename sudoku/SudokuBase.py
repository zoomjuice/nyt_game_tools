game_name = 'sudoku'


def extract_puzzle_string(game_data, difficulty):
    puzzle_string = ''.join(map(str, game_data[difficulty]['puzzle_data']['puzzle']))
    return puzzle_string


def print_links(puzzle_dict: dict, link_prefix, date):
    print('NYT sudoku puzzles for ' + date)
    for difficulty, puzzle in puzzle_dict.items():
        puzzle_link = link_prefix + puzzle
        print(f'{difficulty.capitalize()}: {puzzle_link}')
