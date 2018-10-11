from enum import Enum


class WeatherType(Enum):
    SUNNY = 1
    SUNNY_WITH_LITTLE_CLOUDS = 2
    CLOUDY = 2
    LITTLE_RAIN = 3
    RAIN = 4
    HUGE_RAIN = 5


class Weather:
    def __init__(self, weather_type):
        self.weather_type = weather_type
