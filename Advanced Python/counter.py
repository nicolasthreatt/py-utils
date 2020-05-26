"""
Demonstrate the usage of Counter objects
    - Could be useful when trying to count players to see who is most frequent
      in various statistical categories (Leading scorers, leading passers, etc)
"""

from collections import Counter


def main():
    # list of students in class 1
    statclass1 = ["Kobe", "Lebron", "Steph", "KD", "Penny", "Giannis"
                  "Kawhi", "Lebron", "Luka", "Kareem", "Magic", "Michael"]

    # list of students in class 2
    statclass2 = ["Shaq", "Rodman", "KG", "Dirk", "Michael",
                  "Candace", "Sue", "Lebron", "Aja", "Zion", "Ja", "Westbrook"]

    # Create a Counter for statclass1 and statclass2
    c1 = Counter(statclass1)
    c2 = Counter(statclass2)

    # How many players in statclass1 named Lebron?
    print(c1["Lebron"])

    # How many players are in statclass1?
    print(sum(c1.values()), "players in stat class 1")

    # Combine the two classes
    c1.update(statclass2)
    print(sum(c1.values()), "players in stat class 1 and 2")

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(statclass2)
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()
