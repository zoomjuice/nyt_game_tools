import LetterBoxedBase as lbb
from base import scraper

date_str = scraper.get_today_date()
game_data = scraper.load_puzzle_data(lbb.game_name, date_str)

# Get letters for current puzzle
letter_set = lbb.extract_letters(game_data)

# Load user's word list
user_word_file = 'my_words.txt'
user_word_list = lbb.load_user_words(user_word_file)

solutions = [
    lbb.one_word_solve(user_word_list, letter_set),
    lbb.two_word_solve(user_word_list, letter_set),
    lbb.three_word_solve(user_word_list, letter_set)
    ]

for solution_list in solutions:
    lbb.print_solutions(solution_list)
