import re

class Processor:
    def __init__(self, raw: str) -> None:
        self.raw = raw

    def process(self) -> list:
        processed = self.raw
        processed = re.sub(r'//.*', '', processed)

        parts = processed.split(";")
        parts = ["".join(p.split()) for p in parts]
        parts = [p for p in parts if p]

        return parts
