from collections import defaultdict

def solution(k, tangerine):
    d = defaultdict(int)
    for size in tangerine:
        d[size] += 1
    for i, cnt in enumerate(sorted(d.values(), reverse=True)):
        k -= cnt
        if k <= 0:
            return i+1