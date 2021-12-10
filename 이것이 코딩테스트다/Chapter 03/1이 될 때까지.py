n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n = n//k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

# 답안
# 1)
n, k =map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1 씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1
    
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

######################################################
# 2) **
n, k =map(int, input().split())
result = 0

while True:
    # (N == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # Kㄹ 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)