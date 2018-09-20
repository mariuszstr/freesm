class Team:
    def __init__(self, league, league_class, name, city, country, ability, derby_teams):
        self.league = league
        self.league_class = league_class
        self.name = name
        self.city = city
        self.country = country
        self.ability = ability
        self.derby_teams = derby_teams

    def __eq__(self, other):
        return self.name == other.name