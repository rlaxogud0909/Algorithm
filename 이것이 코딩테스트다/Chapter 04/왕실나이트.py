# 1) 좌표를 만들어 보자

n = list(input())

# print(type(n))
# print(n)

row = int(n[1])
column = ord(n[0]) - ord('a') + 1
count = 0

# (column, row)
# (-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2) -> 총 경우의 수
move_row = [-1, 1, -1, 1, -2, -2, 2, 2]
move_column = [-2, -2, 2, 2, 1, -1, 1, -1]

for i in range(len(move_row)):
    a = row + move_row[i]
    b = column + move_column[i]
    # column이랑 row가 0이하, 9이상을 넘을 수 없다
    if a < 1 or a > 8 or b < 1 or b > 8:
        continue
    count += 1
    
print(count)        


# 정답)
# 1)
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


# 참고로 앞서 '상하좌우' 문제에서는 dx, dy리스트를 선언하여 이동할 방향을 기록할 수 있도록 하였다.
# 이번 소스코드에서는 steps 변수가 dx와 dy 변수의 기능을 대신하여 수행한다.
# 이 2가지 형태 모두 자주 사용되므로 참고하도록하자