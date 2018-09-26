from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.stadium import Stadium
from engine.db.team import Team

def init():
    global poland
    global league
    global ekstraliga
    global torun
    global apator
    global stadium
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", None)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)

    torun = City("Toruń", None, 200000, 30, 85)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, None)
    stadium = Stadium("Motoarena", poland, apator, 20000, 99)


def test_constructor():
    init()
    assert stadium.name == "Motoarena"
    assert stadium.country == poland
    assert stadium.team == apator
    assert stadium.sits == 20000
    assert stadium.ability == 99


def test_eq():
    init()
    apator2 = Team(league, ekstraliga, "Apator2", torun, poland, 99, None)

    stadium1 = Stadium("Motoarena", poland, apator, 20000, 99)
    stadium2 = Stadium("Motoarena2", poland, apator, 20000, 99)
    stadium3 = Stadium("Motoarena", poland, apator2, 20000, 99)
    stadium4 = Stadium("Motoarena", poland, apator, 2000, 99)
    stadium5 = Stadium("Motoarena", poland, apator, 20000, 9)

    # note: equals only name
    assert stadium1 != stadium2
    assert stadium1 == stadium3
    assert stadium1 == stadium4
    assert stadium1 == stadium5
    assert stadium3 == stadium4
    assert stadium3 == stadium5
    assert stadium2 != stadium3

