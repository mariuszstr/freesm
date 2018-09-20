class Stadium:
    def __init__(self, name, country, team, sits, ability):
        self.name = name
        self.country = country
        self.team = team
        self.sits = sits
        self.ability = ability

    def __eq__(self, other):
        return self.name == other.name