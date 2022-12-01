#!/usr/bin/python3
"""Print the number of and list of arguments."""
import sys
if __name__ == "__main__":

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1 or count == 2:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
