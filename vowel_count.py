# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(input_str):
    num_vowels = 0
    vowels = "aeiou"
    for char in input_str:
        if char in vowels:
            num_vowels += 1
    return num_vowels
    
