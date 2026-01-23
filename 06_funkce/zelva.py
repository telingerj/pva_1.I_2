import turtle

turtle.Turtle()
turtle.shape("turtle")

"""
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
"""
turtle.width(5)


n = 100
for i in range(n):
    if i % 2 == 0:
        turtle.color("red")
    else:
        turtle.color("blue")
    turtle.forward(1000 / n)
    turtle.left(360 / n)

turtle.done()

# hranatá sprirála
