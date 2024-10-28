import pandas as pd
from dateutil.parser import parse as parse_date


class TargetJson:

    filepath: str | None = None
    date_format: str = "iso"

    def __init__(self):
        self.data = None

    def write(self):
        self.data.to_json(self.filepath, orient="records", date_format=self.date_format)
