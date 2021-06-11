# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for letter in string:
        if letter not in vowels:
            new_string += letter
    return new_string
    
