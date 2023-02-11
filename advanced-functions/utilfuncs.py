"""
Demonstrate built-in utility functions
    - Some could be useful for data analysis
"""

def main():
    # use any() and all() to test sequences for boolean values
    stats = [1, 2, 3, 0, 5, 6]
    
    # any will return true if any of the sequence values are true
    print(any(stats))
    
    # all will return true only if all values are true
    print(all(stats))
    
    # min and max will return minimum and maximum values in a sequence
    print("min: ", min(stats))
    print("max: ", max(stats))    
    
    # Use sum() to sum up all of the values in a sequence
    print("sum: ", sum(stats))
    
    
if __name__ == "__main__":
    main()
    