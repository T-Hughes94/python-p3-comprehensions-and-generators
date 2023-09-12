#!/usr/bin/env python3

def return_evens(num_list):
    return[n for n in num_list if n % 2 == 0]
return_evens([1, 2, 3, 4, 5, 6])

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]