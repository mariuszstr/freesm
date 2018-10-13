class Stadium:
    def __init__(self, name, country, team, capacity, ability, record_time=55.55, record_name="Anonymous"):
        self.name = name
        self.country = country
        self.team = team
        self.capacity = capacity
        self.ability = ability
        self.record_name = record_name
        self.record_time = record_time

    def __eq__(self, other):
        return self.name == other.name
