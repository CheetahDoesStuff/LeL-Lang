from lellang.globals import log, exit
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
            if not cmd_token in vars(TOKENS).values():
                log.error(f"[Tokenizer] Error: Unexpected Token: {cmd_token}")
            
            line_token_struct = {}
            if cmd_token == TOKENS.var_dec:
                line_struct = line[3:].split("=")
                

            
            tokens.append(line_token_struct)
            line_index += 1

            

        return tokens