# https://www.codewars.com/kata/546f922b54af40e1e90001da

import string

def alphabet_position(text):
    alphabet = string.ascii_lowercase
    new_text = ""
    for char in text.lower():
        if char in alphabet:
            if len(new_text) > 0:
                new_text += " "
            new_text += str(alphabet.find(char) + 1)
    return new_text
    
