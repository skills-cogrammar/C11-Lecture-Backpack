"""
One of the coolest and most visually appealing examples of recursion is 
generating a Fractal, particularly the Sierpinski Triangle. 
Fractals are patterns that repeat at every scale, and recursion 
is the perfect tool to create them because each pattern is self-similar.

Here's how you can create a simple Sierpinski Triangle using 
recursion with Python and the turtle graphics library:
"""

import turtle


def draw_triangle(points, color, my_turtle):
    """Draws a filled triangle using the three points."""
    my_turtle.fillcolor(color)
    my_turtle.penup()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_mid(p1, p2):
    """Returns the midpoint between two points."""
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


def sierpinski(points, degree, my_turtle):
    """Recursively draws the Sierpinski triangle."""
    # Color selection based on the recursion depth
    colors = ['blue', 'red', 'green', 'yellow', 'violet', 'orange']
    draw_triangle(points, colors[degree], my_turtle)

    if degree > 0:
        # Calculate the midpoints of the triangle's sides
        mid1 = get_mid(points[0], points[1])
        mid2 = get_mid(points[1], points[2])
        mid3 = get_mid(points[2], points[0])

        # Recursively draw smaller triangles
        sierpinski([points[0], mid1, mid3], degree - 1, my_turtle)
        sierpinski([points[1], mid1, mid2], degree - 1, my_turtle)
        sierpinski([points[2], mid2, mid3], degree - 1, my_turtle)


# Setting up the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
screen = turtle.Screen()

# Initial triangle points and recursion depth
initial_points = [[-200, -100], [0, 200], [200, -100]]
depth = 4  # You can change the depth to see different levels of detail

# Start the recursive Sierpinski triangle drawing
sierpinski(initial_points, depth, my_turtle)

# Keep the window open
screen.mainloop()
