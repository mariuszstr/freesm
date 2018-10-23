import numpy


class League:
    """Country league.
    """
    def __init__(self, country, name, classes):
        """Constructor for league.

        Args:
            country (Country): League's country.
            name: (String): League's name (for example. "polish league"
            classes (LeagueClass[]): list of league classes (for example PGE Ekstraliga, NICE 1 liga etc.
        """
        self.country = country
        self.name = name
        self.classes = classes

    @property
    def ability(self):
        """Calculate league ability using league's classes abilities.

        Returns:
             Int: League ability.
        """
        return numpy.mean([league_class.ability for league_class in self.classes])

    def __eq__(self, other):
        """Equals League object with other.

        Args:
            other (League): Other league.

        Returns:
            bool: The return value - if leagues are equal.

        """
        return self.name == other.name
