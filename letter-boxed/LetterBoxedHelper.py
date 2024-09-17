import LetterBoxedBase as lb
from base import scraper

date_str = scraper.get_today_date()
game_data = scraper.load_puzzle_data(lb.game_name, date_str)

# Get letters for current puzzle
letter_set = lb.extract_letters(game_data)

# Load user's word list
user_word_file = 'my_words.txt'
user_word_list = lb.load_user_words(user_word_file)

solutions = [
    lb.one_word_solve(user_word_list, letter_set),
    lb.two_word_solve(user_word_list, letter_set),
    lb.three_word_solve(user_word_list, letter_set)
    ]

for solution_list in solutions:
    lb.print_solutions(solution_list)
