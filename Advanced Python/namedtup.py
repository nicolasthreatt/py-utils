"""
Demonstrate the usage of namdtuple objects
    - Could be useful for graphing stats pts vs. ast, blk vs. d_fg_pct
"""

import collections


def main():
    # Create a Point namedtuple    (Name,  Stats)
    Point = collections.namedtuple("Point", "x y")

    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1, p2)
    print(p1.x, p1.y)

    # Use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
