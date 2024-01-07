#!/usr/bin/python3
for i in range(1, 90):
    print("{:02d}".format(i), end=", " if i < 89 else "\n")
