def solution(n):
    string = ['수', '박']
    answer = ''.join(string[i%2] for i in range(n))
    return answer