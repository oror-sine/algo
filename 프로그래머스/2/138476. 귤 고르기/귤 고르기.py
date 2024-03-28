from collections import Counter

def solution(k, tangerine):
    cnts = Counter(tangerine)
    for i, cnt in enumerate(sorted(cnts.values(), reverse=True)):
        k -= cnt
        if k <= 0:
            return i+1