# lambda 인자 : 표현식

# 두 수를 더하는 함수
def hap(x, y):
    return x + y

# 람다식으로는?
(lambda x,y: x + y)(10, 20)


# def 함수 이름 (매기변수):
#   return 결과

# 람다식으로는?
# lambda 매개변수: 결과

func = lambda x : x + 1 
func(4)