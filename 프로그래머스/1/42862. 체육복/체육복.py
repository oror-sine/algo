def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    lost_and_reserve = lost_set & reserve_set
    
    lost_set -= lost_and_reserve
    reserve_set -= lost_and_reserve
    
    for res in reserve_set:
        m1, p1 = res-1, res+1
        if m1 in lost_set:
            lost_set.remove(m1)
        elif p1 in lost_set:
            lost_set.remove(p1)
        
    return n - len(lost_set)