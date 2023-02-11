"""
Advanced iteration functions in the itertools package
    - Maybe useful for parsing data

https://docs.python.org/library/itertools.html
"""

import itertools


def firstFgPctBad(x):
    return x < 40

def firstFgPctGood(x):
    return x > 40


def main():
    # cycle iterator can be used to cycle over a collection (infinite iterator)
    teams = ["Hornets", "Celtics", "Nets"]
    teams_cycled = itertools.cycle(teams)
    print(next(teams_cycled))
    print(next(teams_cycled))
    print(next(teams_cycled))
    print(next(teams_cycled))

    # use count to create a simple counter
    start = 100
    step  = 10
    count1 = itertools.count(start, step)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate creates an iterator that accumulates values
    stats = [10,20,30,40,50,40,30]
    acc_total = itertools.accumulate(stats, max)
    print(list(acc_total))
    acc_max = itertools.accumulate(stats, max)
    print(list(acc_max))
        
    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(firstFgPctGood, stats)))
    print(list(itertools.takewhile(firstFgPctBad, stats)))
    
    
if __name__ == "__main__":
    main()
    