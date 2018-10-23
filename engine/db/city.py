class City:
    def __init__(self, name, country, population, wealth, speedway_popularity):
        """Constructor for City class.

        Args:
            name (String): City name.
            country (Country): Country object.
            population (Int): City population.
            wealth( Int): Wealth of the city.
            speedway_popularity (Int): Speedway popularity in the city.
        """
        self.name = name
        self.country = country
        self.population = population
        self.wealth = wealth
        self.speedway_popularity = speedway_popularity

    def __eq__(self, other):
        """Compare two cieties.

        Args:
            other (City): City to compare with.

        Returns:
            bool: The return value - if cities are equal.

        """
        return self.name == other.name
