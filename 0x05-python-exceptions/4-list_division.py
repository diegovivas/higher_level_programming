#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista = []
    for i in range(list_length):
        divi = 0
        try:
            divi = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            pass
        except TypeError:
            print("wrong type")
            pass
        except ZeroDivisionError:
            print("division by 0")
            pass
        finally:
            lista.append(divi)
    return lista
