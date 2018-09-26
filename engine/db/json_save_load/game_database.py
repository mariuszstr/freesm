import jsonpickle

class GameDatabase:
    def __init__(self, cities=None, countries=None, leagues=None, league_classes=None, persons=None, riders=None,
                 stadiums=None, teams=None, tracks=None):
        self.cities = cities
        self.countries = countries
        self.leagues = leagues
        self.league_classes = league_classes
        self.persons = persons
        self.riders = riders
        self.stadiums = stadiums
        self.teams = teams
        self.tracks = tracks

    def save(self, file):
        with open(file, 'w') as outfile:
            outfile.write(jsonpickle.encode(self,))

    @staticmethod
    def load(file):
        with open(file, 'r') as outfile:
            return jsonpickle.decode(outfile.read())
