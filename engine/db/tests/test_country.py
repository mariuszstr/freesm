from engine.db.country import Country


def test_constructor():
    country = Country("Poland", 38000000, 30, 60)
    assert country.name == "Poland"
    assert country.population == 38000000
    assert country.wealth == 30
    assert country.speedway_popularity == 60


def test_eq():
    country1 = Country("Poland", 100000, 30, 85)
    country2 = Country("Sweden", 100000, 30, 85)
    country3 = Country("Poland", 10000, 3, 8)

    assert country1 == country3  # not a bug, a feature - equals only city name
    assert country1 != country2
    assert country2 != country3
