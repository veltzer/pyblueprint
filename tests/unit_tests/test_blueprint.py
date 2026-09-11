"""Behavioural tests for pyblueprint's drawing wrapper."""

import os
import tempfile
import unittest

from pyblueprint.blueprint import BluePrint, Palette


class PaletteTests(unittest.TestCase):
    def test_default_text_color(self):
        self.assertEqual(Palette().text_color, "blue")


class BluePrintTests(unittest.TestCase):
    def test_each_shape_adds_one_element(self):
        bp = BluePrint()
        start = len(bp.dwg.elements)
        bp.rectangle()
        bp.square()
        bp.background()
        self.assertEqual(len(bp.dwg.elements), start + 3)

    def test_text_adds_element(self):
        bp = BluePrint()
        start = len(bp.dwg.elements)
        bp.text("hello")
        self.assertEqual(len(bp.dwg.elements), start + 1)

    def test_text_defaults_color_to_palette(self):
        bp = BluePrint()
        bp.palette.text_color = "green"
        bp.text("defaulted")
        added = bp.dwg.elements[-1]
        self.assertEqual(added.attribs["color"], "green")

    def test_text_honours_explicit_color(self):
        bp = BluePrint()
        bp.text("explicit", color="red")
        added = bp.dwg.elements[-1]
        self.assertEqual(added.attribs["color"], "red")

    def test_save_writes_svg_file(self):
        bp = BluePrint()
        bp.rectangle()
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "out.svg")
            bp.save(path)
            self.assertTrue(os.path.isfile(path))
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
            self.assertIn("<svg", content)


if __name__ == "__main__":
    unittest.main()
