"""Define a Canvas"""
import numpy as np
from PIL import Image


class Canvas:
    """The canvas on which to draw shapes"""

    def __init__(self, width, height, color) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def create(self, image_path):
        """Create the canvas"""
        img = Image.fromarray(self.data, "RGB")
        img.save(image_path)
