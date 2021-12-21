import sys

from players import PlayerSearch
from utils import player_name

if __name__ == "__main__":

    # It could be handled better using 'click' library.
    if len(sys.argv) < 2:
        print("Missing parameters\nExample: python app.py 130")
        exit(1)
    target_value = 0  # making linter happy.
    try:
        target_value = int(sys.argv[1])

    except ValueError:
        print(f"Invalid value for '{sys.argv[1]}'")
        exit(1)

    search_player = PlayerSearch()
    result_pairs = search_player.find_players(target_value)
    if len(result_pairs) > 0:
        for pair in result_pairs:
            print(f"{player_name(pair[0])} \t {player_name(pair[1])}")
    else:
        print("No matches found")
