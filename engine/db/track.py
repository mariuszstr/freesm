class Track:
    def __init__(self, stadium, length, first_corner_angle, second_corner_angle):
        self.stadium = stadium
        self.length = length
        self.first_corner_angle = first_corner_angle
        self.second_corner_angle = second_corner_angle

    def __eq__(self, other):
        return self.stadium.name == other.stadium.name and self.length == other.length