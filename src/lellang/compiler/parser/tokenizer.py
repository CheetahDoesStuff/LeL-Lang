from lellang.globals import log
from lellang.compiler.parser.tokens import TOKENS

class Tokenizer:

    def __init__(self, processed: list) -> None:
        self.processed: list = processed
    
    def tokenize(self) -> list:

        tokens = []
        line_index = 0

        while line_index < len(self.processed):

            line = self.processed[line_index]

            cmd_token = line[:3]
            tokens.append(cmd_token)

            line_index += 1

            

        return tokens