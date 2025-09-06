import lellang.globals as g
from lellang.compiler.compiler import Compiler
import argparse


def handle_args():
    parser = argparse.ArgumentParser(description="LeLlang Compiler Command - Used To Compile LeL to BEANS")

    parser.add_argument("file", help="The Path To The LeL File", type=str)
    parser.add_argument("-o", "--output", help="The Path Of The Output File", default=None, type=str)
    parser.add_argument("-v", "--verbose", help="Logs much more information than normal.", action="store_true")

    return parser.parse_args()


def edit_settings(args) -> None:

    g.log.info(f"Logs are saved at {g.log_dir} - Logs are not automatically cleared.")

    if args.file.endswith(".lel"):
        g.file_path = args.file
    else:
        g.log.error("[Argument Handler] Invalid Input file: Doesnt end with .lel")
        g.exit()


    if args.output and args.output.endswith(".bean"):
        g.output_path = args.output
    elif args.output:
        g.log.error("[Argument Handler] Invalid Output file: Doesnt end with .bean")
        g.exit()
    else:
        g.output_path = args.file[:-4] + ".bean"

    
    g.verbose = args.verbose

    
    g.log.info("[Argument Handler] -------- Specified Arguments --------")
    g.log.info(f"[Argument Handler] -  Input File: {g.file_path}")
    g.log.info(f"[Argument Handler] -  Output File: {g.output_path}")
    g.log.info(f"[Argument Handler] -  Verbose: {g.verbose}")
    g.log.info("[Argument Handler] -------------------------------------")
    g.log.space()


def main():

    args = handle_args()
    edit_settings(args)

    compiler = Compiler()
    compiler.run()