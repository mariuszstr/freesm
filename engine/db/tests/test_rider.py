from engine.db.rider import Rider


def test_constructor():
    rider = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert rider.start == 1
    assert rider.ride == 2
    assert rider.attack == 3
    assert rider.defence == 4
    assert rider.motorcycle_fit == 5
    assert rider.hard_skill == 6
    assert rider.slick_skill == 7
    assert rider.grippy_skill == 8
    assert rider.mud_skill == 9
    assert rider.normal_skill == 10


def test_eq():
    rider1 = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    rider2 = Rider(2, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    rider3 = Rider(2, 3, 3, 4, 5, 6, 7, 8, 9, 10)
    rider4 = Rider(1, 2, 4, 4, 5, 6, 7, 8, 9, 10)
    rider4 = Rider(1, 2, 4, 4, 5, 6, 7, 8, 9, 10)
    rider5 = Rider(1, 2, 3, 5, 5, 6, 7, 8, 9, 10)
    rider6 = Rider(1, 2, 3, 4, 6, 6, 7, 8, 9, 10)
    rider7 = Rider(1, 2, 3, 4, 5, 7, 7, 8, 9, 10)
    rider8 = Rider(1, 2, 3, 4, 5, 6, 8, 8, 9, 10)
    rider9 = Rider(1, 2, 3, 4, 5, 6, 7, 9, 9, 10)
    rider10 = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    rider11 = Rider(1, 2, 3, 4, 5, 6, 7, 8, 10, 10)

    assert rider1 != rider2
    assert rider1 != rider3
    assert rider1 != rider4
    assert rider1 != rider5
    assert rider1 != rider6
    assert rider1 != rider7
    assert rider1 != rider8
    assert rider1 != rider9
    assert rider1 == rider10
    assert rider1 != rider2
    assert rider1 != rider11
