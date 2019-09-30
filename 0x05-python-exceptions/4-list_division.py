#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista = []
    ojo = 0
    for i in range(list_length):
        try:
            divi = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            ojo += 0
        except TypeError:
            print("wrong type")
            ojo += 0
        except ZeroDivisionError:
            print("division by 0")
            ojo += 0
        finally:
            lista.append(divi)
    return lista
