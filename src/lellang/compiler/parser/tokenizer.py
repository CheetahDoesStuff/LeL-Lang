from lellang.globals import log

class Tokenizer:

    def __init__(self, processed) -> None:
        self.processed =processed
    
    def tokenize(self) -> dict:

        for line in self.processed:
            #log.info(line)
            pass