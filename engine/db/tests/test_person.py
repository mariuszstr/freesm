from engine.db.date import Date
from engine.db.person import Person
from engine.db.rider import Rider


def test_constructor():

    rider = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
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


def test_eq():
    rider1 = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    rider2 = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    date1 = Date(18, 3, 1985)
    date2 = Date(18, 4, 1985)

    person1 = Person("Tony", "Rickardsson", rider1, date1, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    person2 = Person("Tony2", "Rickardsson", rider1, date1, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    person3 = Person("Tony", "Rickardsson2", rider1, date1, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    person4 = Person("Tony", "Rickardsson", rider2, date1, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    person5 = Person("Tony", "Rickardsson", rider1, date2, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    person6 = Person("Tony", "Rickardsson", rider1, date1, 2, 2, 3, 4, 5, 6, 7, 8, 9)
    person7 = Person("Tony", "Rickardsson", rider1, date1, 1, 3, 3, 4, 5, 6, 7, 8, 9)
    # NOTE: Compare only names and date of birth.
    assert person1 != person2
    assert person1 != person3
    assert person1 == person4
    assert person1 != person5
    assert person1 == person6
    assert person1 == person7
    assert person4 != person3
    assert person4 != person5
    assert person4 == person6
    assert person4 == person7
    assert person5 != person6
    assert person5 != person7

