#!/usr/bin/env python3

def return_evens(numbers):
    return [n for n in numbers if n % 2 == 0]


def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]
