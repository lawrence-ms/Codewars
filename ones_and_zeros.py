# https://www.codewars.com/kata/578553c3a1b8d5c40300037c

def binary_array_to_number(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return 2**(len(arr) - 1) * arr[0] + binary_array_to_number(arr[1:])
