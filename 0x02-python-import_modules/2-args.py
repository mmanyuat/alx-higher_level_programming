#!/usr/bin/python3
import sys
n = len(sys.argv)

if n == 1:
    print("0 arguments:")
elif n == 2:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    print(n-1, "arguments:")
    for i in range(1, n):
        print("{} : {}".format(i, sys.argv[i]))
