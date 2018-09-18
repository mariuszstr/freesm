from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.team import Team


def test_constructor():

    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)
    druga_liga = LeagueClass(league, "Polska 2 liga", 50, None, None)

    torun = City("Toruń", None, 200000, 30, 85)
    bydgoszcz = City("Bydgoszcz", None, 400000, 40, 55)

    polonia = Team(league, druga_liga, "Polonia", bydgoszcz, poland, 50, None)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, [polonia, ])
    polonia.derby_teams = [apator, ]

    assert polonia.league == league
    assert apator.league == league

    assert polonia.league_class == druga_liga
    assert apator.league_class == ekstraliga

    assert polonia.name == "Polonia"
    assert apator.name == "Apator"

    assert polonia.city == bydgoszcz
    assert apator.city == torun

    assert polonia.country == poland
    assert apator.country == poland

    assert polonia.ability == 50
    assert apator.ability == 99

    assert polonia.derby_teams == [apator, ]
    assert apator.derby_teams == [polonia, ]
