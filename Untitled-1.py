import turtle


def draw_heart():
    # Setup screen
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Heart")

    # Setup turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(3)
    t.color("red", "pink")  # Outline red, fill pink

    # Draw heart shape
    t.penup()
    t.goto(0, -150)
    t.pendown()

    t.begin_fill()
    t.left(140)
    t.forward(180)

    # Left curve
    t.circle(-90, 200)

    # Right curve
    t.left(120)
    t.circle(-90, 200)

    t.forward(180)
    t.end_fill()

    # Write text in center
    t.penup()
    t.goto(0, -20)
    t.color("white")
    t.write("For You", align="center", font=("Arial", 20, "bold"))

    screen.mainloop()


if __name__ == "__main__":
    draw_heart()