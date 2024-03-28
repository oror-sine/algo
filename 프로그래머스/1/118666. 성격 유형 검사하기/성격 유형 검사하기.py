def solution(survey, choices):
    points = {k: 0 for k in 'RTCFJMAN'}
    for typ, choice in zip(survey, choices):
        idx, point = (0, 4 - choice) if choice < 4 else (1, choice - 4)
        points[typ[idx]] += point
        
    answer = ''.join(
        max('RTCFJMAN'[i:i+2], key=lambda k: points[k])
        for i in range(0, 8, 2)
    )
    
    return answer