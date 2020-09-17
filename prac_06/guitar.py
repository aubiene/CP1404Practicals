class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost
        self.current_year = 2020

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Gets guitar age based off current year"""
        age = self.current_year - self.year
        return age

    def is_vintage(self):
        """Checks to see if the guitar is vintage based off the guitars age"""
        if self.get_age() >= 50:
            return True
        else:
            return False
