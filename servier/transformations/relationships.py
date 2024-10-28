from servier.lib.text import tokenize_unique
import pandas as pd


class Relationships:
    def __init__(self):
        self.data = None

    def load(self, drugs, pubs, trials):

        df_pubs = self._preprocess_pubs(pubs)
        df_trials = self._preprocess_trials(trials)
        df_journals = self._create_df_journals(df_pubs, df_trials)

        df_drugs_pubs = self._relationship_drug_pubs(drugs.data, df_pubs)
        df_drugs_trials = self._relationship_drug_trials(drugs.data, df_trials)
        df_drugs_journals = self._relationship_drug_journals(drugs.data, df_journals)

        self.data = pd.concat(
            [df_drugs_pubs, df_drugs_trials, df_drugs_journals], axis=0
        )

    def _preprocess_pubs(self, pubs):
        df_pubs = pubs.data.copy().rename(columns={"id": "reference_id"})
        df_pubs["reference_type"] = "pub"
        df_pubs["title_tokens"] = tokenize_unique(df_pubs["title"])
        df_pubs = df_pubs.drop(columns=["title"]).explode("title_tokens")
        return df_pubs

    def _preprocess_trials(self, trials):
        df_trials = trials.data.copy().rename(columns={"id": "reference_id"})
        df_trials["reference_type"] = "trial"
        df_trials["scientific_title_tokens"] = tokenize_unique(
            df_trials["scientific_title"]
        )
        df_trials = df_trials.drop(columns=["scientific_title"]).explode(
            "scientific_title_tokens"
        )
        return df_trials

    def _relationship_drug_pubs(self, df_drugs, df_pubs):
        result = df_drugs.merge(
            df_pubs[["reference_id", "reference_type", "title_tokens", "date"]],
            how="inner",
            left_on="drug",
            right_on="title_tokens",
        ).drop(columns=["title_tokens"])
        return result

    def _relationship_drug_trials(self, df_drugs, df_trials):
        result = df_drugs.merge(
            df_trials[
                ["reference_id", "reference_type", "scientific_title_tokens", "date"]
            ],
            how="inner",
            left_on="drug",
            right_on="scientific_title_tokens",
        ).drop(columns=["scientific_title_tokens"])
        return result

    def _create_df_journals(self, df_pubs, df_trials):
        df_journals_pubs = (
            df_pubs.copy()
            .drop(columns=["reference_id"])
            .rename(columns={"journal": "reference_id", "title_tokens": "tokens"})
        )
        df_journals_pubs["reference_type"] = "journal"

        df_journals_trials = (
            df_trials.copy()
            .drop(columns=["reference_id"])
            .rename(
                columns={"journal": "reference_id", "scientific_title_tokens": "tokens"}
            )
        )
        df_journals_trials["reference_type"] = "journal"

        df_journals = pd.concat(
            [df_journals_pubs, df_journals_trials], axis=0
        ).drop_duplicates()
        return df_journals

    def _relationship_drug_journals(self, df_drugs, df_journals):
        result = df_drugs.merge(
            df_journals[["reference_id", "reference_type", "tokens", "date"]],
            how="inner",
            left_on="drug",
            right_on="tokens",
        ).drop(columns=["tokens"])
        return result
