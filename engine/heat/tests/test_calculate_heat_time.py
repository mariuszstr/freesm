from unittest import mock

from engine.db.city import City
from engine.db.country import Country
from engine.db.date import Date
from engine.db.person import Person
from engine.db.rider import Rider
from engine.db.stadium import Stadium
from engine.db.track import Track
from engine.db.track_preparation import TrackPreparation
from engine.heat.calculate_heat_time import calculate_heat_time


@mock.patch("engine.heat.calculate_heat_time.randint", return_value=50)
def test_calculate_heat_time(mock):
    people = [
        Person("Tony", "Rickardsson", Rider(start=99, ride=95, attack=90, defence=95, motorcycle_fit=99,
                                            hard_skill=99, slick_skill=85, grippy_skill=85, mud_skill=85,
                                            normal_skill=99), Date(17, 8, 970), determination=95, loyalty=30,
               weight=55, height=180, iq=120, bravery=90, strength=95, condition=95, reflex=99),
        Person("Tomasz", "Gollob", Rider(start=80, ride=99, attack=99, defence=94, motorcycle_fit=99,
                                         hard_skill=89, slick_skill=90, grippy_skill=90, mud_skill=99,
                                         normal_skill=99), Date(0,0,0), determination=99, loyalty=90,
               weight=55, height=100, iq=110, bravery=99, strength=99, condition=95, reflex=85),
        Person("Wiesław", "Jaguś", Rider(start=75, ride=92, attack=99, defence=87, motorcycle_fit=92,
                                         hard_skill=93, slick_skill=90, grippy_skill=90, mud_skill=90,
                                         normal_skill=92), Date(0, 0, 0), determination=99, loyalty=99,
               weight=50, height=170, iq=110, bravery=99, strength=99, condition=95, reflex=85),
        Person("Todd", "Whiltshide", Rider(start=75, ride=85, attack=90, defence=84, motorcycle_fit=85,
                                         hard_skill=85, slick_skill=85, grippy_skill=85, mud_skill=85,
                                         normal_skill=85), Date(0, 0, 0), determination=70, loyalty=40,
               weight=50, height=170, iq=110, bravery=90, strength=99, condition=95, reflex=80)

    ]
    country = Country("Poland", 35000000, 30, 85)
    city1 = City("Toruń", None,  200000, 70, 85)

    track_preparation = TrackPreparation(Track(Stadium("Motoarena", country, city1, capacity=10000, ability=95),
                                               length=318, first_corner_angle=30, second_corner_angle=45), water=0,
                                         grippiness=0)
    times = calculate_heat_time(track_preparation, people)
    assert times == [49.36, 48.21, 46.71, 44.4]
