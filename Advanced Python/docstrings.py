"""
Demonstrate the use of function docstrings

Best Practices
    - Enclose docstrings in triple quotes
    - First line should be summary sentence of funtionality
    - Modules: List important classes, functions, exceptions
    - Classes: List important methods
    - Functions:
        + List parameters and explain each, one per line
        + If there's a return value, then list it; otherwise omit
        + If the function raises exceptions, mention those

https://www.python.org/dev/peps/pep-0257/
"""


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything special.

    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: the second argument. Defaults to None. Whatever makes you happy.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
