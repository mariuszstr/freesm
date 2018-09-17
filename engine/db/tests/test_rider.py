from engine.db.rider import Rider


def test_constructor():
    rider = Rider(1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert rider.start == 1
    assert rider.ride == 2
    assert rider.attack == 3
    assert rider.defence == 4
    assert rider.motorcycle_fit == 5
    assert rider.stiff_track_skill == 6
    assert rider.miry_track_skill == 7
    assert rider.wet_track_skill == 8
    assert rider.slippy_track_skill == 9
