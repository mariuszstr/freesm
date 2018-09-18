from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.stadium import Stadium
from engine.db.team import Team


def test_constructor():
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)

    torun = City("Toruń", None, 200000, 30, 85)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, None)

    stadium = Stadium("Motoarena", poland, apator, 20000, 99)
    assert stadium.name == "Motoarena"
    assert stadium.country == poland
    assert stadium.team == apator
    assert stadium.sits == 20000
    assert stadium.ability == 99
