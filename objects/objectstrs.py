"""
Customize string representations of objects
    - Could be useful for logs when debugging
"""


class Player():
    def __init__(self):
        self.fname = "Lebron"
        self.lname = "James"
        self.jersey_num = 23

    # Use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Player Class - fname:{0}, lname:{1}, jersey_num{2}>".format(self.fname, self.lname, self.jersey_num)

    # Use __str__ for a more human-readable string
    def __str__(self):
        return "Player ({0} {1} is {2})".format(self.fname, self.lname, self.jersey_num)


def main():
    player = Player()

    # Use different Python functions to convert it to a string
    print(repr(player))
    print(str(player))
    print("Formatted: {0}".format(player))


if __name__ == "__main__":
    main()
