import pandas as pd

class SourceCsv:
    
    filepath: str | None = None
    delimiter: str = ','
    header: int = 0

    def __init__(self):
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.filepath, sep=self.delimiter, header=self.header)