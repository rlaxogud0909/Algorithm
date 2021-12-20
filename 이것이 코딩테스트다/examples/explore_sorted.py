# sorted()는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌는데,
# 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경웨도 시간 복잡도가 O(NlogN)을 보장한다는 특징

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# sort()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# 정렬 라이브러리에서 key를 활요한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

# print(setting)

result = sorted(array, key=setting)
print(result)