import lellang.globals as g
from lellang.compiler.compiler import Compiler
import argparse


def handle_args():
    parser = argparse.ArgumentParser(description="LeLlang Compiler Command - Used To Compile LeL to BEANS")

    parser.add_argument("file", help="The Path To The LeL File", type=str)
    parser.add_argument("-o", "--output", help="The Path Of The Output File", default=None, type=str)

    return parser.parse_args()


def edit_settings(args) -> None:
    g.file_path = args.file

    if args.output and args.output.endswith(".bean"):
        g.output_path = args.output

    elif args.output:
        g.log.error(f"[Argument Handler] Invalid Output file: Doesnt end with .bean")
        g.exit()

    else:
        g.output_path = args.file[:-4] + ".bean"

    
    g.log.info("[Argument Handler] -------- Specified Arguments --------")
    g.log.info(f"[Argument Handler] -  Input File: {g.file_path}")
    g.log.info(f"[Argument Handler] -  Output File: {g.output_path}")
    g.log.info("[Argument Handler] -------------------------------------")


def main():

    args = handle_args()
    edit_settings(args)

    compiler = Compiler()
    compiler.run()