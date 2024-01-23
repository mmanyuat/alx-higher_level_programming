#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]
            result = elem_1 / elem_2
        except ZeroDivisionError:
            print("division by 0")
        except(TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
