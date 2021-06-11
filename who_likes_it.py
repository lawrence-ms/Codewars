# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    num_people = len(names)
    if num_people == 0:
        return "no one likes this"
    elif num_people == 1:
        return names[0] + " likes this"
    elif num_people == 2:
        return names[0] + " and " + names[1] + " like this"
    elif num_people == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
