# https://www.codewars.com/kata/54d512e62a5e54c96200019e

def primeFactors(n):
    decomp_string = ""
    for num in range(2, n + 1):
        prime_power = 0
        while n % num == 0:
            n /= num
            prime_power += 1
        if prime_power > 1:
            decomp_string += "(" + str(num) + "**" + str(prime_power) + ")"
        elif prime_power == 1:
            decomp_string += "(" + str(num) + ")"
        if n == 1:
            return decomp_string
