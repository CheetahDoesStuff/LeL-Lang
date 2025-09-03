from lellang.compiler.parser.parser import Parser

class Compiler:

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        
        parser = Parser()
        ast = parser.parse()