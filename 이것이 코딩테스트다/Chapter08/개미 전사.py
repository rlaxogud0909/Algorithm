n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])

#2 1 1 5 3 1

# d
# 0 0 0 0 0 0

# 1) d[0]
# 2 0 0 0 0 0

# 2) d[1]
# 2 2 0 0 0 0

# 3) d[2] -> (1) 2 vs (2) 2 + 1 = 3
# 2 2 3 0 0 0

# 4) d[3] -> (1) 3 vs (2) 2 + 5  = 7
# 2 2 3 7 0 0

# 5) d[4] -> (1) 7 vs (2) 3 + 3 = 6
# 2 2 3 7 7 0

# 6) d[5] -> (1) 7 vs (2) 7 + 1 = 8
# 2 2 3 7 7 8

# array
# 2 1 1 5 3 1

