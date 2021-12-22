# 이진 탐색
# 배열 내부의 데이터가 정렬됭 있어야만 사용할 수 있는 알고리즘

# 위치를 나타내는 변수 3개 : 시작점, 끝점, 중간점
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것

# 원소의 개수가 절반씩 줄어든다는 점에서 시간복잡도가 O(logN)
# 32 -> 16 -> 8 -> 4 -> 2 -> 1 (5번): log 32 -> 5

# 이진 탐색을 구현하는 방법
# 1) 재귀함수를 이용하는 방법
# 2) 반복문을 이용하는 방법

# 1) 재귀 함수로 구현한 이진 탐색 소스코드
def binary_serach(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_serach(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_serach(array, target, mid + 1, end)
    
# n(원소의 개수)과 target(찾고자하는 문자열)을 입력
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_serach(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
    
# 2) 반복문으로 구현한 이진 탐색 소스코드
def binary_serach(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾는 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자하는 문자열)을 입력
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_serach(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
    

# 이진 탐색은 코테 단골로 나오는 문제이니 외우길 권장
# 이진 탐색 문제는 탐색 범위가 큰 상황에서 탐색을 가정하는 문제가 많음 (탐색 범위가 2,000만을 넘어가면 이진탐색 권장)
# 또한 처리해야할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진탐색 같이 O(logN)의 속도를 내야하는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많음


# ex) 데이터 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이사일면 이진 탐색 알고리즘 의심
