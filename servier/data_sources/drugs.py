from servier.lib.io.csv import SourceCsv


class Drugs(SourceCsv):
    filepath: str = "docs/drugs.csv"