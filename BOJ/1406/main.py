import sys
readline = sys.stdin.readline

stack_l = [c for c in readline().strip()]
stack_r = []

M = int(readline())
for _ in range(M):
  command = readline().strip()
  if command == "L":
    if stack_l: stack_r.append(stack_l.pop())
  elif command == "B":
    if stack_l: stack_l.pop()
  elif command == "D" :
    if stack_r: stack_l.append(stack_r.pop())
  else:
    stack_l.append(command[2])

while stack_r:
  stack_l.append(stack_r.pop())

sys.stdout.write("".join(stack_l))