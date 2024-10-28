from collections import defaultdict
import json


def run_query_journal_max_relationships():
    # load data
    with open("outputs/references.json", "r") as jsonfile:
        data = json.load(jsonfile)

    # set of drugs by journal
    drugs_by_journal = defaultdict(set)
    for item in data:
        for reference in item["references"]:
            if reference["reference_type"] == "journal":
                drugs_by_journal[reference["reference_id"]].add(item["drug"])

    # sort and print
    journal_by_max_relationships = sorted(
        drugs_by_journal.items(), key=lambda item: len(item[1]), reverse=True
    )
    print(journal_by_max_relationships[0])


if __name__ == "__main__":
    run_query_journal_max_relationships()
