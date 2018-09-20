from engine.db.date import Date
from engine.db.json_save_load.game_state import GameState


def test_constructor():
    date = Date(1, 1, 2018)
    game_state = GameState(date)
    assert game_state.date == date

def test_eq():
    date1 = Date(1, 1, 2018)
    date2 = Date(2, 1, 2018)
    date3 = Date(3, 1, 2018)

    game_state1 = GameState(date1)
    game_state2 = GameState(date2)
    game_state3 = GameState(date3)
    game_state4 = GameState(date1)
    game_state5 = GameState(date2)

    assert game_state1 != game_state2
    assert game_state1 != game_state3
    assert game_state1 == game_state4
    assert game_state1 != game_state5
    assert game_state2 != game_state3
    assert game_state2 != game_state4
    assert game_state2 == game_state5
    assert game_state4 != game_state5
