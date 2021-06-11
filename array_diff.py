# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    new_list = []
    for char in a:
        if char not in b:
            new_list.append(char)
    return new_list
  
