# 최단 경로
# 1) 다익스트라 최단 경로 알고리즘
# 2) 플로이드 워셜
# 3) 벨만 포드 알고리즘

# 다익스트라 최단 경로 알고리즘이란?
# 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘

# 구현 방법 2가지
# 방법 1: 구현하기 쉽지만 느리게 동작하는 코드
# 방법 2: 구현하기에는 조금 더 까다롭지만 빠르게 동작하는 코드

# 방법 1)
# 간단한 다익스트라 알고리즘 소스코드
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력 받음
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))
    
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없느 경우, 무한 이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])
        
        
# 다익스트라 최단 경로 알고리즘에서는 '방문하지 않는 노드 중에서 가장 최단 거리가 짧은 노드를 선택'하는 과정을 반복하는데,
# 이렇게 선택된 노드는 '최단 거리'가 완전히 선택된 노드이므로 더이상 알고리즘을 반복해도 최단거리가 줄어들지 않는다.
# 즉, 다익스트라 알고리즘이 진행되면서 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해
        
        
# 시간복잡도
# O(V^2)
# 여기서 V는 노드의 개수

# 처음에는 각 노드에 대한 최단 거리를 담는 1차원 리스트를 선언한다.
# 이후에 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)한다.

# 시간복잡도가 O(V^2)이기 때문에 전체 노드의 개수가 5000개이하라면 일반적인 코테에서 풀수 잇을 것이다
# 하지만 노드 개수가 10000개가 넘어가면 이 코드로 해결하기 어렵다. -> 개선된 다익스트라 알고리즘