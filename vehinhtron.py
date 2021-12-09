import turtle
import math
r = int(input("Enter the radius: "))

# ve hinh tron
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)
t.color("Blue")
t.fillcolor("brown")
t.begin_fill()
t.circle(r)
t.end_fill()
turtle.exitonclick()

# Tinh dien tich va chu vi hinh tron
c = 2*math.pi*r
s = r**2*math.pi

print("Chu vi của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
print("Diện tích của hình tròn có bán kính = {r} là {s}".format(r=r, s=s))
