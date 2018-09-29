class TrackPreparation:
    def __init__(self, track, water, grippiness):
        self.track = track
        self.water = water
        self.grippiness = grippiness  # 0 - hard, 50 - normal, 100 - grippy


    @property
    def hard_percent(self):
        return (100 - self.grippiness + 100 - self.water) / 2

    @property
    def grippy_percent(self):
        return (self.grippiness + 100 - self.water) / 2

    @property
    def normal_percent(self):
        return (100 - abs(50 - self.grippiness) + 100 - self.water) / 2

    @property
    def mudy_percent(self):
        return (self.grippiness + self.water) / 2

    @property
    def slick_percent(self):
        return (100 - abs(50 - self.grippiness) + self.water) / 2

    def __eq__(self, other):
        return self.track.stadium.name == other.track.stadium.name and self.water == other.water and \
               self.grippiness == other.grippiness
