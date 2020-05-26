'''
Adapter
	- Converts the interface of a class into another one that a client is expecting
	- Problem
		+ Interfaces are incompatible between a client and a server
	- Useful When
		+ Trying to get various stats from different stat object classes
        + Application trying to access different databases
    - Notes
        + If consistently used, the adapter pattern promotes maintainability
'''


class Traditional:
    """Traditional Table"""

    def __init__(self):
        self.name = "Traditional"

    def tradional_stat(self):
        return "Plus-Minus"


class Advanced:
    """Advanced Table"""

    def __init__(self):
        self.name = "Advanced"

    def advanced_stat(self):
        return "Net Rating"


class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object

        # Add a new dictionary item that establishes the mapping between the generic method name: stat() and the concrete method
        # For example, stat() will be translated to tradional_stat() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)


# List to store stat objects
objects = []

# Create a Traditional object
traditional = Traditional()

# Create an Advanced object
advanced = Advanced()

# Append the objects to the objects list
objects.append(Adapter(traditional, stat=traditional.tradional_stat))
objects.append(Adapter(advanced, stat=advanced.advanced_stat))


for obj in objects:
    print("{} current stat is '{}'\n".format(obj.name, obj.stat()))
