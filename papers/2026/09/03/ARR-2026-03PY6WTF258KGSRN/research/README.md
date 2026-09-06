# Two-state exact routing — research package

The manuscript is `paper.md`. The accompanying PDF is typeset from that source by the root research workflow. This is an unpublished research draft under Lluis Eriksson's name, pending author feedback.

The principal replay needs Python 3.10 or later and SymPy (tested with 1.14.0):

```text
python verify_two_state.py
```

It writes `two_state_certificate.json` and fails immediately on a false algebraic identity or exact fixture. The checked source returns 95 PASS checks. Hashes of the manuscript and verifier are recorded in that JSON. It verifies symbolic identities and exact realizations, not a general numerical optimizer or a formal proof-assistant development.

The independently written review and its verifier are separate files supplied by the quantum research agent. Run the separate 144-check audit with:

```text
python review/quantum_agent_checks.py
```

It identifies its reviewed source and its own scope. It does not import the constructor's verifier.

`explore_two_state.py` and `exploration.json` preserve conjecture-screening experiments. They additionally need NumPy and SciPy. They optimize a three-parameter family at seven symmetric tables using floating-point polynomial roots and differential evolution. They are not used by the exact replay. In particular, neither the numerical minima nor their tiny positive distances from the boundary `V=d²` are global optimality certificates.

The proven results are complete three-parameter feasibility, a quartic cap certificate, the exact delay-two attainment locus, an explicit positive gap away from that locus, and a strictly improved acute-gap construction. The global optimality of the acute construction and the general asymmetric minimum remain open.

`sources_and_scope.md` and `reading_ledger.json` distinguish inspected source regions, inherited context and bounded external comparisons. No bibliography-priority or human-refereeing claim is made. No publication or contact with third parties occurred in this research cycle.
