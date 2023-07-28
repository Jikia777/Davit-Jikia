from turtle import *

speed(0)
# House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "brown") # (stroke, fill)
begin_fill()
for i in range(4):
    forward(170)
    left(90)
end_fill()

# Chimney
penup()
goto(20, 130)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# Roof
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3):
    forward(225)
    left(120)
end_fill()

# Window 1
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window 1 Cross - Horizontal Line 
penup()
goto(0, 25)
pendown()
color("black")
forward(50)

# Window 1 Cross - Vertical Line 
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

# Window 2
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Window 2 Cross - Horizontal Line 
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

# Window 2 Cross - Vertical Line 
penup()
goto(-55, 0)
pendown()
left(90)
forward(50)

# Door
penup()
goto(-40, -97)
pendown()
right(90)
color("gray")
begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

# Door Handle
penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

hideturtle()
exitonclick()