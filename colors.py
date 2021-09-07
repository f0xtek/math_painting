"""Handle the colors for the shapes"""
from validations import validate_shape_colors


def get_colors():
    """Get the amounts of red, green and blue for the shape"""
    while True:
        red = int(input("How much red color (0-255)? "))
        green = int(input("How much green color (0-255)? "))
        blue = int(input("How much blue color (0-255)? "))
        if not validate_shape_colors((red, green, blue)):
            print("Invalid color amounts specified!")
            continue
        break
    return red, green, blue
