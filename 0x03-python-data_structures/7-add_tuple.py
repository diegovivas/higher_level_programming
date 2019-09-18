#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    lista = []
    listab = []
    for x in tuple_a:
        lista.append(x)
    for y in tuple_b:
        listab.append(y)
    if len(lista) <= 3:
        lista.append(0)
        lista.append(0)
        lista.append(0)
        lista.append(0)
    if len(listab) <= 2:
        listab.append(0)
        listab.append(0)
        listab.append(0)
    lista[0] = lista[0] + listab[0]
    listab[0] = lista[1] + listab[1]
    new_tuple = (lista[0], listab[0])
    return new_tuple
