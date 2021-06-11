# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    max_sum = aux_sum = 0
    for l_bound in range(len(arr)):
        for h_bound in range(len(arr)):
            aux_sum = sum(arr[l_bound:h_bound + 1])
            if aux_sum > max_sum:
                max_sum = aux_sum
    return max_sum
