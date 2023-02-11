"""
Customize string representations of objects
    - Think of how this could be usefulness
"""


class someStats():
    def __init__(self):
        self.ppg = 23.7
        self.fg_pct = 40.1
        self.stl = 1.3

    # Use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "stats":
            return (self.ppg, self.fg_pct, self.stl)
        else:
            raise AttributeError

    # Use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "stats":
            self.ppg = val[0]
            self.fg_pct = val[1]
            self.stl = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ("ppg", "fg_pct", "stl", "stats", "anotherAttrHere")


def main():
    # Create an instance of someStats
    cls1 = someStats()

    # Print values of a computed attribute
    print(cls1.stats)

    # Set value of a computed attribute
    cls1.stats = (27.3, 42.7, 0.8)
    print(cls1.stats)

    # Access a regular attribute
    print(cls1.ppg)

    # List the available attributes
    print(dir(cls1))


if __name__ == "__main__":
    main()
