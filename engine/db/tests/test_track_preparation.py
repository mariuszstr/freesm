from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.stadium import Stadium
from engine.db.team import Team
from engine.db.track import Track
from engine.db.track_preparation import TrackPreparation


def init():
    global poland
    global league
    global ekstraliga
    global torun
    global apator
    global stadium
    global track
    global track_preparation
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", None)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)

    torun = City("Toruń", None, 200000, 30, 85)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, None)

    stadium = Stadium("Motoarena", poland, apator, 20000, 99)
    track = Track(stadium, 300, 30, 45)
    track_preparation = TrackPreparation(track, 90, 50)


def test_constructor():
    init()
    assert track_preparation.track == track
    assert track_preparation.grippness == 50
    assert track_preparation.water == 90


def test_eq():
    init()
    stadium1 = Stadium("Motoarena", poland, apator, 20000, 99)
    stadium2 = Stadium("Motoarena2", poland, apator, 20000, 99)

    track1 = Track(stadium1, 300, 30, 45)
    track2 = Track(stadium2, 300, 30, 45)

    track_preparation1 = TrackPreparation(track1, 90, 50)
    track_preparation2 = TrackPreparation(track2, 90, 50)
    track_preparation3 = TrackPreparation(track1, 80, 50)
    track_preparation4 = TrackPreparation(track1, 90, 60)
    track_preparation5 = TrackPreparation(track1, 90, 50)

    assert track_preparation1 != track_preparation2
    assert track_preparation1 != track_preparation3
    assert track_preparation1 != track_preparation4
    assert track_preparation1 == track_preparation5
