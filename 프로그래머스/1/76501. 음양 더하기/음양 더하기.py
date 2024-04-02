def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        answer += absolute * (1 if sign else -1)
    return answer