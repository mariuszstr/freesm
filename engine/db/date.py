class Date:
    """Date representation.
    """
    def __init__(self, day, month, year):
        """Date constructor.

        Args:
            day (Int): day.
            month (Int): month.
            year (Int): year.
        """
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        """Compare Date object with other date.

        Args:
            other (Date): Other date.

        Returns:
            bool: The return value - if dates are equal.
        """
        return self.day == other.day and self.month == other.month and self.year == other.year
