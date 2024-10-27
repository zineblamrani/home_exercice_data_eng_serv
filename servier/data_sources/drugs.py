from servier.lib.data_sources.csv import SourceCsv


class Drugs(SourceCsv):
    filepath: str = "docs/drugs.csv"