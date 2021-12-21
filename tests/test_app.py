from players import PlayerSearch
from utils import player_name


def test_not_found():
    player_obj = PlayerSearch()
    result = player_obj.find_players(2)
    # Will results will result as zero pairs
    assert len(result) == 0


def test_avoid_same_player():
    player_obj = PlayerSearch()
    result = player_obj.find_players(140)
    times_found = 0

    for pair in result:
        if "Brevin Knight" in [player_name(pair[0]), player_name(pair[1])]:
            times_found += 1
            assert int(pair[0]["h_in"]) == 70
    # It means that any player won't be duplicated summing itself twice
    assert times_found == 1


def test_example_case():
    player_obj = PlayerSearch()

    result = player_obj.find_players(139)
    assert len(result) == 2

    """
    Given example:
    > app 139

    - Brevin Knight         Nate Robinson
    - Nate Robinson         Mike Wilks
    """

    pair_1 = result[0]
    pair_2 = result[1]
    assert player_name(pair_1[0]) == "Brevin Knight"
    assert player_name(pair_1[1]) == "Nate Robinson"

    assert player_name(pair_2[0]) == "Nate Robinson"
    assert player_name(pair_2[1]) == "Mike Wilks"
