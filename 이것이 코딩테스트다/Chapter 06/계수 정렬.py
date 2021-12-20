# 계수 정렬
# 특정한 조건이 부합할 때만 사용할 수 있찌만 매우 빠른 정렬 알고리즘

# 특정한 조건
# 데이터 크기 범위가 제한 되어 정수 형태로 표현할 수 있을 때만 사용
# 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용

# why?
# 계숙 정렬을 이용할 대는 모든 범위를 담을 수 있는 크기의 리스트를 선언해야하기 때문

# 계수 정렬 소스코드

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에서 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        
# 계수 정렬의 시간복잡도
# 데이터의 개수: N, 데이터 중 최대값의 크기: K
# -> O(N + K)
#계수 정렬은 앞에서 부터 데이터를 하나씩 확인하면서 리스트에서 적절한 인덱스값을 1씩 증가시킬 뿐만 아니라,
# 추후에 리스트의 각 인덱스에 해당하는 값들을 확인할 때 데이터 중 최대값의 크기만큼 반복적으로 수행해야하기 때문

# 단점
# 만약 데이터가 0과 999,999 단 두개라면
# 리스트 크기가 100만 개가 되도록 선언해야 함
