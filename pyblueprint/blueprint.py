"""
This is the module of pyblueprint
"""
import svgwrite
import svgwrite.text
import svgwrite.shapes


class BluePrint:
    def __init__(self, filename: str):
        self.dwg = svgwrite.Drawing(filename=filename)

    def text(self, text: str):
        self.dwg.add(svgwrite.text.Text(text=text))

    def square(self):
        self.dwg.add(svgwrite.shapes.Rect())

    def save(self) -> None:
        self.dwg.save()
