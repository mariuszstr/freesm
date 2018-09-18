from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.stadium import Stadium
from engine.db.team import Team
from engine.db.track import Track


def test_constructor():
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)

    torun = City("Toruń", None, 200000, 30, 85)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, None)

    stadium = Stadium("Motoarena", poland, apator, 20000, 99)
    track = Track(stadium, 300, 30, 45)
    assert track.stadium == stadium
    assert track.length == 300
    assert track.first_corner_angle == 30
    assert track.second_corner_angle == 45