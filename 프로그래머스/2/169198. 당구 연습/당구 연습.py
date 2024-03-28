on_line = (
    lambda sX, sY, x, y: x==sX and y < sY,
    lambda sX, sY, x, y: x==sX and y > sY,
    lambda sX, sY, x, y: y==sY and x < sX,
    lambda sX, sY, x, y: y==sY and x > sX,
)

flip = (
    lambda m, n, x, y: (x, -y),         # U
    lambda m, n, x, y: (x, (n<<1) - y), # D     n + (n-y)
    lambda m, n, x, y: (-x, y),         # L
    lambda m, n, x, y: ((m<<1) - x, y), # R     m + (m-x)
)

def distance(sX, sY, x, y):
    dx = x-sX if x > sX else sX-x
    dy = y-sY if y > sY else sY-y
    return dx**2 + dy**2

def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        distances = (
            distance(startX, startY, *flip[i](m, n, x, y))   
            for i in range(4)
            if not on_line[i](startX, startY, x, y)
        )
        answer.append(min(distances))
    return answer