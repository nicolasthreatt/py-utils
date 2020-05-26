"""
Demonstrate the use of variable argument lists
    - Could be useful to help print stats
"""


# define a function that takes variable arguments
def printStats(statName, *args):
    print('Stat: ', statName)
    for arg in args:
        print(arg)
    print()


def main():
    # pass different arguments
    printStats('PPG', 5, 10, 15, 20)
    printStats('BLK', 1, 2, 3)

    # pass an existing list
    myNums = [5, 10, 15, 20]
    printStats('PPG', *myNums)


if __name__ == "__main__":
    main()
