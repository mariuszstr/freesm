from engine.db.date import Date


def test_constructor():
    date = Date(18, 3, 1985)
    assert date.day == 18
    assert date.month == 3
    assert date.year == 1985