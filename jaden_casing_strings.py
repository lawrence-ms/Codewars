# https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    new_string = ""
    for pos in range(len(string)):
        if pos == 0 or string[pos -1] == " ":
            new_string += string[pos].upper()
        else:
            new_string += string[pos]
    return new_string
