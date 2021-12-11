# n = int(input())

# # L, R, U, D -> x, y
# x = [-1, 1, 0, 0]
# y = [0, 0, -1, 1]

# move = {'L': 0, 'R': 1, 'U': 2, 'D': 3}

# a, b = 1, 1


# for _ in range(n):
#     m = input()
#     dx = x[move[m]]
#     dy = y[move[m]]
    
#     # 범위 벗어날 때
#     if a+dy < 1 or b+dx < 1 or a+dy > n or b+dx > n:
#         continue
    
#     a += dy
#     b += dx
#     print(a, b)

# print(a, b)
    
# 범위를 벗어날 경우 무시를 했지만 그 만큼 더 움직여야함 -> 미해결

# 정답)
n = int(input())
x, y = 1, 1
plans = list(input().split())

# print(plans)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)