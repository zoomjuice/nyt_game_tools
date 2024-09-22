from itertools import permutations

game_name = 'letter-boxed'


def extract_letters(game_data):
    letters = {char.lower() for string in game_data['sides'] for char in string}

    return letters


def generate_disallowed_pairs(game_data):
    sides = [side.lower() for side in game_data['sides']]
    all_pairs = []
    for side in sides:
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


def clean_word_list(word_list, game_data):
    word_list_unique = []

    for word in word_list:
        if word in word_list_unique:
            print(f'Removing "{word}" (duplicate)')
        else:
            word_list_unique.append(word)

    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    allowed_letters = extract_letters(game_data)
    disallowed_pairs = generate_disallowed_pairs(game_data)
    disallowed_letters = alphabet - allowed_letters
    invalid_words = []

    for word in word_list_unique:
        for pair in disallowed_pairs:
            if pair in word:
                invalid_words.append(word)
                print(f'Removing "{word}" (contains invalid pair "{pair}")')
        for letter in disallowed_letters:
            if letter in word:
                invalid_words.append(word)
                print(f'Removing "{word}" (contains invalid letter "{letter}")')

    word_list_clean = [word for word in word_list_unique if word not in invalid_words]
    word_list_clean.sort()

    return word_list_clean


def write_user_wordlist(word_list, word_file):
    with open(word_file, 'w') as w:
        for word in word_list:
            w.write(f'{word}\n')
        print(f'Wrote {word_file}')


def one_word_solve(word_list, letter_set, printable=True):
    solution_list = [1] if printable else []
    for word in word_list:
        if set(word) == letter_set:
            solution_list.append([word])

    return solution_list


def two_word_solve(word_list, letter_set, printable=True):
    solution_list = [2] if printable else []
    for word in word_list:
        matches = [w for w in word_list if word[-1] == w[0] and w != word]
        for match in matches:
            if set(word + match) == letter_set:
                solution_list.append([word, match])

    return solution_list


def three_word_solve(word_list, letter_set, printable=True):
    solution_list = [3] if printable else []
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


def suggest_end_letters(word_list, letter_set):
    end_letters = {word[-1] for word in word_list}
    missing_letters = list(letter_set - end_letters)
    missing_letters.sort()
    print(f'You have no words ending in the following letters: {', '.join(missing_letters)}')


def suggest_beginning_letters(word_list, letter_set):
    beginning_letters = {word[0] for word in word_list}
    missing_letters = list(letter_set - beginning_letters)
    missing_letters.sort()
    print(f'You have no words beginning with the following letters: {', '.join(missing_letters)}')
