from lellang.globals import log

class Tokenizer:

    def __init__(self, processed: list) -> None:
        self.processed =processed
    
    def tokenize(self) -> dict:

        tokens = {}
        line_index = 0

        for i in range(len(self.processed)):

            line = self.processed[line_index]

            

        return tokens