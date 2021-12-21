n = int(input())

class_list = []
for i in range(n):
    student, score = input().split()
    class_list.append((student, score))
    
# print(class_list)

def setting(data):
    return data[1]

result = sorted(class_list, key=setting)

for i in result:
    print(i[0], end=" ")
    
    
    
# 정답
n = int(input())

# N명의 학생 정보를 입력 받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 출력
for student in array:
    print(student[0], end=' ')