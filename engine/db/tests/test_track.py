from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.stadium import Stadium
from engine.db.team import Team
from engine.db.track import Track


def init():
    global poland
    global league
    global ekstraliga
    global torun
    global apator
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", None)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)

    torun = City("Toruń", None, 200000, 30, 85)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, None)


def test_constructor():
    init()
    stadium = Stadium("Motoarena", poland, apator, 20000, 99)
    track = Track(stadium, 300, 30, 45)
    assert track.stadium == stadium
    assert track.length == 300
    assert track.first_corner_angle == 30
    assert track.second_corner_angle == 45


def test_eq():
    init()

    stadium1 = Stadium("Motoarena", poland, apator, 20000, 99)
    stadium2 = Stadium("Motoarena2", poland, apator, 20000, 99)

    track1 = Track(stadium1, 300, 30, 45)
    track2 = Track(stadium1, 300, 40, 45)
    track3 = Track(stadium1, 300, 30, 50)
    track4 = Track(stadium2, 300, 30, 45)
    track5 = Track(stadium1, 400, 30, 45)
    track6 = Track(stadium1, 300, 30, 45)
    # note - equals only stadium and length
    assert track1 == track2
    assert track1 == track3
    assert track1 != track4
    assert track1 != track5
    assert track1 == track6
