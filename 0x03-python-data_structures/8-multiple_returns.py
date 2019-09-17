#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuples = (len(sentence), sentence[0])
    else:
        tuples = (0, None)
    return tuples
