from servier.data_sources.drugs import Drugs
from servier.data_sources.pubs import Pubs
from servier.data_sources.trials import Trials
from servier.transformations.references import References

drugs = Drugs()
drugs.load()
print(f"{drugs.data[:10]}")

pubs = Pubs()
pubs.load()
print(f"{pubs.data[:10]}")

trials = Trials()
trials.load()
print(f"{trials.data[:10]}")

references = References()
references.load(drugs, pubs, trials)