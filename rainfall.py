# https://www.codewars.com/kata/56a32dd6e4f4748cc3000006

def get_num_list(town, strng):
    new_list = []
    for line in strng.split("\n"):
        if line.split(":")[0] == town:
            for chunk in line.split(":")[1].split():
                new_list.append(chunk.split(",")[0])
            return [float(num) for num in new_list[1:]]
    return -1

def mean(town, strng):
    if get_num_list(town, strng) == -1:
        return -1
    return sum(get_num_list(town, strng)) / 12
    
def variance(town, strng):
    if get_num_list(town, strng) == -1:
        return -1
    m = mean(town, strng)
    return sum((x - m)**2 for x in get_num_list(town, strng)) / 12
