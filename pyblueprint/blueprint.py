"""
This is the module of pyblueprint
"""
import svgwrite
import svgwrite.text
import svgwrite.shapes


class Palette:
    def __init__(self):
        self.text_color = 'blue'


class BluePrint:
    def __init__(self, filename: str):
        self.dwg = svgwrite.Drawing(filename=filename)
        self.palette = Palette()

    def background(self):
        self.dwg.add(svgwrite.shapes.Rect())

    def text(self, text: str, color: str = None) -> None:
        if color is None:
            color = self.palette.text_color
        self.dwg.add(svgwrite.text.Text(text=text, color=color))

    def rectangle(self) -> None:
        self.dwg.add(svgwrite.shapes.Rect())

    def square(self) -> None:
        self.dwg.add(svgwrite.shapes.Rect())

    def save(self) -> None:
        self.dwg.save()
