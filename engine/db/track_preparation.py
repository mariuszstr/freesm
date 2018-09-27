class TrackPreparation:
    def __init__(self, track, water, grippness):
        self.track = track
        self.water = water
        self.grippness = grippness  # 0 - hard, 50 - normal, 100 - grippy


    @property
    def hard_percent(self):
        return (100 - self.grippness + 100 - self.water) / 2

    @property
    def grippy_percent(self):
        return (self.grippness + 100 - self.water) / 2

    @property
    def normal_percent(self):
        return (100 - abs(50 - self.grippness) + 100 - self.water) / 2

    @property
    def mudy_percent(self):
        return (self.grippness + self.water) / 2

    @property
    def slick_percent(self):
        return (100 - abs(50 - self.grippness) + self.water) / 2

    def __eq__(self, other):
        return self.track.stadium.name == other.track.stadium.name and self.water == other.water and \
               self.grippness == other.grippness
