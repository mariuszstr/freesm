from engine.db.country import Country


def test_constructor():
    country = Country("Poland", 38000000, 30, 60)
    assert country.name == "Poland"
    assert country.population == 38000000
    assert country.wealth == 30
    assert country.speedway_popularity == 60
