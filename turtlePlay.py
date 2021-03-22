import turtle

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

def pentagon(t, n):
    for i in range(0, 5):
        t.forward(n)
        t.left(360/5)

t.up()
# t.goto(-300,0)
t.down()

t.begin_fill()
for i in range(1, 256,2):
    t.color(255-i,i,0)
    t.left(360/256*2/3)
    t.left(90)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.left(90)

for i in range(1, 256,2):
    t.color(0,255-i,i)
    t.left(360/256*2/3)
    t.left(90)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.left(90)

for i in range(1, 256,2):
    t.color(i,0,255-i)
    t.left(360/256*2/3)
    t.left(90)
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.left(90)

t.end_fill()

turtle.mainloop()