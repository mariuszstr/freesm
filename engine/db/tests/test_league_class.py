from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass


def test_constructor():
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)
    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)
    druga_liga = LeagueClass(league, "Polska 2 liga", 50, None, None)
    pierwsza_liga = LeagueClass(league, "Polska 1 liga", 70, ekstraliga, druga_liga)

    ekstraliga.previous_class = pierwsza_liga
    druga_liga.next_class = pierwsza_liga

    assert ekstraliga.league == league
    assert pierwsza_liga.league == league
    assert druga_liga.league == league

    assert ekstraliga.name == "Polska Ekstraliga"
    assert pierwsza_liga.name == "Polska 1 liga"
    assert druga_liga.name == "Polska 2 liga"

    assert ekstraliga.ability == 99
    assert pierwsza_liga.ability == 70
    assert druga_liga.ability == 50

    assert not ekstraliga.next_class
    assert ekstraliga.previous_class == pierwsza_liga

    assert pierwsza_liga.next_class == ekstraliga
    assert pierwsza_liga.previous_class == druga_liga

    assert druga_liga.next_class == pierwsza_liga
    assert not druga_liga.previous_class
