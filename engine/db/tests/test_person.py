from engine.db.date import Date
from engine.db.person import Person
from engine.db.rider import Rider


def test_constructor():

    rider = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9)
    date = Date(18, 3, 1985)
    person = Person("Tony", "Rickardsson", rider, date, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert person.first_name == "Tony"
    assert person.last_name == "Rickardsson"
    assert person.rider == rider
    assert person.birth_date == date
    assert person.determination == 1
    assert person.loyalty == 2
    assert person.weight == 3
    assert person.height == 4
    assert person.iq == 5
    assert person.bravery == 6
    assert person.strength == 7
    assert person.condition == 8
    assert person.reflex == 9
