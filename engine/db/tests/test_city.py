from engine.db.city import City


def test_constructor():
    city = City("Toruń", None, 100000, 30, 85)
    assert city.name == "Toruń"
    assert city.country == None
    assert city.population == 100000
    assert city.wealth == 30
    assert city.speedway_popularity == 85
