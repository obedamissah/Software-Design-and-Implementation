#################################################################################
# Driver: Marima Andrew Mambondiumwe
# Navigator: Emmanuel Acheampong
# Assignment: T17- Class Collaborations
# Purpose: To Gain an understanding of how classes are represented in Python, and how they can interact with each other
######################################################################
# Acknowledgements:
# Dr Jan Pearce
# Dr Scott Heggens-crazy_rectangles.py
# point_v2.py
# rectangle.py

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
##################################################################################

import turtle                                               # this imports the turtle library

class Shape:
    """a class to manufacture any shape with given number of sides and the position """

    def __init__(self, posn, nsides, slen):
        """this initializes shape at posn with ,number of sides, and length"""

        self.start_point = posn                            # start_point is set at (0,0)
        self.num_sides = nsides
        self.slength = slen
        self.turtle = turtle.Turtle()                      # a Turtle object of the turtle class is created

    def draw_shape(self):
        """this draws a shape using a turtle,using number of sides,length and angle """
        angle = 360 // self.num_sides                      # this gives the angles of the shape to be drawn
        x = self.start_point[0]                            # this initializes the start point to x=0
        y = self.start_point[1]                            # this initializes the start point to y=0
        self.turtle.penup()
        self.turtle.goto(x, y)                             # this moves the turtle so that it starts drawing at that particular point
        self.turtle.left(angle)
        self.turtle.showturtle()
        self.turtle.pendown()

        for i in range(self.num_sides):                     # uses a to turtle to use number of sides to draw an appropriate shape
            self.turtle.forward(self.slength)
            self.turtle.left(angle)

        for i in range(self.num_sides):                     # uses a turtle to use number of sides to draw an appropriate shape in the opposite direction
            self.turtle.forward(self.slength)
            self.turtle.right(angle)







