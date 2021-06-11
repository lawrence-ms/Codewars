# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    trib_list = signature[:n]
    for i in range(3, n):
        trib_list.append(sum(trib_list[i-3:i]))
    return trib_list
  
