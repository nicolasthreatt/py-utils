'''
Visitor
	- Allows adding new features to an existing class hierarchy without changing it
	- Problem:
		+ Add new operations to existing classes dynamically
'''


class Player(object):
    def accept(self, table):
        """Interface to accept a table"""
        table.show(self)

    def add_traditional(self, tradional_stat):
        # Note that we now have a reference to the Traditiona stat object in the player object
        print(self, "current table is", tradional_stat)

    def add_advanced(self, advanced_stat):
        # Note that we now have a reference to the Advcanced Stat object in the player object
        print(self, "current table is", advanced_stat)

    def __str__(self):
        """Simply return the class name when the Table object is printed"""
        return self.__class__.__name__


class Table(object):
    """Abstract table"""

    def __str__(self):
        """Simply return the class name when the Table object is printed"""
        return self.__class__.__name__


class Traditional(Table):  # Inherits from the parent class, Table
    """Concrete table: Traditional table"""

    def show(self, player):
        # Note that the table now has a reference to the table object
        player.add_traditional(self)


class Advanced(Table):  # Inherits from the parent class, Table
    """Concrete table: Advanced Table"""

    def show(self, player):
        # Note that the table now has a reference to the player object
        player.add_advanced(self)


# Create an Traditional Table
t = Traditional()

# Create an Advanced Table
a = Advanced()

# Create a Player
player = Player()

# Let the player accept the Traditional table and update on the player by invoking the show() method
player.accept(t)

# Let the player accept the Advanced table and update on the player by invoking the show() method
player.accept(a)
