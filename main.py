"""
An app that lets the user provide the start coordinates of geometrical
shapes such as squares and rectangles, their dimensions,
and their colors, and the program produces an image file canvas with all
the geometrical shapes drawn in it.
"""
import sys

from canvas import Canvas
from colors import get_colors
from shapes import Square, Rectangle
from validations import (
    validate_canvas_color,
    validate_shape_type,
    validate_coordinates,
    validate_dimensions,
)

if __name__ == "__main__":

    try:
        canvas_colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
        canvas_width = int(input("Enter canvas width: "))
        canvas_height = int(input("Enter canvas height: "))
    except ValueError:
        print("Invalid value specified for canvas dimensions.")
        sys.exit(1)

    while True:
        canvas_color = input("Enter canvas color (white or black): ").lower()
        if not validate_canvas_color(canvas_color):
            print("Invalid canvas color. Please choose one of 'white' or 'black.")
            continue
        break

    canvas = Canvas(
        width=canvas_width, height=canvas_height, color=canvas_colors[canvas_color]
    )

    while True:
        shape_type = input(
            "What would you like to draw (square or rectangle). Enter 'quit' to exit: "
        ).lower()
        if not validate_shape_type(shape_type):
            print(
                "Invalid shape type. Please choose one of 'square' or 'rectangle'.",
                "Enter 'quit' to exit.",
            )
            continue

        if shape_type == "quit":
            break

        if shape_type == "square":
            try:
                sqr_x = int(input("Enter the x coordinate of the square: "))
                sqr_y = int(input("Enter the y coordinate of the square: "))
                validate_coordinates(sqr_x, sqr_y)
            except ValueError:
                print(
                    "Invalid values specified for square coordinates.",
                    "Coordinates must be positive integers.",
                )
                continue

            try:
                sqr_side = int(input("Enter the length of the square side: "))
                validate_dimensions(sqr_side)
            except ValueError:
                print(
                    "Invalid value specified for square side length.",
                    "Length must be a positive integer.",
                )
                continue

            color = get_colors()
            square = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=color)
            square.draw(canvas)

        if shape_type == "rectangle":
            try:
                rec_x = int(input("Enter the x coordinate of the rectangle: "))
                rec_y = int(input("Enter the y coordinate of the rectangle: "))
                validate_coordinates(rec_x, rec_y)
            except ValueError:
                print("Invalid value specified for rectangle coordinates.")
                continue

            try:
                rec_width = int(input("Enter the width of the rectangle: "))
                rec_height = int(input("Enter the height of the rectangle: "))
                validate_dimensions(rec_width, rec_height)
            except ValueError:
                print(
                    "Invalid value specified for rectangle dimensions.",
                    "Dimensions must be positive integers.",
                )
                continue

            color = get_colors()
            rectangle = Rectangle(
                x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=color
            )
            rectangle.draw(canvas)

    canvas.create("canvas.png")
