Scientific supplement: Sharp positivity orders for reduction maps on perfect-tensor codes.
Author transcription controls; neither independent referee reports nor formal proofs.
Requires Python 3 and SymPy. From this directory run:
 python werner422-perfect-code-controls.py
 python werner413-h-mub.py
 python output-code-block437.py
 python werner432-rank-controls.py
The third command replays complex-code-gram.py and werner429-ame6-controls.py,
then checks the stronger entire-output-code separation in those same instances.
All scripts use relative files and algebraically constructed inputs; no network,
private audit directory, author session or downloaded paper is required.
422 constructs all polynomial coefficient Grams of dimensions81 and625.
413 first runs412, checking all complex qutrit matrix units and Weyl MUBs.
429 checks the64-dimensional wheel Gram, six parameter coefficients, stars,
nonorthogonal disjoint pair spaces, and all20integer cut determinants.
432 checks scalar rank thresholds and exact large-dimensional witnesses.
437 deliberately reuses author constructions: it is not an independent check.
The universal conclusions come from the analytic proofs, not sample interpolation.
No245^6matrix or proof-assistant certificate is constructed.
JSON outputs and replay records preserve actual executions; timings may vary.
The attempt1/attempt2 source snapshots are intentionally FAILED historical
calculations, not verification commands. Their paired failure summaries explain
the guessed multiplicity error and the symbolic structural-equality error.
The corrected controls assert expanded identities and the actual spectrum.
Known codes, isotropic Schmidt optimization and MUB tools remain prior ingredients.
