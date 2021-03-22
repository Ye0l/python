s = 0 #전역변수

#함수정의
def sum(n):
    # s = 0  지역변수
    global s #전역변수를 사용
    for i in range(1, n+1):
        s = s + i

    return s

#함수호출
print("sum = ", sum(10))

