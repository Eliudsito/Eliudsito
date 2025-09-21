from turtle import *


color("white")
penup()
goto(-280, 250)
pendown()


speed(20)
bgcolor("lightblue")  # Cambiado de "black" a "lightblue"
h = 0

# Tallo verde
penup()
goto(-12, -80)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

# Pétalos de la flor
penup()
goto(0, 0)
pendown()
for i in range(16):
     for j in range(18):
          color("yellow")
          h+=0.005
          rt(90)
          circle(150-j*6,90)
          lt(90)
          circle(150-j*6,90)
          rt(180)
     circle(40,24)

# Centro de la flor
penup()
goto(-20, 0)
pendown()
color("#8B4513")  # Color café más específico (saddle brown)
begin_fill()
circle(44)
end_fill()
done()