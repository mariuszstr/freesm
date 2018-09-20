class City:
    def __init__(self, name, country, population, wealth, speedway_popularity):
        self.name = name
        self.country = country
        self.population = population
        self.wealth = wealth
        self.speedway_popularity = speedway_popularity

    def __eq__(self, other):
        return self.name == other.name