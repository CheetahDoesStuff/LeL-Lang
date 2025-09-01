from lellang.globals import globals
from lellang.compiler.compiler import Compiler
import argparse


def handle_args() -> list:
    return []


def edit_settings(args: list) -> None:
    pass


def main():

    args = handle_args()
    edit_settings(args)

    compiler = Compiler()
    compiler.run()