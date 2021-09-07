"""Define the shape objects to be drawn"""


class Square:
    """An object that represents a Square"""

    def __init__(self, x, y, color, side) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.side = side

    def draw(self, canvas):
        """Draw the shape on the canvas"""
        canvas.data[
            self.x : self.x + self.side, self.y : self.y + self.side
        ] = self.color


class Rectangle:
    """An object that represents a Rectangle"""

    def __init__(self, x, y, color, width, height) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self, canvas):
        """Draw the shape on the canvas"""
        canvas.data[
            self.x : self.x + self.width, self.y : self.y + self.height
        ] = self.color
