"""
Demonstrate how to use dictionary comprehensions
    - Coud be useful when analyzing stats
"""


def main():
    # Define a list of field goals made
    fg_m = [0, 6, 12, 15]
    fg_a = 18

    # Use a comprehension to build a dictionary
    fgPctDict = {fg: fg/fg_a for fg in fg_m if fg < 100}
    print(fgPctDict)

    # Merge two dictionaries with a comprehension
    west = {"Lebron James": 23, "Anthony Davis": 3,
            "Luka Doncic": 77, "James Harden": 13, "Kawhi Leonard": 2}
    east = {"Giannis Antetokounmpo": 34, "Joel Embiid": 21,
            "Pascal Siakam": 43, "Kemba Walker": 8, "Trae Young": 11}
    allstars = {k: v for team in (east, west) for k, v in team.items()}
    print(allstars)


if __name__ == "__main__":
    main()
