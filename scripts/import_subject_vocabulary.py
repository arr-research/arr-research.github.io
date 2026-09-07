# SPDX-License-Identifier: AGPL-3.0-or-later
"""Import a reviewed local EuroSciVoc SKOS-XL snapshot; not run at build time.

Requires rdflib only for vocabulary maintenance. See docs/SUBJECT_TAXONOMY.md.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    from rdflib import Graph, Namespace, OWL, RDF, SKOS

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--source-url", required=True)
    parser.add_argument("--output", type=Path, default=Path("registry/euroscivoc.json"))
    args = parser.parse_args()
    graph = Graph().parse(args.source, format="turtle")
    xl = Namespace("http://www.w3.org/2008/05/skos-xl#")
    scheme = next(graph.subjects(RDF.type, SKOS.ConceptScheme))
    concepts = {c for c in graph.subjects(RDF.type, SKOS.Concept)
                if str(graph.value(c, OWL.deprecated)) != "true"}

    def identifier(concept):
        return "eu-" + str(concept).rsplit("/", 1)[-1]

    terms = []
    for concept in concepts:
        labels = {str(label.language): str(label).strip() for node in graph.objects(concept, xl.prefLabel)
                  for label in graph.objects(node, xl.literalForm)}
        aliases = sorted({str(label).strip() for node in graph.objects(concept, xl.altLabel)
                          for label in graph.objects(node, xl.literalForm)})
        parents = list(graph.objects(concept, SKOS.broader))
        if len(parents) > 1 or any(p not in concepts for p in parents) or not labels.get("en"):
            raise ValueError(f"Review hierarchy/labels before importing {concept}")
        terms.append({"id": identifier(concept), "label": labels["en"][:1].upper() + labels["en"][1:],
                      "parent": identifier(parents[0]) if parents else None,
                      "labels": labels, "aliases": aliases, "uri": str(concept)})
    output = {"source": "EuroSciVoc", "source_version": str(graph.value(scheme, OWL.versionInfo)),
              "publisher": "Publications Office of the European Union",
              "source_url": args.source_url, "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
              "license": "CC-BY-4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
              "license_evidence": "https://data.europa.eu/api/hub/search/datasets/euroscivoc-the-european-science-vocabulary",
              "changes": "Active concepts only; labels and aliases flattened from SKOS-XL and trimmed; English initial capitalised; stable URI-derived identifiers.",
              "terms": sorted(terms, key=lambda t: t["id"])}
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(terms)} active terms from EuroSciVoc {output['source_version']}")


if __name__ == "__main__":
    main()
