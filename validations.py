"""Helper functions to validate user inputs"""


def validate_canvas_color(col):
    """Validate the canvas color"""
    if col not in ["white", "black"]:
        return False
    return True


def validate_shape_type(shape):
    """Validate the chosen shape"""
    if shape not in ["square", "rectangle", "quit"]:
        return False
    return True


def validate_shape_colors(rgb):
    """Validate the colors fall in the correct RGB range"""
    for value in rgb:
        if value not in list(range(0, 256)):
            return False
    return True


def validate_coordinates(x, y):
    """Ensure coordinates are positive integers"""
    if x <= 0 or y <= 0:
        raise ValueError


def validate_dimensions(*args):
    """Ensure dimensions are positive integers"""
    for value in args:
        if value <= 0:
            raise ValueError
