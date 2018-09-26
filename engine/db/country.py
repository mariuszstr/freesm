class Country:
    def __init__(self, name, population, wealth, speedway_popularity):
        self.name = name
        self.population = population
        self.wealth = wealth
        self.speedway_popularity = speedway_popularity

    def __eq__(self, other):
        return self.name == other.name
