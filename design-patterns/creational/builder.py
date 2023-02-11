'''
Builder
    - Excess number of constructors
    - Scenario
        + Build a car in parts, then assemble them after
            -> jersey_num
            -> Engine
            -> etc.
    - Solution
        + Director
            -> In charge of building product using the builder object
        + Abstract Builder
            -> Requires all neccessary interfaces when building an object
        + Concrete Builder
            -> Implements the interfaces
        + Product 
            -> Object being built
'''


class Director():
    """Director"""

    def __init__(self, builder):
        self._builder = builder

    def construct_player(self):
        self._builder.create_new_player()
        self._builder.add_name()
        self._builder.add_jersey_num()

    def get_player(self):
        return self._builder.player


class Builder():
    """Abstract Builder"""

    def __init__(self):
        self.player = None

    def create_new_player(self):
        self.player = Player()


class PlayerBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """

    def add_name(self):
        self.player.name = "Lebron James"

    def add_jersey_num(self):
        self.player.jersey_num = 23


class Player():
    """Product"""

    def __init__(self):
        self.name = None
        self.jersey_num = None

    def __str__(self):
        return '{} | {}'.format(self.name, self.jersey_num)


# Build a Player
builder = PlayerBuilder()
director = Director(builder)
director.construct_player()
player = director.get_player()
print(player)
