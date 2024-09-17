from itertools import permutations

game_name = 'letter-boxed'


def extract_letters(game_data):
    letters = {char.lower() for string in game_data['sides'] for char in string}

    return letters


def extract_sides(game_data):
    sides = [side.lower() for side in game_data['sides']]

    return sides


def generate_disallowed_pairs(side_lst):
    all_pairs = []

    for side in side_lst:
        pairs = permutations(side, 2)
        all_pairs.extend(''.join(pair) for pair in pairs)

    return all_pairs


def extract_word_list(game_data):
    word_list = []
    for item in game_data['dictionary']:
        word = item.strip('"').lower()
        word_list.append(word)

    return word_list


def load_user_words(word_file):
    with open(word_file, 'r') as wordfile:
        word_list = []
        for line in wordfile:
            word = line.strip().lower()
            word_list.append(word)

    return word_list


def write_user_wordlist(word_dict, word_file):
    with open(word_file, 'w') as word_file:
        for word in word_dict.keys():
            word_file.write(f'{word}\n')


def one_word_solve(word_list, letter_set):
    solution_list = [1]
    for word in word_list:
        if set(word) == letter_set:
            solution_list.append([word])

    return solution_list


def two_word_solve(word_list, letter_set):
    solution_list = [2]
    for word in word_list:
        matches = [w for w in word_list if word[-1] == w[0] and w != word]
        for match in matches:
            if set(word + match) == letter_set:
                solution_list.append([word, match])

    return solution_list


def three_word_solve(word_list, letter_set):
    solution_list = [3]
    ab = [[a, b] for a in word_list for b in word_list if a[-1] == b[0] and set(a + b) != letter_set]
    for pair in ab:
        pair_str = ''.join(pair)
        matches = [w for w in word_list if pair_str[-1] == w[0]]
        for match in matches:
            if set(pair_str + match) == letter_set:
                solution_list.append([pair[0], pair[1], match])

    return solution_list


def print_solutions(solution_list):
    num_words = solution_list[0]
    print(f'\n{num_words}-word solutions:')
    solution_list.pop(0)
    if not solution_list:
        print('None')
    else:
        for solution in solution_list:
            print('-'.join(solution))
