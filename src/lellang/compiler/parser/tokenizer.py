from lellang.globals import log

class Tokenizer:

    def __init__(self, processed) -> None:
        self.processed =processed
    
    def tokenize(self) -> dict:

        tokens = {}
        line_index = 0

        return tokens