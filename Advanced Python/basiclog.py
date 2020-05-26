"""
Demonstrate the logging api in Python
    - Useful for debugging purposes
"""

# use the built-in logging module
import logging


def main():
    # Use basicConfig to configure logging
    # this is only executed once, subsequent calls to
    # basicConfig will have no effect
    logging.basicConfig(level=logging.DEBUG,
                        filemode="w",
                        filename="output.log")

    # Log Levels
    logging.debug("This is a debug-level log message")   # Diagnostic info useful for debugging
    logging.info("This is an info-level log message")    # General info about program execution results
    logging.warning("This is a warning-level message")   # Something unexpected, or an approaching problem
    logging.error("This is an error-level message")      # Unable to perform a specific operation due to problem
    logging.critical("This is a critical-level message") # Program may not be able to continue, serious error

    # Output formatted string to the log
    logging.info("Here's a {} variable and an int: {}".format("string", 10))


if __name__ == "__main__":
    main()
