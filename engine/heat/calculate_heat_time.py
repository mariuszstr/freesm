from random import randint

from engine.heat.skill_for_track import get_skill_for_track


def calculate_heat_time(track_preparation, people):
    skills_for_track = [get_skill_for_track(person.rider, track_preparation) for person in people]
    max_time = track_preparation.track.stadium.record_time + track_preparation.track.stadium.record_time * 0.1
    # TODO: calculate max time less if track conditions are worse than optimal.

    percents = [(person.rider.start + skills_for_track[counter] + person.rider.ride + person.rider.attack +
                person.rider.defence + person.rider.motorcycle_fit + randint(1, 100) * 3) / 9
                for counter, person in enumerate(people)]
    return [round(max_time * 0.01 * percent, 2) for percent in percents]
