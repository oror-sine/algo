def solution(num):
    cnt = 0
    
    while(cnt <= 500):
        if num == 1:
            return cnt
        
        cnt += 1
        num, r = divmod(num, 2)
        
        if r:
            cnt += 1
            num = num*3 + 2
        
    return -1