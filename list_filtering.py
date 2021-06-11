# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(l):
  new_l = []
  for char in l:
      if type(char) != str:
          new_l.append(char)
  return new_l
  
