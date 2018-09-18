from engine.db.country import Country
from engine.db.league import League


def test_constructor():
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)
    assert league.name == "polish league"
    assert league.country == poland
    assert league.ability == 99
