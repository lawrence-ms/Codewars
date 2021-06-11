# https://www.codewars.com/kata/55e2adece53b4cdcb900006c

def race(v1, v2, g):
    if v1 >= v2:
        return None
    time = int((g / (v2 - v1)) * 3600)
    hours = time // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60
    return [hours, minutes, seconds]
