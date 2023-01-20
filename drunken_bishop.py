#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Imports.
from typing import Optional
import hashlib, secrets
import sys, os, argparse


# • ── Utils: Clear.
def clear():
    match sys.platform:
        case "win32":
            os.system("cls")
        case "linus" | "darwin":
            os.system("clear")
        case _:
            raise Exception("Unidentified Operating System.")


# • ── Drunken Bishop.
class DrunkenBishop:
    def __init__(self, fingerprint: Optional[str] = None) -> None:
        # Input.
        self.fingerprint = fingerprint or self.random_fingerprint()

        # Board Size.
        self.WIDTH = 17 # 0..16
        self.HEIGHT = 9 # 0..8

        # Positions.
        self.START_POSITION = (8, 4)
        self.position = self.START_POSITION

        # Symbols.
        self.SYMBOLS = " .o+=*BOX@%&#/^"
        self.START_SYMBOL, self.END_SYMBOL = "S", "E"

        # Bishop's Moves (x, y).
        self.MOVE = {
            "00": (-1, -1),  # ↖
            "01": (+1, -1),  # ↗
            "10": (-1, +1),  # ↙
            "11": (+1, +1),  # ↘
        }

    # * ── Create a Random Fingerprint.
    def random_fingerprint(self) -> str:
        string = secrets.token_urlsafe(16).encode("utf-8")
        hash_obj = hashlib.md5(string).hexdigest()

        fingerprint = []
        for index in range(0, len(hash_obj), 2):
            fingerprint.append(hash_obj[index] + hash_obj[index + 1])

        return ":".join(fingerprint)

    # * ── HEX to Binary.
    def hex_to_binary(self, item: str) -> str:
        decimal = int(item, 16)
        return bin(decimal)[2:].zfill(8)

    # * ── Bit Pairs (x, y).
    def bit_pairs(self, bits: str) -> str:
        for x, y in zip(bits[::2], bits[1::2]):
            yield f"{x}{y}"

    # * ── Define Position (Current + Delta).
    def get_position(self, direction: str) -> tuple[int, int]:
        delta_x, delta_y = self.MOVE[direction]
        position_x, position_y = self.position

        position_x = max(0, min((position_x + delta_x), self.WIDTH - 1))  # Clamp | Bound by board.
        position_y = max(0, min((position_y + delta_y), self.HEIGHT - 1))  # Clamp | Bound by board.

        return position_x, position_y

    # * ── Draw.
    def draw_board(self, counter: dict, show_end_symbol: bool = False) -> str:
        board = []

        # Draw Top Border.
        y_border = "+" + "-" * (self.WIDTH) + "+"
        board.append(y_border + "\n")

        # Draw Rows.
        for y in range(self.HEIGHT):
            row = "|"  # Left Border.

            for x in range(self.WIDTH):

                # Bishop's Path.
                coins = counter.get((x, y), 0)
                symbol = self.SYMBOLS[coins]

                # Bishop's Start.
                if (x, y) == self.START_POSITION:
                    symbol = self.START_SYMBOL

                # Last Bishop's Move.
                elif (x, y) == self.position and show_end_symbol:
                    symbol = self.END_SYMBOL

                row += symbol

            row += "|\n"  # Right Border.
            board.extend(row)

        # Draw Bottom Border.
        board.append(y_border)
        return "".join(board)

    # * ── Run.
    def run(self, print_board=True) -> str:
        counter = {}

        for index, item in enumerate((items := self.fingerprint.split(":"))):
            binary = self.hex_to_binary(item)

            # Reversed(list(...)) -> little endian.
            for direction in reversed(list(self.bit_pairs(binary))):
                self.position = self.get_position(direction)

                # Bishop placing coins on the field along his way.
                count = counter.setdefault(self.position, 0)
                counter[self.position] = count + 1

                # Draw Board.
                end_symbol = index == len(items) - 1
                result = self.draw_board(counter, show_end_symbol=end_symbol)

                # Print Board.
                if print_board:
                    # fmt:off
                    clear(); print(result) # fmt: on

        return result


# • ── Main.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="drunken bishop visualization.")
    parser.add_argument("-f", "--fingerprint", type=str, help="Public key fingerprint.")
    parser.add_argument("-i", "--iterations", type=int, default=1, help="No. of iterations (max=10).")
    args = parser.parse_args()

    for _ in range(min(args.iterations, 10)):
        bishop = DrunkenBishop(args.fingerprint)
        bishop.run()


