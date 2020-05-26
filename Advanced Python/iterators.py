"""
Use iterator functions like enumerate, zip, iter, next
    - Could be useful when comparing stats
"""


def main():
    # define a list of days in English and French
    stats1 = [0, 1, 2, 3, 4, 5, 6]
    stats2 = [28.3, 15.7, 0, 18.7, 9.8, 11.2, 6]

    # use iter to create an iterator over a collection
    i = iter(stats1)
    print(next(i))  # 0
    print(next(i))  # 1
    print(next(i))  # 2

    # use regular interation over the stats1
    for m in range(len(stats1)):
        print(m+1, stats1[m])

    # using enumerate reduces code and provides a counter (Preferred Way)
    for i, m in enumerate(stats1, start=1):
        print(i, m)

    # use zip to combine sequences (Produces a tuple)
    for m in zip(stats1, stats2):
        print(m)

    for i, m in enumerate(zip(stats1, stats2), start=1):
        print(i, m[0], "=", m[1], "when comparing stats")


if __name__ == "__main__":
    main()
