#!/usr/bin/python3
def uppercase(in_str):
    for char in in_str:
        ascii_value = ord(char)
        if ord('a') <= ascii_value <= ord('z'):
            uppercase_char = char(ascii_value - ord('a') + ord('A'))
        else:
            uppercase_char = char
        print(uppercase_char, end=" ")
    print( )
