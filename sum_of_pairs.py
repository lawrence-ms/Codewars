# https://www.codewars.com/kata/54d81488b981293527000c8f

def sum_pairs(ints, s):
    seen_list = set()
    for num in ints:
        if s - num in seen_list:
            return[s - num, num]
        seen_list.add(num)
