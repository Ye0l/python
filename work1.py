import turtle
t = turtle.Turtle() # turtle객체를 t로 지정한다.
def circleDraw(t, r, f, n) : # 원을 그리는 함수 정의 시작. circleDraw(터틀객체, 반지름, forward이동거리, 원의 수)
    for i in range(1, n+1) : # 1부터 매개변수 n까지 반복하는 반복문 시작
        t.circle(r) # 반지름 r의 원 그리기
        t.forward(f) # f만큼 이동

circleDraw(t, 50, 40, 4) # Test case 1
t.penup()
t.goto(-200, 0)
t.pendown()
circleDraw(t, 60, 60, 3) # Test case 2

turtle.mainloop()