# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(s):
    aux_s = short_s = ""
    for pos in range(len(s)):
        if s[pos] != " ":
            aux_s += s[pos]
        if s[pos] == " " or pos == len(s) - 1:
            if len(aux_s) < len(short_s) or short_s == "":
                short_s = aux_s
            aux_s = ""
    return len(short_s)
  
