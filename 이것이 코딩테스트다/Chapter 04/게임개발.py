# (A, B)
# A는 북쪽으로 부터 떨어진 칸의 개수
# B는 서쪽으로 부터 떨어진 칸의 개수

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에서 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진하다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간
# 3. 만약 네방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.



# x, y = map(int, input().split()) # 맵 
# A, B, direction = map(int, input().split()) # (A, B)와 방향

# # 맵을 2중 리스트를 만들어보자
# map_list = []
# for _ in range(x):
#     map_list.append(list(map(int, input().split())))
    
# start_location = map_list[A][B] # 시작 위치

# # 동서남북 방향
# map_list[A-1][B] # 북으로 이동
# map_list[A+1][B] # 남으로 이동
# map_list[A][B-1] # 서로 이동
# map_list[A][B+1] # 동으로 이동

# # 북(0), 동(1), 남(2), 서(3)
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

      
# 미해결  

# 정답)
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
            # turn_time = 0
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
        

# 정답 출력
print(count)