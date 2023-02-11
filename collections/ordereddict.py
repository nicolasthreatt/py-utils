"""
Demonstrate the usage of OrderedDict objects
    - Could be useful when trying to get stats from a database then sort
"""

from collections import OrderedDict


def main():
    # List of sport teams with wins and losses
    sportTeams = [("Thunder", (18, 12)), ("Bucks",    (24, 6)), 
                  ("Rockets", (20, 10)), ("Celtics",  (22, 8)),
                  ("Kings",   (15, 15)), ("Clippers", (20, 10)), 
                  ("Nets",    (16, 14)), ("Lakers",   (25, 5))]

    # Sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # Create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # Test for equality
    ordered_dict = OrderedDict({"a": 1, "b": 2, "c": 3})
    regular_dict =             {"c": 3, "b": 2, "a": 1}
    print("Equality test: ", ordered_dict == regular_dict)


if __name__ == "__main__":
    main()
