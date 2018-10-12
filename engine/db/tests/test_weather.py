from unittest import mock

from engine.db.weather import Weather, generate_temperature, generate_weather_type, WeatherType, generate_weather


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


@mock.patch("engine.db.weather.random")
def test_generate_weather_type(mock):
    mock.choices.return_value = 1
    assert generate_weather_type(10) == 1
    mock.choices.assert_called_with([WeatherType.SUNNY] * 21 + [WeatherType.SUNNY_WITH_LITTLE_CLOUDS] * 60 +
                          [WeatherType.CLOUDY] * 137 + [WeatherType.LITTLE_RAIN] * 63 + [WeatherType.RAIN] *
                          60 + [WeatherType.HUGE_RAIN] * 23)


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_little_rain_temperature_positive(mock):
    mock.choices.return_value = WeatherType.LITTLE_RAIN
    assert generate_weather_type(10) == WeatherType.LITTLE_RAIN


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_little_rain_temperature_1_celcius(mock):
    mock.choices.return_value = WeatherType.LITTLE_RAIN
    assert generate_weather_type(1) == WeatherType.LITTLE_SNOW


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_little_rain_temperature_negative_celcius(mock):
    mock.choices.return_value = WeatherType.LITTLE_RAIN
    assert generate_weather_type(-1) == WeatherType.LITTLE_SNOW


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_rain_temperature_positive(mock):
    mock.choices.return_value = WeatherType.RAIN
    assert generate_weather_type(3) == WeatherType.RAIN


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_rain_temperature_1_celcius(mock):
    mock.choices.return_value = WeatherType.RAIN
    assert generate_weather_type(1) == WeatherType.SNOW


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_rain_temperature_negative_celcius(mock):
    mock.choices.return_value = WeatherType.RAIN
    assert generate_weather_type(-5) == WeatherType.SNOW


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_huge_rain_temperature_positive(mock):
    mock.choices.return_value = WeatherType.HUGE_RAIN
    assert generate_weather_type(2) == WeatherType.HUGE_RAIN


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_huge_rain_temperature_1_celcius(mock):
    mock.choices.return_value = WeatherType.HUGE_RAIN
    assert generate_weather_type(1) == WeatherType.HUGE_SNOW


@mock.patch("engine.db.weather.random")
def test_generate_weather_type_huge_rain_temperature_negative_celcius(mock):
    mock.choices.return_value = WeatherType.HUGE_RAIN
    assert generate_weather_type(-55) == WeatherType.HUGE_SNOW


@mock.patch("engine.db.weather.generate_weather_type")
@mock.patch("engine.db.weather.generate_temperature")
def test_generate_weather(generate_temperature_mock, generate_weather_type_mock):
    temperature = 10
    month = 5
    generate_temperature_mock.return_value = temperature
    generate_weather_type_mock.return_value = WeatherType.CLOUDY
    weather = generate_weather(month)
    assert weather.temperature == temperature
    assert weather.weather_type == WeatherType.CLOUDY
    generate_temperature_mock.assert_called_with(month)
    generate_weather_type_mock.assert_called_with(temperature)
