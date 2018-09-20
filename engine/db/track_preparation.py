class TrackPreparation:
    def __init__(self, track, wetness, adhesion):
        self.track = track
        self.wetness = wetness
        self.adhesion = adhesion

    def __eq__(self, other):
        return self.track.stadium.name == other.track.stadium.name and self.wetness == other.wetness and \
               self.adhesion == other.adhesion