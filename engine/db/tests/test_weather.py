from unittest import mock

from engine.db.weather import Weather, generate_temperature


def test_weather_constructor():
    weather1 = Weather(1, 15)
    assert weather1.weather_type == 1
    assert weather1.temperature == 15
    weather2 = Weather(3, 5)
    assert weather2.weather_type == 3
    assert weather2.temperature == 5


def randint(from_, to):
    return from_


@mock.patch("engine.db.weather.randint", side_effect=randint)
def test_generate_temperature_march(mock):
    temperature = generate_temperature(3)
    assert temperature == -5
    mock.assert_called_with(-5, 15)


@mock.patch("engine.db.weather.randint", side_effect=randint)
def test_generate_temperature_april(mock):
    temperature = generate_temperature(4)
    assert temperature == 3
    mock.assert_called_with(3, 22)
