import sys;

dir_r = 0, 0, -1, -1, -1, 0, 1, 1, 1
dir_c = 0, -1, -1, 0, 1, 1, 1, 0, -1
diag_r = -1, -1, 1, 1
diag_c = -1, 1, -1, 1

rl = sys.stdin.readline
N, M = map(int, rl().split())
board = [[0]*(N+1)] + [[0] + list(map(int, rl().split())) for _ in range(N)]

pos_r = [N, N, N-1, N-1]
pos_c= [1, 2, 1, 2]

def move(d, s):
  cnt = len(pos_r)
  for i in range(cnt):
    pos_r[i] = (pos_r[i] + dir_r[d] * s) % N
    pos_c[i] = (pos_c[i] + dir_c[d] * s) % N
    if pos_r[i] == 0: pos_r[i] = N
    if pos_c[i] == 0: pos_c[i] = N

def pour():
  cnt = len(pos_r)
  for i in range(cnt):
    board[pos_r[i]][pos_c[i]] += 1

def duplicate():
  cnt = len(pos_r)
  for i in range(cnt):
    for j in range(4):
      r = pos_r[i] + diag_r[j]
      c = pos_c[i] + diag_c[j]
      if r < 1 or r > N or c < 1 or c > N: continue
      if not board[r][c]: continue 
      board[pos_r[i]][pos_c[i]] += 1

tmp_r = []
tmp_c = []
tmp_v = []

def hide():
  cnt = len(pos_r)
  for _ in range(cnt):
    r = pos_r.pop()
    c = pos_c.pop()
    tmp_v.append(board[r][c])
    board[r][c] = 0
    tmp_r.append(r)
    tmp_c.append(c)

def recover():
  cnt = len(tmp_r)
  for _ in range(cnt):
    r = tmp_r.pop()
    c = tmp_c.pop()
    v = tmp_v.pop()
    board[r][c] = v

def form():
  for r in range(1, N+1):
    for c in range(1, N+1):
      if board[r][c] < 2: continue
      board[r][c] -= 2
      pos_r.append(r)
      pos_c.append(c)

for _ in range(M):
  d, s = map(int, rl().split())
  move(d, s)
  pour()
  duplicate()
  hide()
  form()
  recover()

print(sum((sum(row) for row in board)))