from collections import deque

n, m = map(int, input().split())

# 그래프
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 상하좌우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


    
def bfs(x, y):
    # 큐
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
    
        for i in range(len(dx)):
            
            if x+dx[i] < 0 or y+dy[i] < 0 or x+dx[i] >= n or y+dy[i] >= m:
                continue
            
            # if graph[x+dx[i]][y+dy[i]] == 0:
            #     continue
            
            if graph[x+dx[i]][y+dy[i]] == 1:
                graph[x+dx[i]][y+dy[i]] = graph[x][y] + 1
                queue.append((x+dx[i], y+dy[i]))
    return graph[n-1][m-1]

print(bfs(0, 0))
print(graph)