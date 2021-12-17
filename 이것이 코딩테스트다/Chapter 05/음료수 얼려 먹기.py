# 탐색 문제는 그래프 형태로 표현

# 좌표 크기
n, m = map(int, input().split())

# 2중 리스트 좌표 설정
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    

# dfs 방식
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        print(x, y) # 이동 방향을 볼 수 있음
        
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
        
print(result)