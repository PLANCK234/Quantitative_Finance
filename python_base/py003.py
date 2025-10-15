import turtle

# 画一个奥运五环
turtle.width(7)

turtle.color("blue")
turtle.circle(50)

turtle.penup()
turtle.goto(125,0)
turtle.pendown()
turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(250,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(62.5,-50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(187.5,-50)
turtle.pendown()
turtle.color("green")
turtle.circle(50)

turtle.done()