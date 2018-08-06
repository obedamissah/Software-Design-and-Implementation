#################################################################################
# Author: Obed Amissah
# Purpose: To Gain an understanding of how classes are represented in Python, and how they can interact with each other
######################################################################


from shape import Shape                                     # this imports the Shape class from the shape file
import random                                               # this imports the random library
import turtle                                               # this imports the turtle library


def main():                                                 # this defines the main function
    wn = turtle.Screen()                                    # this creates a turtle window
    wn.colormode(255)                                       # this changes the color mode to RGB


    square = Shape([0, 0], 4, 50)                           # this draws a square of length 50
    square.draw_shape()                                     # this calls the draw_square method from the Shape class to draw the specified shape
    triangle = Shape([0, 0], 3, 50)                         # this draws a triangle of length 50
    triangle.draw_shape()                                   # this calls the draw_square method from the Shape class to draw the specified shape
    square = Shape([0, 0], 4, 80)                           # this draws a square of length 80
    square.draw_shape()                                     # this calls the draw_square method from the Shape class to draw the specified shape
    oct = Shape([0, 0], 8, 50)                              # this draws an octagon of length 50
    oct.draw_shape()                                        # this calls the draw_square method from the Shape class to draw the specified shape
    square = Shape([0, 0], 4, 100)                          # this draws a square of length 100
    square.draw_shape()                                     # this calls the draw_square method from the Shape class to draw the specified shape


    wn.exitonclick()                                        # this exits the turtle window when it is clicked

main()                                                      # this calls the main function