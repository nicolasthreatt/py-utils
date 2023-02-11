"""
Abstact Factory
	- Useful When
		+ The user expectation yields multiple, related objects
		+ Dynamic
"""


class Traditional:
    """A simple traditional stat class"""

    def stat(self):
        return "Pts"

    def __str__(self):
        return "Tradional"


class StatFactory:
    """Concrete Factory"""

    def get_category(self):
        """Returns a Tradional Object"""
        return Traditional()

    def get_stat(self):
        """Returns a Tradional Stat Object"""
        return "Plus Minus"


class StatStore:
    """ Player houses our Abstract Factory """

    def __init__(self, stat_factory=None):
        """ stat_factory is our Abstract Factory """
        self._stat_factory = stat_factory

    def show_stat(self):
        """ Utility method to display the details of the objects retured by the StatFactory """

        stat_category = self._stat_factory.get_category()
        stat_name = self._stat_factory.get_stat()

        print("Our current stat category is '{}'" .format(stat_category))
        print("The stat wanted is '{}'!".format(stat_name))
        print("Another stat wanted is '{}'".format(stat_category.stat()))


# Create a Concrete Factory
factory = StatFactory()

# Create a player housing our Abstract Factory
database = StatStore(factory)


# Invoke the utility method to show the details of our player
database.show_stat()
