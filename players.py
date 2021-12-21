import json
import requests


class PlayerSearch:
    _player_data = {}
    API_URL = "https://mach-eight.uc.r.appspot.com/"

    def __init__(self):
        self.retrieve_players_data()

    def retrieve_players_data(self):
        result = requests.get(self.API_URL)
        json_data = json.loads(result.text)
        self._player_data = json_data.get("values", {})

    def find_players(self, target_value) -> list:
        values_dict = {}
        pairs_found = []
        for player in self._player_data:
            # Key (value) to find in previous iterated players
            # matching with current one to sum target_value
            rest_value = str(target_value - int(player.get("h_in")))
            # if target_
            if rest_value in values_dict:
                # Creating pairs of every single
                # player added in this list and adding to pairs
                players = [[p, player] for p in values_dict[rest_value]]
                pairs_found.extend(players)

            current_data = [player]
            # In case that another previous player has
            # same height we'll use a list to handle it
            if player["h_in"] in values_dict:
                current_data += values_dict[player["h_in"]]

            # Just storing all my players indexed by h_in considering that
            # python dict is a hashmap, in average we'll have a simple O(1)
            values_dict[player["h_in"]] = current_data
        return pairs_found
