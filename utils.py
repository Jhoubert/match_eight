# It should be handled by dataclass.
def player_name(player):
    return f"{player.get('first_name')} {player.get('last_name')}"
