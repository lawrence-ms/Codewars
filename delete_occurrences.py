# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    repeat_dict = {}
    new_order = []
    for num in order:
        repeat_dict[num] = 0
    for num in order:
        repeat_dict[num] += 1
        if repeat_dict[num] <= max_e:
            new_order.append(num)
    return new_order
