import sys
import os
import platform
import click
import numpy as np
from config import STYLES, BIASES, WIDTH


if platform.system == "Windows":
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
else:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')




@click.command()
@click.option('--bias', default=.75, help="The default is .75. That seems to work. Experiment with other numbers, I dunno.")
@click.option('--width', default=1, help="Default is 1. This is the width of the pen stroke.")
@click.option('--style', default=3, help="This is the various styles of writing. The options are 1 - 9")
@click.argument('input_file')
@click.argument('output_file', default=f"{desktop}/scribble.svg")


def scribble(input_file, output_file, bias, width, style):
    """
        Usage: scribble [OPTIONS] source_file.txt output_file_name.svg

        INPUT_FILE: This is the path to the text file with the message you want to write.
        OUTPUT_FILE: This is the path where you want to write the SVG file.
    """
    from handwriting_synthesis import Hand
    hand = Hand()
    file = open(input_file, 'r')

    raw_text = ""
    for l in file.readlines():
        raw_text += l

    lines = raw_text.split("\n")

# usage demo
    biases = [bias for i in lines]
    styles = [style for i in lines]
    stroke_colors = ['black' for i in lines]
    stroke_widths = [width for i in lines]

    hand.write(
        filename=output_file,
        lines=lines,
        biases=biases,
        styles=styles,
        stroke_colors=stroke_colors,
        stroke_widths=stroke_widths
    )
    file.close()







if __name__ == '__main__':
    scribble()


