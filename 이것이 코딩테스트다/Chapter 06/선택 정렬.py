# 선택정렬
# 가장 작은 데이터를 선택해 맨 앞에 잇는 데이터와 바꾸고,
# 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복

# 스와프란
# 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
array =  [3, 5]
array[0], array[1] = array[1], array[0]
print(array)

# 선택 정렬 소스 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        
        array[i], array[min_index] = array[min_index], array[i] # 스와프
        
print(array)

# 선택 정렬의 시간 복잡도
# 선택 정렬은 n-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야함
# 연산 횟수 = N + (N-1) + (N-2) + ... + 2 -> (N^2 + N) / 2
# (N^2 + N) / 2 빅오표기법 -> O(N^2)
# 데이터 개수가 100배 늘어나면, 이론적으로 수행 시간이 10,000배 늘어난다
