class League:
    def __init__(self, country, name, ability):
        self.country = country
        self.name = name
        self.ability = ability

    def __eq__(self, other):
        return self.name == other.name