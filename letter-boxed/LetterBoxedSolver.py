import LetterBoxedBase as lbb
from base import scraper

date_str = scraper.get_today_date()
game_data = scraper.load_puzzle_data(lbb.game_name, date_str)

# Get letters, word list, and chosen solution for current puzzle
letter_set = lbb.extract_letters(game_data)
word_list = lbb.extract_word_list(game_data)
nyt_solution = '-'.join(game_data['ourSolution']).lower()

solutions = [
    lbb.one_word_solve(word_list, letter_set),
    lbb.two_word_solve(word_list, letter_set),
    lbb.three_word_solve(word_list, letter_set)
    ]

for solution_list in solutions:
    lbb.print_solutions(solution_list)

print('\nNYT\'s solution:\n' + nyt_solution)
