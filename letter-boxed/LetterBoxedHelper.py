import LetterBoxedBase as lbb
from base import scraper

date_str = scraper.get_today_date()
game_data = scraper.load_puzzle_data(lbb.game_name, date_str)

# Get letters for current puzzle
letter_set = lbb.extract_letters(game_data)

# Load user's word list
user_word_file = 'my_words.txt'
user_word_list = lbb.load_user_words(user_word_file)

user_words_clean = lbb.clean_word_list(user_word_list, game_data)
lbb.write_user_wordlist(user_words_clean, user_word_file)  # TODO: Ask for confirmation before overwrite

lbb.suggest_beginning_letters(user_words_clean, letter_set)
lbb.suggest_end_letters(user_words_clean, letter_set)

solutions = [
    lbb.one_word_solve(user_word_list, letter_set),
    lbb.two_word_solve(user_word_list, letter_set),
    lbb.three_word_solve(user_word_list, letter_set)
    ]

for solution_list in solutions:
    lbb.print_solutions(solution_list)
