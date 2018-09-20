class Rider:
    def __init__(self, start, ride, attack, defence, motocycle_fit, stiff_track_skill, miry_track_skill,
                 wwt_track_skill, slippy_track_skill):
        self.start = start
        self.ride = ride
        self.attack = attack
        self.defence = defence
        self.motorcycle_fit = motocycle_fit
        self.stiff_track_skill = stiff_track_skill
        self.miry_track_skill = miry_track_skill
        self.wet_track_skill = wwt_track_skill
        self.slippy_track_skill = slippy_track_skill

    def __eq__(self, other):
        return self.start == other.start and self.ride == other.ride and self.attack == other.attack and \
               self.defence == other.defence and self.motorcycle_fit == other.motorcycle_fit and \
               self. stiff_track_skill == other.stiff_track_skill and self.miry_track_skill == other.miry_track_skill \
               and self.wet_track_skill == other.wet_track_skill and \
               self.slippy_track_skill == other.slippy_track_skill
