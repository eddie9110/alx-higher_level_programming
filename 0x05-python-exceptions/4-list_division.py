#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for vx in range(list_length):
        result = 0
        try:
            result = my_list_1[vx] / my_list_2[vx]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            n_list.append(result)
    return n_list
