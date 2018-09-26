class Stadium:
    def __init__(self, name, country, team, capacity, ability):
        self.name = name
        self.country = country
        self.team = team
        self.capacity = capacity
        self.ability = ability

    def __eq__(self, other):
        return self.name == other.name
