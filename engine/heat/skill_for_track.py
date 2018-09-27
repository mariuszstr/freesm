def get_skill_for_track(rider, track_preparation):
    top = max([track_preparation.hard_percent, track_preparation.grippy_percent,track_preparation.normal_percent,
               track_preparation.mudy_percent, track_preparation.slick_percent])
    if top == track_preparation.hard_percent:
        return rider.hard_skill
    elif top == track_preparation.grippy_percent:
        return rider.grippy_skill
    elif top == track_preparation.normal_percent:
        return rider.normal_skill
    elif top == track_preparation.mudy_percent:
        return rider.mud_skill
    else:
        return rider.slick_skill
