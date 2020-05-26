"""
Use transform functions like sorted, filter, map
    - Could be useful for comparing stats
"""


def filterFunc(x):
    if x % 2 == 0:  # Check to see if number is even
        return False
    return True


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 45):
        return "A"
    elif (x >= 40 and x < 45):
        return "B"
    elif (x >= 35 and x < 40):
        return "C"
    elif (x >= 30 and x < 35):
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    shootingPct = (40, 49, 55, 38, 29, 35, 72, 37)

    # use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # use map to create a new sequence of values
    # Could be use to calculate formulas
    squares = list(map(squareFunc, nums))
    print(squares)

    # use sorted and map to change numbers to shootingPct
    # Could be use to map stats to a player
    shootingPct = sorted(shootingPct)
    letters     = list(map(toGrade, shootingPct))
    print(letters)


if __name__ == "__main__":
    main()
