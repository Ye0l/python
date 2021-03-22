import turtle
from random import *
t = turtle.Turtle() # turtle객체를 t로 지정한다.
t.speed(0)
def circleDraw(t, r, f, n) : # 원을 그리는 함수 정의 시작. circleDraw(터틀객체, 반지름, forward이동거리, 원의 수)
    turtle.colormode(255)
    for i in range(1, n+1) : # 1부터 매개변수 n까지 반복하는 반복문 시작
        t.pencolor(randint(0,255), randint(0,255), randint(0,255))
        t.circle(r) # 반지름 r의 원 그리기
        t.forward(f) # f만큼 이동

while True: # 무한 반복
    r = input("반지름 입력: ") # r만 따로 입력받는다. q입력을 통해 반복을 종료할 것이기 때문
    if(r == "q"): # r에 q가 입력되었을 경우
        break # 반복문 탈출
    circleDraw(t, int(r), int(input("이동 거리 입력: ")), int(input("원의 갯수 입력: "))) # 지시한 만큼 circleDraw 실행