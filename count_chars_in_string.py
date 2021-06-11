# https://www.codewars.com/kata/52efefcbcdf57161d4000091

def count(string):
    count_dict = {}
    for char in string:
        count_dict[char] = 0
    for char in string:
        count_dict[char] += 1
    return count_dict
