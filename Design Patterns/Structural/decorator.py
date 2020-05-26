'''
Decorator
	- Problem
		+ New features to an existing object, dynamically, without using subclasses
	- Useful When:
		+ Trying to add format various stats for analyizing
'''

from functools import wraps


def make_percentage(function):
    """Defines the decorator"""

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator():
        # Grab the return value of the function being decorated
        ret = function()

        # Add new functionality to the function being decorated
        return str(ret) + '%'

    return decorator


# Apply the decorator here!
@make_percentage
def pts():
    """Original function! """

    pts = 25.7
    return pts


# Check the result of decorating
print(pts())

# Check if the function name is still the same name of the function being decorated
print(pts.__name__)

# Check if the docstring is still the same as that of the function being decorated
print(pts.__doc__)
