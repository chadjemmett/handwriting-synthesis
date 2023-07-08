import sys
import click
from config import STYLES, BIASES, WIDTH

if len(sys.argv) < 3:
    print("Usage: python main.py <path/to/text/file.txt> img/<name of output file>.svg")
else:
    import numpy as np
    from handwriting_synthesis import Hand

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    file = open(input_file, 'r')

    raw_text = ""
    for l in file.readlines():
        raw_text += l

    lines = raw_text.split("\n")

    if __name__ == '__main__':
        hand = Hand()

    # usage demo
        biases = [BIASES for i in lines]
        styles = [STYLES for i in lines]
        stroke_colors = ['black' for i in lines]
        stroke_widths = [WIDTH for i in lines]

        hand.write(
            filename=f'img/{output_file}',
            lines=lines,
            biases=biases,
            styles=styles,
            stroke_colors=stroke_colors,
            stroke_widths=stroke_widths
        )
    file.close()
