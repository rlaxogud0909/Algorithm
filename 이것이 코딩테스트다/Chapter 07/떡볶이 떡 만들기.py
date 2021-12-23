
def binary_search(rice_cakes, start, end, m):
    mid = (start + end) // 2
    # print('mid::', mid) # 중간값 경로 탐색
    
    result = 0
    for i in rice_cakes:
        if i > mid:
            result += i - mid
        else:
            result += 0
    
    if result == m:
        return mid
    elif result > m:
        return binary_search(rice_cakes, mid + 1, end, m)
    else:
        return binary_search(rice_cakes, start, mid - 1, m)
    



# 입력 받기
n, m = map(int, input().split())

rice_cakes = sorted(list(map(int, input().split())))


print(binary_search(rice_cakes, 0, rice_cakes[n-1], m))


# 정답)
# 떡의 개수와 요청한 떡의 길이를 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 선정
start = 0
end = max(array)

# 이진 탐색 수행(반복문)
result = 0
while(start >= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부복한 경우 더 많이 자르기( 왼쪽 부분 탐색 )
    if total < m:
        end = mid - 1
    # 덕의 양이 충분한 경우 덜 자르기( 오른쪽 부분 탐색 )
    else:
        result = mid # 최대한 덜 자랐을 때가 정답이므로, 여기서 result에 기록
        start = mid + 1
        
# 정답출력
print(result)


# 전형적인 이진 탐색 문제이자, 파라메트릭 서치 유형의 문제
# 파라메트릭 서치: 최적화 문제를 결정 문제( '예/아니오'로 답하는 문제 )로 바꾸어 해결하는 방법

# 문제에서 절단기의 높이가 1부터 10억까지의 정수 중 하나인데 이처럼 큰수는 가장 먼저 이진탐색을 떠올려야한다.
# 반면 높이를 이진탐색으로 찾는다면 대략 31번의 경우의수 
# 떡의 개수 N이 치대 100만 개 이므로 이진 탐색으로 절단기의 높이 H를 바꾸면서,
# 바꿀 때마다 모든 떡을 체크하는 경우 대략 최대 3000만번 정도 연산
# 시간제안이 2초이므로 최악의 경우 3000만번 정도의 연산이 필요하다면 아슬아슬하게 정답