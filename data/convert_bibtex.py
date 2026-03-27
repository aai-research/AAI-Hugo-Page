import bibtexparser
import json

with open("data/publications.bib") as bib_file:
    bib_database = bibtexparser.load(bib_file)

with open("data/publications.json", "w") as json_file:
    json.dump(bib_database.entries, json_file, indent=2)