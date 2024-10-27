from servier.lib.data_sources.csv import SourceCsv


class Pubs(SourceCsv):
    filepath: str = "docs/pubmed.csv"