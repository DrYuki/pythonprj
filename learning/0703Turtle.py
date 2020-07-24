import turtle

t = turtle.Turtle()

t.penup()
r = 255
t.goto(-r, 0)
t.pencolor((1.0,0,0))
t.pensize(4)
t.pendown()
t.begin_fill()
t.circle(r, 360)
t.fillcolor((0, 1.0, 1.0))
t.end_fill()
turtle.done()


