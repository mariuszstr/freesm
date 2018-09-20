from engine.db.country import Country
from engine.db.league import League


def test_constructor():
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)
    assert league.name == "polish league"
    assert league.country == poland
    assert league.ability == 99


def test_eq():
    poland = Country("Poland", 38000000, 30, 60)
    league1 = League(poland, "polish league", 99)
    league2 = League(poland, "english league", 99)
    league3 = League(poland, "english league", 59)

    assert league1 != league2
    assert league1 != league3
    assert league2 == league3  # it is not a bug, it's a feature - compare only names.
