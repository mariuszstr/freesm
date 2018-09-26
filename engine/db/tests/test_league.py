from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass


def init():
    global poland
    global league
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 123)

def test_constructor():
    init()
    assert league.name == "polish league"
    assert league.country == poland
    assert league.classes == 123

def test_ability():
    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)
    druga_liga = LeagueClass(league, "Polska 2 liga", 50, None, None)
    pierwsza_liga = LeagueClass(league, "Polska 1 liga", 70, ekstraliga, druga_liga)
    league.classes = [ekstraliga, pierwsza_liga, druga_liga]
    assert league.ability == 73

    ekstraliga.ability = 3
    pierwsza_liga.ability = 4
    druga_liga.ability = 5

    assert league.ability == 4


def test_eq():
    poland = Country("Poland", 38000000, 30, 60)
    league1 = League(poland, "polish league", 99)
    league2 = League(poland, "english league", 99)
    league3 = League(poland, "english league", 59)

    assert league1 != league2
    assert league1 != league3
    assert league2 == league3  # it is not a bug, it's a feature - compare only names.
