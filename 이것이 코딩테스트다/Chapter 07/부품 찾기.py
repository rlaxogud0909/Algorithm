
# 이진탐색 (재귀함수)
def binary_search(array, start, end, target):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    # mid 값이 찾는 값보다 큰 경우 (왼쪽)
    elif array[mid] > target:
        return binary_search(array, start, mid - 1, target)
    # mid 값이 찾는 값보다 작은 경우 (오른쪽)
    elif array[mid] < target:
        return binary_search(array, mid + 1, end, target)


# binary_search 테스트
# print(binary_serach(array, 0, len(array)-1, 3))


# 입력 받기
n = int(input())
array = list(map(int, input().split()))

# 찾을 값
m = int(input())
value_array = list(map(int, input().split()))


arrary = array.sort()

for i in range(m):
    target = value_array[i]
    if binary_search(array, 0, n-1, target) == False:
        print("no", end=' ')
    else:
        print("yes", end=' ')

# 정답
# 시간복잡도
# 부품을 차즌 과정에서 최악의 경우 시간복잡도: O(M * logN)
# N개의 부품을 정렬하기 위해서 요구되는 시간복잡도: O(N * logN)
# 이진탐색으로 풀경우 O((M + N) * logN)

# 1) 이진탐색 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = min - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
# 2) 계수정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1
    
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
# 3) 집합 자료형 이용 (set())
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        