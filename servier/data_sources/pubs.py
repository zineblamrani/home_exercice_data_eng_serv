from servier.lib.io.csv import SourceCsv


class Pubs(SourceCsv):
    filepath: str = "docs/pubmed.csv"
    date_columns: list[str] = ["date"]
