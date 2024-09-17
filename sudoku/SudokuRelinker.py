import SudokuBase as sb
from base import scraper

preferred_site = 'exchange'
sites = {'exchange': 'https://sudokuexchange.com/play/?s=',
         'coach': 'https://sudoku.coach/en/play/'}

date_str = scraper.get_today_date()
game_data = scraper.load_puzzle_data(sb.game_name, date_str)

# Extract 81-character puzzle strings from game data
puzzle_strings = {difficulty: sb.extract_puzzle_string(game_data, difficulty) for difficulty in ['easy', 'medium', 'hard']}

# Provide user with new links for each puzzle
sb.print_links(puzzle_strings, sites[preferred_site], date_str)
