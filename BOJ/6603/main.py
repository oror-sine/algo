import sys
readline = sys.stdin.readline

def dp(callback):
  cache = {}
  def func(*args):
    if not cache.get(args):
      cache[args] = callback(*args)
    return cache[args]
  return func

@dp
def C6_out_of(n):
  if n == 6:
    c = 0
    for i in range(6):
      c += 1 << i
    return [c]
  
  arr = []

  for i in reversed(range(1<<(n-1), 1<<n)):
    cnt = sum(( 1 for j in range(n) if i & 1<<j))
    if cnt == 6: arr.append(i)
  return arr + C6_out_of(n-1)

buf = ""
while (TC:= readline().split())[0] != "0":
  K, *S = TC
  K = int(K)
  combinations = C6_out_of(K)
  for combination in combinations:
    buf += " ".join((S[i] for i in range(K) if combination & 1<<(K-i-1)))
    buf += "\n"
  buf += "\n"

print(buf)