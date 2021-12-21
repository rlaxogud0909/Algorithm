n = int(input())

value_list = []
for i in range(n):
    value_list.append(int(input()))
    
    
for i in sorted(value_list):
    print(i, end=" ")
    
    
    
# 정답
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))
    
# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

# 출력
for i in array:
    print(i, end=" ")