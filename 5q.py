import turtle

length = int(input("Enter the length: "))
color_ = input("Enter the color: ")
tur = turtle.Turtle()

for i in range(4):
    tur.color(color_)
    tur.forward(length)
    tur.right(90)

turtle.done()


