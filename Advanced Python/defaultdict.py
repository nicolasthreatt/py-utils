"""
Demonstrate the usage of defaultdict objects
    - Could be useful to get all stats from different types
        + i.e. (Shooting AND Opponenet Shooting)
"""

from collections import defaultdict


def main():
    # Define a list of items that we want to count
    passers = ['Lebron James', 'Ricky Rubio', 'Luka Doncic', 'Ben Simmons',
               'Lebron James', 'Nikola Jokic', 'Ben Simmons', 'Ben Simmons']

    # Use a dictionary to count each element (See the difference)
    passerCounter = defaultdict(int)
    # passerCounter = defaultdict(lambda: 100)

    # Count the elements in the list
    for passer in passers:
        passerCounter[passer] += 1

    # Print the result
    for (k, v) in passerCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
