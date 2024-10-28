import pandas as pd
from dateutil.parser import parse as parse_date


class SourceCsv:

    filepath: str | None = None
    delimiter: str = ","
    header: int = 0
    date_columns: list[str] = []
    date_parser: callable = parse_date

    def __init__(self):
        self.data = None

    def load(self):
        self.data = pd.read_csv(
            self.filepath,
            sep=self.delimiter,
            header=self.header,
            parse_dates=self.date_columns,
            date_parser=parse_date,
        )
