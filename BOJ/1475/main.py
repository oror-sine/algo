import sys
buf = sys.stdin.readline().strip()
cnts = [0]*9

for num in buf:
  cnts[6 if num == '9' else int(num)] += 1
cnts[6] = (cnts[6] + 1) >> 1

sys.stdout.write(f"{max(cnts)}")