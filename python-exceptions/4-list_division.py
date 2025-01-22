#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_res = 0
    div_list = []
    for i in range(list_length):
        try:
            div_res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_res = 0
        except TypeError:
            print("wrong type")
            div_res = 0
        except IndexError:
            print("out of range")
            div_res = 0
        finally:
            div_list.append(div_res)
    return div_list
