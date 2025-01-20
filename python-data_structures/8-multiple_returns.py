#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        tuple_sentence = (len(sentence), sentence[0])
    else:
        tuple_sentence = (len(sentence), None)
    return tuple_sentence
