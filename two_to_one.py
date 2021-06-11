# https://www.codewars.com/kata/5656b6906de340bd1b0000ac

def longest(s1, s2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_s = ""
    for letter in alphabet:
        if letter in s1 or letter in s2:
            new_s += letter
    return new_s
