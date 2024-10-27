from servier.lib.data_sources.csv import SourceCsv


class Trials(SourceCsv):
    filepath: str = "docs/clinical_trials.csv"