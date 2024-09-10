#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1

    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print(n, "arguments:")
        for i in range(1, len(sys.argv)):
            print("{} : {}".format(i, sys.argv[i]))
