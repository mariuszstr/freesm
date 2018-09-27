class TrackPreparation:
    def __init__(self, track, water, grippness):
        self.track = track
        self.water = water
        self.grippness = grippness  # 0 - hard, 50 - normal, 100 - grippy

    def __eq__(self, other):
        return self.track.stadium.name == other.track.stadium.name and self.water == other.water and \
               self.grippness == other.grippness
