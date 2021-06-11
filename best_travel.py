# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

from itertools import combinations

def choose_best_sum(t, k, ls):
    best_dist = 0
    all_combinations = [sum(x) for x in combinations(ls, k)]
    for dist_sum in all_combinations:
        if dist_sum <= t and dist_sum > best_dist:
            best_dist = dist_sum
    return best_dist if best_dist > 0 else None
  
