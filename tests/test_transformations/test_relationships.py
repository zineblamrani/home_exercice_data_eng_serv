from servier.transformations.relationships import Relationships
import pandas as pd


def test_relationships():

    relationships = Relationships()

    class Drugs:
        data = pd.DataFrame([{"atccode": "d1", "drug": "DOLIPRANE"}])

    class Trials:
        data = pd.DataFrame(
            [
                {
                    "id": "t1",
                    "scientific_title": "usage of Doliprane for senior",
                    "date": "22/06/2023",
                    "journal": "nature",
                }
            ]
        )

    class Pubs:
        data = pd.DataFrame(
            [
                {
                    "id": "p1",
                    "title": "usage of Doliprane for babies",
                    "date": "25/07/2023",
                    "journal": "university of paris",
                }
            ]
        )

    drugs = Drugs()
    pubs = Pubs()
    trials = Trials()
    relationships.load(drugs, pubs, trials)

    assert list(relationships.data.columns) == [
        "atccode",
        "drug",
        "reference_id",
        "reference_type",
        "date",
    ]
    assert (relationships.data["reference_type"] == "pub").sum() == 1
    assert (relationships.data["reference_type"] == "trial").sum() == 1
    assert (relationships.data["reference_type"] == "journal").sum() == 2
