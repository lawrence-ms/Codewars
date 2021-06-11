# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    numbers = numbers.split()
    odd_count = odd_pos = even_count = even_pos = 0
    for pos in range(len(numbers)):
        if int(numbers[pos]) % 2 == 0:
            even_count += 1
            even_pos = pos
        else:
            odd_count += 1
            odd_pos = pos
    if even_count == 1:
        return even_pos + 1
    else:
        return odd_pos + 1
