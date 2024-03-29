def solution(number):
    answer = 0
    for i, a in enumerate(number):
        for j, b in enumerate(number):
            for k, c in enumerate(number):
                if i < j < k and a + b + c == 0:
                    answer += 1
                    
    return answer