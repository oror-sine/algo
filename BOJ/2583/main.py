import sys
readline = sys.stdin.readline

M, N, K = map(int, readline().split())
arr = [[0]*N for _ in range(M)]

for _ in range(K):
  sc, sr, ec, er  = map(int, readline().split())
  for row in range(sr, er):
    for col in range(sc, ec):
      arr[row][col] = True

areas = []
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

for row in range(M):
  for col in range(N):
    if arr[row][col]: continue

    stack = [(row, col)]
    arr[row][col] = True
    area = 1
    
    while stack:
      cr, cc = stack.pop()
      for i in range(4):
        nr = cr+dr[i]
        nc = cc+dc[i]
        if not (nr <= -1 or  nr >= M or nc <= -1 or  nc >= N ) and not arr[nr][nc]:
          arr[nr][nc] = True
          stack.append((nr, nc))
          area +=1
    else:
      areas.append(area)

sys.stdout.write(f"{len(areas)}\n{' '.join(map(str, sorted(areas)))}")

