from lellang.compiler.parser.get_raw import get_raw
from lellang.compiler.parser.processor import Processor
from lellang.compiler.parser.tokenizer import Tokenizer

class Parser():
    
    def __init__(self) -> None:
        self.raw = get_raw()


    def parse(self) -> list:
        
        processor = Processor(self.raw)
        processed = processor.process()

        tokenizer = Tokenizer(processed)
        tokens = tokenizer.tokenize()

        return tokens