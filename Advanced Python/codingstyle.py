"""
Style Guide for Python Code

Code Structure and Format
    - Import statements go at the top, adn each have their own line
    - Indent code using spaces instead of tabs
        + Use for spaces for each indentaion level
    - Limit lines to 79 characters (72 for docstrings/comments)
    - Seperate functions and classes by two blank lines
    - Within classes, seperate methods by one blank line
    - No spaces around function calls, indexes, keyword arguments

https://www.python.org/dev/peps/pep-0008/
"""

# imports go on their own lines
import sys
import os


# two blank lines separate classes from other functions
class MyClass():
    def __init__(self):
        self.prop1 = "my class"

    # within classes, one blank line separates methods
    def method1(self, arg1):
        pass


def main():
    # Long comments, like this one that flow across several lines, are
    # limited to 72 characters instead of 79 for lines of code.
    cls1 = MyClass()
    cls1.prop1 = "hello world"


if __name__ == "__main__":
    main()
