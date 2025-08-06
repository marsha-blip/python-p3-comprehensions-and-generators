#!/usr/bin/env python3
def return_evens(num_list):
    """
    Return a list of all even integers from the input list,
    using a list comprehension to filter by num % 2 == 0.
    """
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    """
    Return a new list of sentences where each string has an exclamation
    mark added at the end, using a list comprehension to transform each item.
    """
    return [sentence + "!" for sentence in sentence_list]
