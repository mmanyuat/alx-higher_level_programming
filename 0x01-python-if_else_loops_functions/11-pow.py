#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        result = 1
        for _ in range(b):
            result *= (a)
        return result
    else:
        result = 1.0
        for _ in range(int(abs(b))):
            result /= int(a)
        return result
