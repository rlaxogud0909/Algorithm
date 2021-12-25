
def one_make(a ,cnt):
    if a == 1:
        return cnt
    
    if a % 5 == 0:
        a = a // 5
        cnt += 1
        return one_make(a, cnt)
    elif a % 3 == 0:
        a = a // 3
        cnt += 1
        return one_make(a, cnt)
    elif a % 2 == 0:
        a = a // 2
        cnt += 1
        return one_make(a, cnt)
    else:
        a -= 1
        cnt += 1
        return one_make(a, cnt)
        

# print(one_make(26, 0))

# 문제점
# 내풀이: 26 -> 13 -> 12 -> 4 -> 2 -> 1 (5)
# 정답: 26 -> 25 -> 5 -> 1 (3)

# 최솟값을 어떻게 구하지??

# 정답)
# **** 약간 이해 안됨 ****
# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1를 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
        
print(d[x])

for i in range(27):
    print(str(i)+":", str(d[i]))
