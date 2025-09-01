import lellang.globals as g
from lellang.compiler.compiler import Compiler
import argparse


def handle_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="The Path To The LeL File")

    return parser.parse_args()


def edit_settings(args) -> None:
    g.file_path = args.file


def main():

    args = handle_args()
    edit_settings(args)

    compiler = Compiler()
    compiler.run()