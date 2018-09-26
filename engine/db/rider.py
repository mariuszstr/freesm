class Rider:
    def __init__(self, start, ride, attack, defence, motorcycle_fit, hard_skill, slick_skill,
                 grippy_skill, mud_skill, normal_skill):
        # tor twardy + woda/opad = sliski
        # hard + water/rain = slick
        # przyczepny + woda = błoto
        # grippy + water = mud
        # normalny + woda = losowo przyczepny lub śliski
        # normal + water = random grippy or slick
        self.start = start
        self.ride = ride
        self.attack = attack
        self.defence = defence
        self.motorcycle_fit = motorcycle_fit
        self.hard_skill = hard_skill
        self.slick_skill = slick_skill
        self.grippy_skill = grippy_skill
        self.mud_skill = mud_skill
        self.normal_skill = normal_skill

    def __eq__(self, other):
        return self.start == other.start and self.ride == other.ride and self.attack == other.attack and \
               self.defence == other.defence and self.motorcycle_fit == other.motorcycle_fit and \
               self. hard_skill == other.hard_skill and self.slick_skill == other.slick_skill \
               and self.grippy_skill == other.grippy_skill and \
               self.mud_skill == other.mud_skill and self.normal_skill == other.normal_skill
