# https://www.codewars.com/kata/59c633e7dcc4053512000073

def solve(s):
    vowels = "aeiou"
    sub_list = s
    for letter in vowels:
        sub_list = sub_list.replace(letter, " ")
    sub_list = sub_list.split()
    score_list = [0] * len(sub_list)
    for pos in range(len(sub_list)):
        for char in sub_list[pos]:
            score_list[pos] += (ord(char) - 96)
    return max(score_list)
