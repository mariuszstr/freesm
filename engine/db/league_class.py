class LeagueClass:
    """League class - for example "PGE Ekstraliga".

    """
    def __init__(self, league, name, ability, next_class, previous_class):
        """Constructor for league class object.

        Args:
            league (League): country league for league class.
            name (String): League class name (for example, "PGE Ekstraliga")
            ability (Int): League ability.
            next_class (LeagueClass): LeagueClass object for promotion teams.
            previous_class(LeagueClass): LeagueClass object for degradation.
        """
        self.league = league
        self.name = name
        self.ability = ability
        self.next_class = next_class
        self.previous_class = previous_class

    def __eq__(self, other):
        """Check if two LeagueClass objects are equals.

        Args:
            other (LeagueClass): other league class to compare.

        Returns:
            bool: The return value - if league classes are equal.

        """
        return self.name == other.name
