import numpy


class League:
    def __init__(self, country, name, classes):
        self.country = country
        self.name = name
        self.classes = classes

    @property
    def ability(self):
        return numpy.mean([league_class.ability for league_class in self.classes])

    def __eq__(self, other):
        return self.name == other.name
