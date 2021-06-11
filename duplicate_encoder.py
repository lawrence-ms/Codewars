# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

import collections

def duplicate_encode(word):
    dup_dict = collections.defaultdict(int)
    new_word = ""
    for letter in word.lower():
        dup_dict[letter] += 1
    for letter in word.lower():
        if dup_dict.get(letter, 0) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word
