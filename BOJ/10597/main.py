import sys
nums = sys.stdin.readline()

if len(nums) <= 9:
  print(" ".join(nums))
else:
  N = 9 + (len(nums)-9)//2
  arr = {str(i+1) : True for i in range(N)}
  stack = []

  def backtrack(index):
    if(len(stack) == N): return True
    buf = ""
    for i in range(2):
      buf += nums[index+i]
      if arr.get(buf):
        arr[buf] = False
        stack.append(buf)
        if backtrack(index+i+1): return True
        arr[buf] = True
        stack.pop()

  backtrack(0)
  print(" ".join(stack))
  