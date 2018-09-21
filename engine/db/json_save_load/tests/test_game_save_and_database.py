
import jsonpickle

from engine.db.city import City
from engine.db.country import Country
from engine.db.date import Date
from engine.db.json_save_load.game_database import GameDatabase
from engine.db.json_save_load.game_save import GameSave
from engine.db.json_save_load.game_state import GameState
from engine.db.league import League
from engine.db.league_class import LeagueClass
from engine.db.person import Person
from engine.db.rider import Rider
from engine.db.stadium import Stadium
from engine.db.team import Team
from engine.db.track import Track


def init_db():
    global rider
    global rider2
    global person
    global person2
    global poland
    global league
    global ekstraliga
    global druga_liga
    global pierwsza_liga
    global torun
    global bydgoszcz
    global polonia
    global apator
    global stadium_polonia
    global stadium_apator
    global track_apator
    global track_polonia
    global game_database
    global game_state
    global game_save

    rider = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9)
    rider2 = Rider(9, 10, 11, 12, 13, 14, 15, 16, 17)

    date = Date(18, 3, 1985)
    person = Person("x", "y", rider, date, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    person2 = Person("x", "y", rider2, date, 9, 10, 11, 12, 13, 14, 15, 16, 17)

    poland = Country("Poland", 38000000, 30, 60)
    league = League(poland, "polish league", 99)
    ekstraliga = LeagueClass(league, "Polska Ekstraliga", 99, None, None)
    druga_liga = LeagueClass(league, "Polska 2 liga", 50, None, None)
    pierwsza_liga = LeagueClass(league, "Polska 1 liga", 70, ekstraliga, druga_liga)

    ekstraliga.previous_class = pierwsza_liga
    druga_liga.next_class = pierwsza_liga

    torun = City("Toruń", poland, 200000, 30, 85)
    bydgoszcz = City("Bydgoszcz", poland, 400000, 40, 55)

    polonia = Team(league, druga_liga, "Polonia", bydgoszcz, poland, 50, None)

    apator = Team(league, ekstraliga, "Apator", torun, poland, 99, [polonia, ])
    polonia.derby_teams = [apator, ]

    stadium_apator = Stadium("Motoarena", poland, apator, 20000, 99)
    stadium_polonia = Stadium("Stadion na ul. Sportowej", poland, polonia, 20000, 99)

    track_apator = Track(stadium_apator, 300, 30, 45)
    track_polonia = Track(stadium_polonia, 300, 30, 45)

    game_database = GameDatabase([torun, bydgoszcz], [poland, ], [league, ], [ekstraliga, pierwsza_liga, druga_liga],
                    [person, person2], [rider, rider2], [stadium_polonia, stadium_apator], [apator, polonia],
                    [track_polonia, track_apator])
    date = Date(1, 1, 2018)
    game_state = GameState(date)
    game_save = GameSave([torun, bydgoszcz], [poland, ], [league, ], [ekstraliga, pierwsza_liga, druga_liga],
                    [person, person2], [rider, rider2], [stadium_polonia, stadium_apator], [apator, polonia],
                    [track_polonia, track_apator], game_state)


def check_database_fields(game_database):
    assert game_database.cities == [torun, bydgoszcz]
    assert game_database.countries == [poland, ]
    assert game_database.leagues == [league, ]
    assert game_database.league_classes == [ekstraliga, pierwsza_liga, druga_liga]
    assert game_database.persons == [person, person2]
    assert game_database.riders == [rider, rider2]
    assert game_database.stadiums == [stadium_polonia, stadium_apator]
    assert game_database.teams == [apator, polonia]
    assert game_database.tracks == [track_polonia, track_apator]


def test_game_database_constructor():
    init_db()
    check_database_fields(game_database)


def test_game_save_constructor():
    init_db()
    check_database_fields(game_save)
    assert game_save.game_state == game_state


def check_database_equals(game_database, game_database2):
    assert game_database.cities == game_database2.cities
    assert game_database.countries == game_database2.countries
    assert game_database.leagues == game_database2.leagues
    assert game_database.league_classes == game_database2.league_classes
    assert game_database.persons == game_database2.persons
    assert game_database.riders == game_database2.riders
    assert game_database.stadiums == game_database2.stadiums
    assert game_database.teams == game_database2.teams
    assert game_database.tracks == game_database2.tracks


def test_game_database_save_and_load():
    init_db()
    game_database.save("file.dat")
    game_database2 = GameDatabase()
    game_database2 = game_database2.load("file.dat")
    check_database_equals(game_database, game_database2)


def test_game_save_save_and_load():
    init_db()
    game_save.save("file.dat")
    game_save2 = GameSave()
    game_save2 = game_save2.load("file.dat")

    check_database_equals(game_save, game_save2)
    assert game_save.game_state == game_save2.game_state
