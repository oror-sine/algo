from math import pow, sqrt, floor

def solution(k, d):
    nd = d/k
    nd_square = pow(nd, 2)
    answer = sum(
        floor(sqrt(nd_square - pow(h, 2)))+1
        for h in range(floor(nd)+1)
    )

    return answer