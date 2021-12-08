# 행과 열을 입력
column, row = map(int, input().split())

# 행별로 total_list에 추가
total_list = []
for _ in range(column):
    total_list.append(list(map(int, input().split())))
    
# 각 행에서 가장 작은 수를 small_list에 추가
small_list = []
for i in total_list:
    small_list.append(min(i))
    
    
print(max(small_list))

#########################################################################

# 책 답안
# 1) min() 함수를 이용한 답안 예시
# 각 행을 data에 넣어 작은 수를 구하고 그 작은 수들 중에서 가장 큰 수를 찾음
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

##############################################################################

# 2) 2중 반복문 구조를 이용한 답안 예시
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_vlaue = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)