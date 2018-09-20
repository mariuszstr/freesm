from engine.db.city import City


def test_constructor():
    city = City("Toruń", None, 100000, 30, 85)
    assert city.name == "Toruń"
    assert city.country == None
    assert city.population == 100000
    assert city.wealth == 30
    assert city.speedway_popularity == 85


def test_eq():
    city1 = City("Toruń", None, 100000, 30, 85)
    city2 = City("Bydgoszcz", None, 100000, 30, 85)
    city3 = City("Toruń", None, 10000, 3, 8)

    assert city1 == city3  # not a bug, a feature - equals only city name
    assert city1 != city2
    assert city2 != city3
