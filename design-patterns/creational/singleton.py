'''
Singleton
    - Useful when:
        + Only one instance
        + Creating a global variable in an object-oriented way
    - Scenario:
        + An information cache shared by multipe objects
        + Add multiple stat objects to a player(s)
    - Borg:
        + https://www.geeksforgeeks.org/singleton-method-python-design-patterns/ 
'''


class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    # This essenstially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_data.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_data)


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


# Let's create a singleton object and add our first acronym
x = Singleton(Traditional=Traditional("Traditional Stats"))
# Print the object
print(x)

# Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.
y = Singleton(Advanced=Advanced("Advanced Stats"))
# Print the object
print(y)
