# https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    tower = []
    for floor in range(n_floors):
        tower_spaces = " " * (n_floors - floor - 1)
        tower.append(tower_spaces + "*" * (2 * floor + 1) + tower_spaces)
    return tower
