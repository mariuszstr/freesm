class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year
