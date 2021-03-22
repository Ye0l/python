import turtle

cor = ["red","green","blue"]
print(cor[0])
print("cor = ", len(cor))

def makeTurtle(t, m, r, c):
    t.color(c)
    t.circle(r)
    t.forward(m)


t = turtle.Turtle()
makeTurtle(t, 50, 50, cor[1])
makeTurtle(t, 100, 180, cor[0])

turtle.mainloop()
turtle.bye()



