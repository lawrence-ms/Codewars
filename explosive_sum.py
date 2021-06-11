# https://www.codewars.com/kata/52ec24228a515e620b0005ef

mem_dict = {}

def exp_sum(n):
    return p(n, n)

def p(n, k):
    if k == 0 or n < 0:
        return 0
    if n == 0:
        return 1
    if (n, k) in mem_dict.keys():
        return mem_dict[(n, k)]
    mem_dict[(n, k)] = p(n, k-1) + p(n-k, k)
    return mem_dict[(n, k)]
