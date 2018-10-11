from enum import Enum
from random import random


class WeatherType(Enum):
    SUNNY = 1
    SUNNY_WITH_LITTLE_CLOUDS = 2
    CLOUDY = 3
    LITTLE_RAIN = 4
    RAIN = 5
    HUGE_RAIN = 6


class Weather:
    def __init__(self, weather_type):
        self.weather_type = weather_type


def generate_weather_type():
    return random.choices([WeatherType.SUNNY] * 21 + [WeatherType.SUNNY_WITH_LITTLE_CLOUDS] * 60 +
                          [WeatherType.CLOUDY] * 137 + [WeatherType.LITTLE_RAIN] * 63 + [WeatherType.RAIN] *
                          60 + [WeatherType.HUGE_RAIN] * 23)
