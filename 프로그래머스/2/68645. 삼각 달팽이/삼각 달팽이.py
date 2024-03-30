steps = (
    # l: length, d: depth
    lambda l, d: (u + d for u in range(l)),
    lambda l, d: (1,) * l, 
    lambda l, d: (u - d for u in range(-(l+2), -2))
)

def fill_side(arr, idx, num, length, direction, depth):
    """
    리스트에 삼각형의 한 변을 채워넣습니다.
    arr: 채워 넣을 리스트
    idx: 직전의 인덱스
    num: 직전의 숫자
    length: 길이
    direction: 채워나가는 방향
    depth: 표면으로부터의 깊이
    """
    
    direction %= 3
    for step in steps[direction](length, depth):
        idx += step
        num += 1
        arr[idx] = num
    
    if direction == 2:
        depth +=2;
    
    # 그 다음에 실행될 fill_side 함수의 args
    return (arr, idx, num, length-1, direction+1, depth)


def solution(n):
    answer = [0] * sum(range(n+1))
    args = (answer, 0, 0, n, 0, 0)
    
    # recursion error 방지를 위해 반복문으로 실행
    while(args[3] > 0):
        args = fill_side(*args)
    
    return answer