import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Logo with Text")

# Set up the turtle
logo_turtle = turtle.Turtle()

# Load the PNG logo
logo_path = "logo.gif"  # Replace with the path to your PNG file
screen.addshape(logo_path)  # Add the logo as a shape
logo_turtle.shape(logo_path)  # Set the turtle's shape to the logo

# Position the logo
logo_turtle.penup()
logo_turtle.goto(0, 10)  # Adjust position if needed

# Add text below the logo
logo_turtle.goto(0, -50)  # Position the turtle below the logo
logo_turtle.color("black")
logo_turtle.write("HELLO MY FRIENDS", align="center", font=("Arial", 16, "bold"))

# Hide the turtle and keep the window open
#logo_turtle.hideturtle()
screen.mainloop()


