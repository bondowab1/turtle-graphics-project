import turtle

# Create screen and turtle
screen = turtle.Screen()
screen.title("Draw a Star")
pen = turtle.Turtle()

# Draw a star (5 pointed)
for i in range(5):
    pen.forward(100)
    pen.right(144)

turtle.done()