from engine.db.city import City
from engine.db.country import Country
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.rider import Rider
from engine.db.stadium import Stadium
from engine.db.team import Team
from engine.db.track import Track
from engine.db.track_preparation import TrackPreparation
from engine.heat.skill_for_track import get_skill_for_track


def init():
    global track
    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", None)

    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)

    torun = City("Toruń", None, 200000, 30, 85)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, None)

    stadium = Stadium("Motoarena", poland, apator, 20000, 99)
    track = Track(stadium, 300, 30, 45)


def test_get_skill_for_track_hard_track():
    init()
    assert get_skill_for_track(Rider(1, 2, 3, 4, 5, 77, 7, 8, 9, 10), TrackPreparation(track, 0, 0)) == 77


def test_get_skill_for_track_slick_track():
    init()
    assert get_skill_for_track(Rider(1, 2, 3, 4, 5, 6, 77, 8, 9, 10), TrackPreparation(track, 100, 50)) == 77


def test_get_skill_for_track_grippy_track():
    init()
    assert get_skill_for_track(Rider(1, 2, 3, 4, 5, 6, 7, 77, 9, 10), TrackPreparation(track, 0, 100)) == 77


def test_get_skill_for_track_mud_track():
    init()
    assert get_skill_for_track(Rider(1, 2, 3, 4, 5, 6, 7, 8, 77, 10), TrackPreparation(track, 100, 100)) == 77


def test_get_skill_for_track_normal_track():
    init()
    assert get_skill_for_track(Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 77), TrackPreparation(track, 0, 50)) == 77
