#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_element = []
    for element in my_list:
        if element not in unique_element:
            unique_element.append(element)
    total = 0
    for num in unique_element:
        total += num
    return total
