def solution(number):
    answer = sum(
      i < j < k and a + b + c == 0
      for i, a in enumerate(number)
      for j, b in enumerate(number)
      for k, c in enumerate(number)
    )
    return answer