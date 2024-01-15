#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    if even_numbers == 0:
        return even_numbers()
    else :
        return even_numbers

def make_exclamation(sentence_list):
    exclamated = [sentence + "!" for sentence in sentence_list]
    if exclamated == 0:
        return exclamated()
    else:
        return exclamated
