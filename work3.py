# 함수 정의부
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

while True: # 무한 반복
    calc1 = input("a : ") # calc1 변수를 입력받는다
    if calc1 == "q": # q 일경우 종료
        break
    op = input("+, -, *, / : ") # 연산자를 입력받는다
    calc2 = input("b : ") # calc2 변수를 입력받는다
    if op == "+": # 연산자 + 일때
        print(add(int(calc1), int(calc2)))
    elif op == "-": # 연산자 - 일때
        print(sub(int(calc1), int(calc2)))
    elif op == "*": # 연산자 * 일때
        print(mul(int(calc1), int(calc2)))
    elif op == "/": # 연산자 / 일때
        if calc2 == "0": # 0으로 나누기 예외처리
            print("0으로 나눌 수 없습니다.")
            continue
        print(div(int(calc1), int(calc2)))
    else: # 잘못 입력되었을 경우
        print("input error")