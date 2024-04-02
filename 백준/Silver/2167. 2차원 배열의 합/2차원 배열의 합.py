import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(N)]

K = int(input())

answer = []
for __ in range(K):
    i, j, x, y = map(int, input().split())
    answer.append(str(sum(sum(arr[r][j-1:y]) for r in range(i-1, x))))

print('\n'.join(answer))