import math
import turtle

color = input("nhap vao mau sac ban can to: ")
w = float(input("Nhập chiều dài hình chữ nhật: "))
h = float(input("Nhập chiều rộng hình chữ nhật: "))

t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.begin_fill()
for i in range(2):
    t.forward(w)
    t.rt(90)
    t.fd(h)
    t.rt(90)
t. end_fill()
turtle.done()

# Tinh chuvi dientich
c = 2 * (w + h)
s = w * h
print("Chu vi của hình chữ nhật (dài = {w}, rộng = {h}) là {c}".format(
    w=w, h=h, c=c))
print("Diện tích của hình chữ nhật (dài = {w}, rộng = {h}) là {s}".format(
    w=w, h=h, s=s))
