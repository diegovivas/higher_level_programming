#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    lista = []
    for x in tuple_a:
        lista.append(x)
    for y in tuple_b:
        lista.append(y)
    if len(lista) <= 3:
        lista.append(0)
        lista.append(0)
        lista.append(0)
        lista.append(0)
    lista[0] = lista[0] + lista[2]
    lista[1] = lista[1] + lista[3]
    new_tuple = (lista[0], lista[1])
    return new_tuple
