# https://www.codewars.com/kata/556e0fccc392c527f20000c5

def Xbonacci(signature,n):
    x_list = []
    x = len(signature)
    if n == 0:
        return []
    elif n <= x:
        return signature[:n]
    else:
        x_list += signature
        for i in range(x, n):
            x_list.append(sum(x_list[i-x:i]))
    return x_list
