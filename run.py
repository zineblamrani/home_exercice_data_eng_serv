from servier.data_sources.drugs import Drugs
from servier.data_sources.pubs import Pubs
from servier.data_sources.trials import Trials
from servier.data_targets.references import References
from servier.transformations.relationships import Relationships


def run_pipeline():
    drugs = Drugs()
    drugs.load()

    pubs = Pubs()
    pubs.load()

    trials = Trials()
    trials.load()

    relationships = Relationships()
    relationships.load(drugs, pubs, trials)

    references = References()
    references.load(relationships)
    references.write()


if __name__ == "__main__":
    run_pipeline()
