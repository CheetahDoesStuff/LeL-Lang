class Processor:

    def __init__(self, raw: str) -> None:
        self.raw = raw

    def process(self) -> list:

        processed = self.raw
        processed = processed.replace("\n", "")
        processed = "".join(processed.split())

        processed = processed.split(";")
        return processed