class GameState:
    def __init__(self, date):
        self.date = date

    def __eq__(self, other):
        return self.date == other.date