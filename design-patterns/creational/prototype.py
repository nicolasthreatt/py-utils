'''
Prototype
    - Why
        + Creating many identical objects individually: expensive
        + Cloning: an alternative
    - Scenario
        + Mass production
    - Solution
        + Create a prototypical instance first
        + Simply clone it whenever you need a replica
'''

import copy


class Prototype:

    def __init__(self):
        self._objects = dict()

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Player:
    def __init__(self):
        self.name = "Lebron James"
        self.jersey_num = 23
        self.team = "LAL"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.jersey_num, self.team)


# Instantiate Player()
player = Player()
prototype = Prototype()
prototype.register_object('GOAT', player)

# Clone player
player_copy = prototype.clone('GOAT')
print(player_copy)
