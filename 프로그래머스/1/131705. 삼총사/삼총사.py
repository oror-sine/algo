from itertools import combinations

def solution(number):
    combs = combinations(number, 3)
    return sum(sum(comb) == 0 for comb in combs)