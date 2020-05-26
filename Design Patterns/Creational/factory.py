'''
Factory
    - Encapsulates object creation
        + Factory is an object specialized in creating other objects
    - Useful When:
        + Uncertainies in types of objects
        + Decisions to be made at runtime regarding what classes to use
        + Dynamically add different stats objects to a player
'''


class Traditional:
    """A simple traditional stat class"""

    def __init__(self, name):
        self._name = name

    def stat(self):
        return self._name


class Advanced:
    """A simple advanced stat class"""

    def __init__(self, name):
        self._name = name

    def stat(self):
        return self._name


def get_stat(stat='traditional'):
    """The factory method"""

    stats = dict(traditional=Traditional("Traditional"),
                 advanced=Advanced("Advanced"))

    return stats[stat]


# Test Output
traditional = get_stat("traditional")
print(traditional.stat())

advanced = get_stat("advanced")
print(advanced.stat())
