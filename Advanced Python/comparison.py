"""
Use special methods to compare objects to each other
    - Useful for comparing and soritng stats
"""


class Player():
    def __init__(self, fname, lname, ppg, experience):
        self.fname = fname
        self.lname = lname
        self.ppg = ppg
        self.seasons = experience   

    # implement comparison functions by player ppg
    def __ge__(self, other):
        if self.ppg == other.ppg:
            return self.seasons >= other.seasons
        return self.ppg >= other.ppg

    def __gt__(self, other):
        if self.ppg == other.ppg:
            return self.seasons > other.seasons
        return self.ppg > other.ppg

    def __lt__(self, other):
        if self.ppg == other.ppg:
            return self.seasons < other.seasons
        return self.ppg < other.ppg

    def __le__(self, other):
        if self.ppg == other.ppg:
            return self.seasons <= other.seasons
        return self.ppg <= other.ppg

    def __eq__(self, other):
        return self.ppg == other.ppg


def main():
    players = []
    players.append(Player("Elena", "Delle Donne", 19.5, 6))
    players.append(Player("Lebron", "James", 25.7, 16))
    players.append(Player("Russell", "Westbrook", 27.5, 11))
    players.append(Player("Ja", "Morant", 17.6, 1))
    players.append(Player("Kevin", "Durant", 26.0, 12))

    # Who's more experiened?
    print(bool(players[0] > players[2]))
    print(bool(players[4] < players[3]))

    # Sort the items
    sorted_players = sorted(players)
    for player in sorted_players:
        print(player.lname)


if __name__ == "__main__":
    main()
