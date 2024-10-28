from servier.lib.io.json import TargetJson


class References(TargetJson):
    filepath: str = "outputs/references.json"

    def load(self, relationships):
        self.data = (
            relationships.data.groupby(["atccode", "drug"])
            .apply(
                lambda row: row[["reference_id", "reference_type", "date"]].to_dict(
                    "records"
                )
            )
            .reset_index()
            .rename(columns={0: "references"})
        )
