from engine.db.weather import Weather


def test_weather_constructor():
    weather1 = Weather(1, 15)
    assert weather1.weather_type == 1
    assert weather1.temperature == 15
    weather2 = Weather(3, 5)
    assert weather2.weather_type == 3
    assert weather2.temperature == 5
