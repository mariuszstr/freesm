from engine.db.date import Date


def test_constructor():
    date = Date(18, 3, 1985)
    assert date.day == 18
    assert date.month == 3
    assert date.year == 1985


def test_eq():
    date1 = Date(1, 1, 2018)
    date2 = Date(2, 1, 2018)
    date3 = Date(3, 1, 2018)
    date4 = Date(1, 1, 2018)
    date5 = Date(2, 1, 2018)

    assert date1 != date2
    assert date1 != date3
    assert date1 == date4
    assert date1 != date5
    assert date2 != date3
    assert date2 != date4
    assert date2 == date5
    assert date4 != date5
