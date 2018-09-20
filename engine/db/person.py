class Person:
    def __init__(self, first_name, last_name, rider, birth_date, determination, loyalty,
                 weight, height, iq, bravery, strength, condition, reflex):
        self.first_name = first_name
        self.last_name = last_name
        self.rider = rider
        self.birth_date = birth_date
        self.determination = determination
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
        return self.first_name == other.first_name and self.last_name == other.last_name and \
               self.birth_date.day == other.birth_date.day and self.birth_date.month == other.birth_date.month and \
               self.birth_date.year == other.birth_date.year
