def solution(n):
    answer = ''.join("수박"[i%2] for i in range(n))
    return answer