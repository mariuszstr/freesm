from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.team import Team


def init():
    global poland
    global league
    global ekstraliga
    global druga_liga
    global torun
    global bydgoszcz
    global polonia
    global apator

    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", None)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)
    druga_liga = LeagueClass(league, "Polska 2 liga", 50, None, None)

    torun = City("Toruń", None, 200000, 30, 85)
    bydgoszcz = City("Bydgoszcz", None, 400000, 40, 55)

    polonia = Team(league, druga_liga, "Polonia", bydgoszcz, poland, 50, None)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, [polonia, ])
    polonia.derby_teams = [apator, ]


def test_constructor():
    init()

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

def test_eq():

    team1 = Team(league, druga_liga, "Polonia", bydgoszcz, poland, 50, None)
    team2 = Team(league, ekstraliga, "Apator", torun, poland, 99, None)
    team3 = Team(league, druga_liga, "Polonia", bydgoszcz, poland, 50, None)
    team4 = Team(league, ekstraliga, "Polonia", bydgoszcz, poland, 50, None)
    team5 = Team(league, ekstraliga, "Polonia", torun, poland, 50, None)
    team6 = Team(league, ekstraliga, "Polonia", torun, poland, 60, None)
    # note - compare only names
    assert team1 != team2
    assert team1 == team3
    assert team1 == team4
    assert team1 == team5
    assert team1 == team6
