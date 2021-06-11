# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

def tickets(people):
    vasya_wallet = {25:0, 50:0, 100:0}
    for bill in people:
        if bill == 50:
            if vasya_wallet[25] >= 1:
                vasya_wallet[25] -= 1
            else:
                return "NO"
        if bill == 100:
            if vasya_wallet[25] >=1 and vasya_wallet[50] >=1:
                vasya_wallet[50] -= 1
                vasya_wallet[25] -= 1
            elif vasya_wallet[25] >= 3:
                vasya_wallet[25] -= 3
            else:
                return "NO"
        vasya_wallet[bill] += 1
    return "YES"
