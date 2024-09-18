from datetime import date
import requests
import json
import sys
import re
import os

game_data_search_pattern = r'gameData\s*=\s*(\{.*?})<'
base_url = 'https://www.nytimes.com/puzzles/'
cache_folder = 'gamedata_cache'
cache_file_suffix = 'gamedata.json'


def fetch_page(game_name):
    response = requests.get(base_url + game_name)
    if response.status_code != 200:
        sys.exit('Failed to load page with status: ' + str(response.status_code))
    else:
        page = response.text

    return page


def extract_game_data(page):
    pattern = re.compile(game_data_search_pattern)
    data_string = re.search(pattern, page).group(1)
    game_data = json.loads(data_string)

    return game_data


def write_game_data_cache(game_data, cache_file):
    if not os.path.exists(f'{cache_folder}'):
        os.mkdir(cache_folder)

    with open(cache_file, 'w') as data_file:
        json.dump(game_data, data_file, indent=4)
    print(f'Game data written to {cache_file}')

    return


def get_today_date():
    today_date = date.today().strftime('%Y-%m-%d')

    return today_date


def load_puzzle_data(game_name, date_str):
    cache_file = f'{cache_folder}/{date_str}_{game_name}_{cache_file_suffix}'
    if os.path.exists(cache_file):
        with open(cache_file) as game_data_file:
            game_data = json.load(game_data_file)
        print(f'Game data loaded from {cache_file}')
    else:
        page = fetch_page(game_name)
        print(f'Game data fetched from {base_url + game_name}')
        game_data = extract_game_data(page)
        write_game_data_cache(game_data, cache_file)

    return game_data
