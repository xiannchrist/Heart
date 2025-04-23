import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle for heart
pen = turtle.Turtle()
pen.color("red")
pen.pensize(4)
pen.speed(1)

# Draw the heart
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()
pen.hideturtle()

# Create turtle for main text
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, -100)
text.color("red")
text.write("I LOVE YOU LOVE", align="center", font=("Arial", 20, "bold"))

# Smaller font for "from: Christian"
text.goto(0, -130)
text.write("from: Christian", align="center", font=("Arial", 12, "normal"))

# Keep the window open until clicked
screen.exitonclick()
