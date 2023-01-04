import turtle
import random

# 初始化turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(3)
t.color('red')

# 画出烟花
for i in range(50):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(random.randint(5, 20))

turtle.done()