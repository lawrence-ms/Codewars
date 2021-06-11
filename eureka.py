# https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    eureka_list = []
    for num in range(a, b + 1):
        power = 1
        sum = 0
        for char in str(num):
            sum += int(char)**power
            power += 1
        if sum == num:
            eureka_list.append(num)
    return eureka_list
