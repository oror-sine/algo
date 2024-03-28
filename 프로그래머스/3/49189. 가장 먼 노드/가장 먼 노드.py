from collections import deque

def solution(n, edge):
    m = {}
    vis = {}
    for k in range(1, n+1):
        m[k] = []
        vis[k] = False
        
    for v1, v2 in edge:
        m[v1].append(v2)
        m[v2].append(v1)
    
    Q = deque()
    Q.append(1)
    vis[1] = True
    
    while Q:
        answer = len(Q)
        for __ in range(len(Q)):
            curr = Q.popleft()
            for nxt in m[curr]:
                if vis[nxt]: continue
                vis[nxt] = True
                Q.append(nxt)

    return answer