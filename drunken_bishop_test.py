#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Imports.
from drunken_bishop import DrunkenBishop
from pathlib import Path
import unittest


# • ── Input Test Data.
HEX_BINARY_SAMPLE = [("fc", "11111100"), ("6C", "01101100"), ("a1", "10100001")]
POSITIONS_SAMPLE = [("00", (7, 3)), ("01", (9, 3)), ("10", (7, 5)), ("11", (9, 5))]
WALL_SAMPLE = ["01" for _ in range(10)]
BASE_DIR = Path(__file__).resolve().parent


# • ── Test Drunken Bishop
class TestDrunkenBishop(unittest.TestCase):

    # * ── Test Hex to Binary.
    def test_hex_to_binary(self):
        bishop = DrunkenBishop()

        for hex_input, result in HEX_BINARY_SAMPLE:
            self.assertEqual(result, bishop.hex_to_binary(hex_input))

    # * ── Test Movement.
    def test_positions(self):
        for direction_input, result in POSITIONS_SAMPLE:
            bishop = DrunkenBishop()
            self.assertEqual(result, bishop.get_position(direction_input))

    # * ── Test Wall Boundary.
    def test_wall_boundary(self):
        bishop = DrunkenBishop()

        for direction_input in WALL_SAMPLE:
            bishop.position = bishop.get_position(direction_input)

        self.assertEqual(bishop.position, (16, 0))

    # * ── Test Drawing.
    def test_drawing(self):
        for sample in BASE_DIR.joinpath("tests").iterdir():
            if sample.is_file() and sample.suffix == ".txt":

                # Create Drawing.
                bishop = DrunkenBishop(sample.stem)
                result = bishop.run(print_board=False)

                # Compare Results.
                with open(sample, "r") as f:
                    self.assertEqual(f.read(), result)


if __name__ == "__main__":
    unittest.main()
