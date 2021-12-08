# 파이썬의 내장 함수인 map()는 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용
a = map(int, input().split())

print(type(a)) # <class 'map'>
print(a) # <map object ~>

users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M'},
         {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F'},
         {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M'},
         {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F'},
         {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F'}]

def conver_to_name(user):
    first, last = user["name"].split()
    return {"first": first, "last": last}

# map 또 다른 사용법
for name in map(conver_to_name, users):
    print(name)