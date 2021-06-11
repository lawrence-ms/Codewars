# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

def increment_string(strng):
    char_str, num_str = "", ""
    for i in range(len(strng), 0, -1):
        if strng[i-1].isnumeric() and char_str == "":
            num_str = strng[i-1] + num_str
        else:
            char_str = strng[i-1] + char_str
    num_len = len(num_str)
    if num_len == 0:
        return (char_str + '1')
    num_str = str(int(num_str) + 1)
    if num_len > len(num_str):
        for i in range(len(num_str), num_len):
            char_str += '0'
    return (char_str + num_str)
