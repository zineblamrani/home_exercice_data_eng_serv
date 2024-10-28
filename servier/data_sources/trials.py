from servier.lib.io.csv import SourceCsv

class Trials(SourceCsv):
    filepath: str = "docs/clinical_trials.csv"
    date_columns: list[str] = ["date"]