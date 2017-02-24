'''Using map-reduce'''
# -*- coding: utf-8 -*-

from functools import reduce


def count_words(doc):
    ''' Returns count for a string'''

    # Convert to lower case
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    # Split words
    for word in normalized_doc.split():
        # frequencies.get(word, 0) == frequencies[word] if word in frequencies
        # else return 0
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

DOCUMENTS = ['I was getting ready to be a threat',
             'I was getting set for my',
             'accidental suicide',
             'the kind where no one dies']

# Map each string in DOCUMENTS to seperate dictionaries
COUNTS = map(count_words, DOCUMENTS)


def combine_words(first_dict, second_dict):
    '''Combine 2 dictionaries'''

    # Do a shallow copy of first_dict
    new_dict = first_dict.copy()
    for word, count in second_dict.items():
        new_dict[word] = new_dict.get(word, 0) + count
    return new_dict

# Combine all dictionaries
TOTAL_COUNT = reduce(combine_words, COUNTS)

print(TOTAL_COUNT)
