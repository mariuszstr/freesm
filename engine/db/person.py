class Person:
    """Person.

    """
    def __init__(self, first_name, last_name, rider, birth_date, determination, loyalty,
                 weight, height, iq, bravery, strength, condition, reflex):
        """Person's constructor.

        Args:
            first_name (String): First name.
            last_name (String): Last name.
            rider (Rider): Skills for ride.
            birth_date (Date): Birth's date.
            determination (Int): Determination (1-100).
            loyalty (Int): Loyalt (1-100)
            weight (Int): Weight.
            height (Int): Height
            iq (Int): Iq.
            bravery (Int): Bravery (1-100)
            strength (Int): Strength (1-100)
            condition (Int): Condition (1-100)
            reflex (Int): Reflex (1-100)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.rider = rider
        self.birth_date = birth_date
        self.determination = determination
        self.loyalty = loyalty
        self.weight = weight
        self.height = height
        self.iq = iq
        self.bravery = bravery
        self.strength = strength
        self.condition = condition
        self.reflex = reflex

    def __eq__(self, other):
        """Equals two persons.

        Args:
            other (Person): other Person object.

        Returns:
            bool: The return value - if persons are equal.

        """
        return self.first_name == other.first_name and self.last_name == other.last_name\
               and self.birth_date.day == other.birth_date.day and self.birth_date.month == other.birth_date.month and \
               self.birth_date.year == other.birth_date.year
