#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ", end=" ")
            continue
        elif i % 3 == 0:
            print("FIZZ", end=" ")
            continue
        elif i % 5 == 0:
            print("BUZZ", end=" ")
            continue
        else:
            print(i, end=" ")
