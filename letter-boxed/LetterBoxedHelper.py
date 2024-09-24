import LetterBoxedBase as lbb
from base import scraper

date_str = scraper.get_today_date()
game_data = scraper.load_puzzle_data(lbb.game_name, date_str)

letter_set = lbb.extract_letters(game_data)
nyt_word_list = lbb.extract_word_list(game_data)
nyt_solution = '-'.join(game_data['ourSolution']).lower()

nyt_one_solutions = lbb.one_word_solve(nyt_word_list, letter_set, False)
nyt_two_solutions = lbb.two_word_solve(nyt_word_list, letter_set, False)

two_solution_word_list = [word for lst in nyt_two_solutions for word in lst]
two_solution_word_list = list(set(two_solution_word_list))

# Load user's word list
user_word_file = 'my_words.txt'
user_word_list = lbb.load_user_words(user_word_file)

user_words_clean = lbb.clean_word_list(user_word_list, game_data)
lbb.write_user_wordlist(user_words_clean, user_word_file)  # TODO: Ask for confirmation before overwrite

if nyt_one_solutions:
    print(f'{len(nyt_one_solutions)} possible one-word solution(s)')
if nyt_two_solutions:
    print(f'{len(nyt_two_solutions)} possible two-word solution(s) featuring {len(two_solution_word_list)} unique words')

    found_two_solution_words = []
    subset_words = []

    for word in user_words_clean:
        if word in two_solution_word_list:
            found_two_solution_words.append(word)
        for solution_word in two_solution_word_list:
            if word in solution_word and word not in found_two_solution_words and word not in subset_words:
                subset_words.append(word)

    if found_two_solution_words:
        print(f'You have found {len(found_two_solution_words)} of {len(two_solution_word_list)} words for a two-word solution:')
        for word in found_two_solution_words:
            print(word)
    else:
        print('You have not yet found any of the words required for a two-word solution')

    if subset_words:
        print('The following words are a subset of a solution word:')
        for word in subset_words:
            print(word)

lbb.suggest_beginning_letters(user_words_clean, letter_set)
lbb.suggest_end_letters(user_words_clean, letter_set)

# user_solutions = [
#     lbb.one_word_solve(user_word_list, letter_set),
#     lbb.two_word_solve(user_word_list, letter_set),
#     lbb.three_word_solve(user_word_list, letter_set)
#     ]

user_solutions = [lbb.two_word_solve(user_words_clean, letter_set)]

for solution_list in user_solutions:
    lbb.print_solutions(solution_list)
