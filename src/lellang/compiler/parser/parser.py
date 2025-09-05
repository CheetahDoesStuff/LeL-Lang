from lellang.compiler.parser.get_raw import get_raw
from lellang.compiler.parser.processor import Processor

class Parser():
    
    def __init__(self) -> None:
        self.raw = get_raw()


    def parse(self) -> list:
        
        processor = Processor(self.raw)
        return processor.process()