from lellang.compiler.parser.parser import Parser

from lellang.globals import log

class Compiler:

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        
        parser = Parser()
        ast = parser.parse()
        log.raw(str(ast))