class Rider:
    """Rider's attributes for person.

    """
    def __init__(self, start, ride, attack, defence, motorcycle_fit, hard_skill, slick_skill,
                 grippy_skill, mud_skill, normal_skill):
        """Rider's constructor

        Args:
            start (Int): Start (1-100).
            ride (Int): Ride (1-100).
            attack (Int): Attack (1-100).
            defence (Int): Defence (1-100).
            motorcycle_fit (Int): Fit of motorcycle (1-100).
            hard_skill (Int): Ride in hard tracks (1-100).
            slick_skill (Int): Ride in slick tracks (1-100).
            grippy_skill (Int): Ride in grippy tracks (1-100).
            mud_skill (Int): Ride in mud tracks (1-100).
            normal_skill (Int): Ride in normal tracks (1-100)
        """
        # tor twardy + woda/opad = sliski
        # hard + water/rain = slick
        # przyczepny + woda = błoto
        # grippy + water = mud
        # normalny + woda = losowo przyczepny lub śliski
        # normal + water = random grippy or slick
        # now implemented only as slick
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
        """Equals rider with other.

        Args:
            other: Other rider's object.

        Returns:
            bool: The return value - if riders are equal.
        """
        return self.start == other.start and self.ride == other.ride and self.attack == other.attack and \
               self.defence == other.defence and self.motorcycle_fit == other.motorcycle_fit and \
               self. hard_skill == other.hard_skill and self.slick_skill == other.slick_skill \
               and self.grippy_skill == other.grippy_skill and \
               self.mud_skill == other.mud_skill and self.normal_skill == other.normal_skill
