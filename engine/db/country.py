class Country:
    """Country.
    """
    def __init__(self, name, population, wealth, speedway_popularity):
        """Constructor for Country class.

        Args:
            name (String): Country name.
            population (Int): Country population.
            wealth (Int): Country wealth.
            speedway_popularity (Int): Speedway popularity in the country.
        """
        self.name = name
        self.population = population
        self.wealth = wealth
        self.speedway_popularity = speedway_popularity

    def __eq__(self, other):
        """Equals two Country objects.

        Args:
            other(Country): Other country.

        Returns:
            bool: The return value - if countries are equal.


        """
        return self.name == other.name
