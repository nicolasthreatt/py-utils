"""
Demonstrate how to customize logging output
    - Useful for debugging 

Customized Loggins
    %(asctime)s   - Human readable date format when the log record was created
    %(filename)s  - Filename where the log message originated
    %(funcName)s  - Function name where the log message originated
    %(levelname)s - String representation of the message level (DEBUG, INFO, etc)
    %(levelno)d   - Numeric representation of the message level
    %(message)s   - The logged message string itself
    %(module)s    - Module name portion of the filename where the message was logged
"""

import logging

extData = {'Player Overrated': 'Kawhi Leonard'}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # Set the output file and debug level, and use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d Player Overrated:%(Player Overrated)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"

    """
    basicConfig(
        format = formatstr,
        datefmt = date_format_str
    )
    """
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    main()
