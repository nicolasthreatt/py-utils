"""
Define enumerations using the Enum base class
    - Many useful cases
"""

from enum import Enum, unique, auto


@unique
class Stats(Enum):
    PPG       = 1
    FG_PCT    = 2
    REB       = 3
    FOULS     = 4
    PLUSMINUS = auto()


def main():
    # Enums have human-readable values and types
    print(Stats.PPG)
    print(type(Stats.PPG))
    print(repr(Stats.PPG))

    # Enums have name and value properties
    print(Stats.PPG.name, Stats.PPG.value)

    # Print the auto-generated value
    print(Stats.PLUSMINUS.value)

    # Enums are hashable - can be used as keys
    myStats = {}
    myStats[Stats.PPG] = 48.7
    print(myStats[Stats.PPG])


if __name__ == "__main__":
    main()
