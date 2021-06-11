# https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers, n):
    checkout_list = []
    for pos in range(n):
        checkout_list.append(0)
    for customers_time in customers:
        min_position = checkout_list.index(min(checkout_list))
        checkout_list[min_position] += customers_time
    return max(checkout_list)
