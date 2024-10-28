from servier.transformations.relationships import Relationships
import pandas as pd


def test_relationships():

    relationships = Relationships()

    class Drug:
        data = pd.DataFrame()

    class Trials:
        data = pd.DataFrame()

    class Pubs:
        data = pd.DataFrame()

    relationships.load(drug, pubs, trials)

    assert relationships.data
