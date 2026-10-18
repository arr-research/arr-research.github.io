from pathlib import Path
import json,hashlib,shutil,datetime,re,sys
out=Path(__file__).resolve().parent
root=out.parent;base=root.parent
archive=Path(r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-manuscript-4")
assert not archive.exists(),"Frozen archive must never be overwritten."
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
inp=json.loads((out/"input-check.json").read_text(encoding="utf-8"))
for name,record in inp["files"].items():
 assert sha(root/"input"/name)==record["sha256"]
 assert sha(out/"reviewed-inputs"/name)==record["sha256"]
tex=(out/"reviewed-inputs"/"main.tex").read_text(encoding="utf-8")
pdftext=(out/"main-extracted.txt").read_text(encoding="utf-8")
labels=re.findall(r"\\label\{([^}]+)\}",tex)
assert len(labels)==len(set(labels))
refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",tex)
assert set(refs)<=set(labels)
bib=re.findall(r"\\bibitem\{([^}]+)\}",tex)
cites=set()
for c in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}",tex):
 cites.update(x.strip() for x in c.split(","))
assert cites==set(bib)
assert "??" not in pdftext
assert "Schmidt number" not in tex and "1/(e" not in tex
shutil.copy2(root/"prepare_review.py",out/"prepare_review.py")
# Preserve independently inspectable earlier evidence without creating a new independent vote.
evidence=[]
evidence_sources=[
("review-manuscript-3/output/source-register.json","manuscript3-source-register.json"),
("review-reduction-mixed-1/source-register.json","dossiers5-7-source-register.json"),
("review-reduction-mixed-1/dossier-5-review.txt","dossier5-review.txt"),
("review-reduction-mixed-1/dossier-6-review.txt","dossier6-review.txt"),
("review-reduction-mixed-1/dossier-7-review.txt","dossier7-review.txt"),
("review-reduction-mixed-1/verdict.json","dossiers5-7-verdict.json"),
("review-ldoi-1/source-register.json","dossier8-source-register.json"),
("review-ldoi-1/audit-report.txt","dossier8-review.txt"),
("review-ldoi-1/verdict.json","dossier8-verdict.json")
]
for rel,name in evidence_sources:
 src=base/rel;dst=out/"reused-evidence"/name
 shutil.copy2(src,dst)
 evidence.append(dict(source=str(src),copy=str(dst.relative_to(out)),sha256=sha(src)))
visual=dict(status="pass",method="Independent Poppler rendering at 100 dpi; all 15 page images viewed individually.",
 pages_inspected=list(range(1,16)),observations="Legible equations, table and references; no clipping or overlap observed. Normal theorem/proof continuations across page breaks. Table on page 13 checked against all 24 verified roundings.",
 author_compilation_claim="Manifest reports built-in and Tectonic compilation success; not independently recompiled by this reviewer.",
 compiled_by_reviewer=False)
(out/"visual-review.json").write_text(json.dumps(visual,indent=2),encoding="utf-8")
source_register=dict(
 scope="Same reviewer's primary readings from previous exact reviews and dossiers are reused with their stated limits. No claim to have reread every source in full.",
 reused_registers=[
  r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-manuscript-3\source-register.json",
  r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-adaptive-3\source-register.json",
  r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-adaptive-4\source-register.json"],
 finite_core=[
  dict(citation="HH quant-ph/9708015v3",scope="Previously read pertinent IV-VI, especially filtering and positive-yield distillation after reduction violation."),
  dict(citation="Vollbrecht-Wolf quant-ph/0202058",scope="Theorem 2 and proof through (21)-(24), operator-log reduction argument; explicit attribution now correct."),
  dict(citation="HHHO quant-ph/0506189",scope="Section XI Theorem 9 proof and Appendix H; K_D<=E_R^infty with arbitrary shielding/public transcript."),
  dict(citation="Hostens et al. quant-ph/0602205v2; Vollbrecht-Verstraete quant-ph/0404111v2",scope="Nondestructive appended-pair measurement, partition breeding, discarding and removal of assistance; the manuscript proves its extension beyond Bell-diagonal states explicitly."),
  dict(citation="Vollbrecht-Wolf quant-ph/0208152; Maneva-Smolin quant-ph/0003099; Leung-Shor quant-ph/0702156v3",scope="Previously read relevant normalized isotropic and adaptive purification sections; Leung-Shor full four pages. A.W. Leung corrected."),
  dict(citation="Johnston-MacLean arXiv:1807.06897",scope="Previously read relevant Section 5 definition, normal form and Theorem 6. Official journal metadata newly checked."),
  dict(citation="Singh-Nechita arXiv:2010.07898v2 / Quantum 5,519",scope="Definitions 2.1, Propositions 2.2-2.3 and 4.1, forms (5)-(8), relevant conclusion; not all 50 pages."),
  dict(citation="Britz-Laurent arXiv:2512.06551v2",scope="Title, abstract, contents and introduction/support forms; not all 50 pages. May 2026 version; J. Britz correct.")
 ],
 oscillator_dependencies="Wilde-Qi Theorems 1-3; Holevo constrained classical regularization; Holevo-Shirokov Theorem 1; DSW Theorem 4, (101),(141); Devetak-Winter Theorem 10; BBPS; Catalano v2 cited vacuum and fading special cases; Amosov-Mancini Theorem 9. Prior direct readings and hypothesis checks reused, not presumed universal beyond stated conditions.",
 new_metadata_check=dict(url="https://journals.uwyo.edu/index.php/ela/article/download/1961/1961/1961",
 finding="Official ELA title page confirms Nathaniel Johnston, Olivia MacLean, volume 35, pp.156-180, May 2019."),
 new_search_queries=[
 '"entanglement" "separable noise" "irreversibility" pure state bound',
 '"distillation" "diagonal invariant" states',
 '"entanglement distillation" "constant gap" states',
 '"Pairwise completely positive matrices" "156" "2019"'],
 search_limit="Targeted searches and primary readings did not identify a directly matching universal absolute-gap theorem. Absence from these results is not proof of novelty or global priority. No novel primitive, invariant class, logarithmic reduction criterion or vacuum special case is credited to this manuscript.",
 evidence_files=evidence)
(out/"source-register.json").write_text(json.dumps(source_register,indent=2),encoding="utf-8")
claim_audit=[
 ("Lemma 1","Dominated-component positive seed","Support restriction and regularized operator logarithm give log a+u_A+D<=0 under reduction; HH supplies positive rate. No marginal constraint."),
 ("Theorem 2","Universal stopped classification and CLDUI interval","Finite Z3 twirl; fixed A via entropy concavity; parity-projector Kraus; typical binary hashes; survivor MC hashing; seed from actual block and paid reserve. CLDUI reference gives upper v."),
 ("Corollary 3","LDOI log2(9) interval","Known global block spectrum, not a free nonlocal measurement; c<=1-w and separable dephasing reference. No E_C claim."),
 ("Theorem 4","Arbitrary-noise MC recovery and pure/separable irreversibility","Applies classification to actual accepted state; three-branch identity handles all weights; no matching marginal. Cost upper only for pure good component with separable noise."),
 ("Corollaries 5-6","Growing-dimensional absolute bounds","ER convex upper for MC plus separable noise; pure-state cost upper and vanishing h(q)+q log5. No q log d condition needed."),
 ("Corollary 7","All finite identity/EB mixtures","Bell-input lower; channel squashed-entanglement upper with branch/separable extension; covers adaptive Q2/K2 without covariance."),
 ("Theorem 8","Four unrestricted fixed-reset asymptotics","Finite decoded coding and erasure postprocessing avoid entropy hypotheses on physical reset. Absolute gaps and uniformity only on bounded reset-energy sets."),
 ("Lemma 9","Exact diamond distance","Replacement difference has norm 2delta; decoder removes cross-block reset coherences; reference systems included."),
 ("Lemma 10","Hidden-branch loss","Correct CMI chain-rule direction, cq conditional entropy positivity and membership data processing; all registers finite."),
 ("Propositions 11-12","Operational lower and upper rates","Strict energy slack, general operational equivalences, finite decoded/erasure hypotheses; anti-degradability gives Q=P=0 for lambda<=1/2."),
 ("Lemma 13","Shifted truncated geometric input","Exact energy/entropy formulas, positive strict slack, tail and absolute entropy loss."),
 ("Theorem 14","Two-way high-energy reset capacities","Paid seed uses same finite-energy copies; adaptive average-cost erasure upper; fixed tau trace-class tail suffices."),
 ("Corollary 15","Specified distributed-state reversibility","Local decoding lower and random-branch pure dilution upper; countable local preparation permitted for arbitrary tau; no channel-simulation or local energy-cost claim."),
 ("Theorem 16","Uniform finite-partner classical defect","Subset argument with M=Psi^n finite, convex output-entropy roof, constrained regularization; upper independent of partner dimension."),
 ("Corollary 17","Positive Q/P at each N>0 iff lambda>1/2","Time sharing at block-average cost; no peak-energy assertion."),
 ("Corollary 18","Non-EB for any lambda>0","Fixed d=2, tail escape, antisymmetric partial-transpose expectation -lambda/2+delta/4.")
]
claims=[dict(reference=a,claim=b,status="valid_in_stated_scope",basis=c) for a,b,c in claim_audit]
minor=[
 dict(id="M1",severity="optional_editorial",location="Corollary 3 proof, page 4",
 suggestion="Add Proposition 4.1 of Singh-Nechita alongside Proposition 2.2 and (5)-(8), since it states the direct-sum decomposition explicitly.",
 blocking=False),
 dict(id="M2",severity="optional_editorial",location="Theorem 16 proof, page 12",
 suggestion="Point specifically to Proposition 3 of the cited Holevo preprint for constrained classical regularization.",
 blocking=False),
 dict(id="M3",severity="optional_bibliographic",location="References [10], [19], [20]",
 suggestion="Adding published journal metadata would ease lookup; current exact arXiv identifiers already identify the theorem dependencies sufficiently.",
 blocking=False)
]
verify=json.loads((out/"supplement-verification.json").read_text(encoding="utf-8"))
scale=Path(r"D:\Proyectos\airr-publicacion\scripts\prepare_model_assessment.py")
assessment=dict(
 title="Constant-gap entanglement distillation for diagonal invariant states and quantum reset channels",
 local_version="manuscript-4",pages=15,canonical_sha256=inp["files"]["main.pdf"]["sha256"],artifact_hashes=inp["files"],
 assessed_at=now,provider="OpenAI",model_id=None,requested_model="gpt-6-astra",requested_reasoning_effort="xhigh",
 runtime_model_attested=False,independence="involved_in_manuscript",
 provenance="Same reviewer involved in earlier exact manuscript and dossier audits; expanded exact-version review, not blind or an additional independent vote. No subagents. Prior evidence reused only with stated scope and identity checks; grades independently chosen for this exact manuscript.",
 recommendation="accept",recommendation_detail="Scientific acceptance in the declared scope; no mandatory mathematical or bibliographic correction. Optional precision improvements listed separately.",
 technical_quality_score=9.0,technical_quality_scale="0-10, distinct from importance",
 millennium_score=7.0,importance_airr_score=7.0,importance_label="exceptional",overall_stars=7,
 score_scale_source=str(scale),score_scale_source_sha256=sha(scale),
 score_rationale=dict(
 technical="The complete integrated proof is coherent and operationally specified: actual-survivor seed, counted assistance, public-transcript security, valid source hypotheses, finite coding for arbitrary infinite-entropy reset densities, reproducible supplement and legible 15-page PDF. No unresolved material objection. The review is neither formal verification nor independent human scrutiny.",
 importance="An exceptional specialized theoretical contribution: a universal coherent-block distillation lower bound yields absolute dimension-independent intervals for two broad established invariant classes and removes all marginal restrictions from pure/separable constant irreversibility. The unrestricted mixed-MC recovery, identity/EB and oscillator applications demonstrate reach of one mechanism. This judgment is based on that finite-dimensional structural theorem, not on counting corollaries or inheriting earlier grades. Existing protocol primitives and known special cases, nonoptimal constants, loose small-dimension bounds, asymptotic inefficiency and a limited priority search prevent a field-shaping/historic rating."),
 criteria=dict(
 correctness_confidence=dict(stars=5,basis="All integrated claims reviewed; no unresolved material objection. Limited to this involved model review."),
 rigor=dict(stars=5,basis="Explicit parity Kraus, fixed low-entropy A, iid decoding, positive seed and reserve-error control, operational hypotheses and limit order."),
 novelty=dict(stars=4,basis="Bounded stopped-classification loss and broad absolute-gap consequences appear substantive in checked sources; primitives/classes/reduction credited. No exhaustive priority certificate."),
 significance=dict(stars=5,basis="Uniform absolute control across CLDUI/LDOI and arbitrary pure/separable mixtures, with channel and infinite-dimensional applications."),
 presentation=dict(stars=4,basis="Finite theory now leads and dependencies are explicit. Long theorem proof and several continuations are readable; optional source pointers could improve navigation."),
 reproducibility=dict(stars=5,basis="All supplement hashes valid, new 264-case reproduction exact except timestamp, identical earlier evidence identified, 24 high-precision table entries verified.")
 ),
 strengths=[
 "Universal classification theorem stands before applications and supplies its own actual-survivor seed.",
 "No matching marginal, free initial ebits, hidden nonlocal block measurement or restricted adversary is used.",
 "ER, ER^infty, KD and EC scopes remain distinct; disputed optional EC-to-single-copy-ER replacement is absent.",
 "Physical reset outputs with infinite entropy are handled by finite decoded coding and erasure upper bounds.",
 "Direct finite-partner subset proof and explicit adaptive mean-energy convention avoid unjustified infinite-dimensional iterations.",
 "Known classes, breeding primitives, reduction method and vacuum/fading special cases are attributed."
 ],
 unresolved_material_objections=[],required_revisions=[],optional_revisions=minor,claims=claims,
 operational_formulation_sufficient=True,theorem_citations_sufficient=True,bibliography_has_nonblocking_erratum=False,
 verification=dict(manifest_valid=True,supplement_files=18,manifest_entries=17,reused_identical_script_or_record_files=14,
 newly_executed_author_scripts=["verify_diagonal_invariant_5.py"],new_author_cases=264,
 new_output_equal_except_created_at=True,new_summary=verify["new_reproductions"][0]["summary"],
 reused_author_case_counts=[200,500,120,240,1000,480],
 reused_independent_evidence="Previous finite Kraus/general-noise/reduction/MC/CLDUI/LDOI checks reused with their existing limits; no new claim of numerical rate certification.",
 table_entries=24,author_table_precision_digits=100,independent_table_precision_digits=130,
 table_evidence_reused_after_byte_identity=True,all_table_roundings_match_exact_tex_and_pdf=True,
 interval_certified=False,new_harness_incidents=[],
 environment=dict(python="3.12.14",numpy="2.2.6",scipy="1.18.0",mpmath="1.3.0")),
 visual_review=visual,
 limitations=[
 "Same involved reviewer, not formal verification, blind peer review, independent human validation or runtime model attestation.",
 "Targeted source audit does not establish exclusive priority.",
 "Constant gaps need not be optimal or useful at every low dimension; no efficient code implementation.",
 "No general mixed-state EC reversibility, no LDOI EC-ED bound and no resolution of NPT bound entanglement.",
 "Invariant-state upper bounds do not transfer to an arbitrary state before twirling.",
 "Oscillator reset state fixed before N tends to infinity; no uniform rate over all densities or unrestricted tau_N.",
 "No exact finite-energy reset capacities, quantum/private arbitrary-partner additivity, channel-simulation cost or energy-constrained local state formation.",
 "Grades apply only to the exact files identified here; later research excluded."
 ],
 published=False,deposited=False,inputs_modified=False,prior_reviews_modified=False,subagents_spawned=False,archive=str(archive))
(out/"assessment.json").write_text(json.dumps(assessment,indent=2,ensure_ascii=False),encoding="utf-8")
report=r"""REVISION CIENTIFICA DEL MANUSCRITO 4 EXACTO
Constant-gap entanglement distillation for diagonal invariant states and quantum reset channels
Lluis Eriksson. Working paper, 18 October 2026. PDF de 15 paginas.

DICTAMEN Y NOTAS
Recomendacion: ACCEPT, en el alcance declarado.
Calidad tecnica: 9/10.
Importancia AIRR: 7/10, excepcional segun la rubrica; distinta de la calidad tecnica.
No hay objecion material pendiente ni correccion obligatoria. Las sugerencias finales son de precision bibliografica y presentacion. No se fija una nota objetivo ni se trasladan notas de versiones anteriores.

Entrada exacta:
main.pdf SHA256 04d8bb0d944fb667d67ab0a9fd59f1bcd2f8d79175d5a3de885274c250c25c5c
main.tex SHA256 98b459adb42322fb564e10a581c816895ccfe6c5edf4cd97ab04e7a4416badf2
supplement.zip SHA256 75d174a77777b584273a084442bb9cdfc5872e35785645183c2f4301da165aec
artifact-manifest.json SHA256 357b9671b16087d86c3345ac776520a02289631598fcb24812087fb4ee4118eb
Se verificaron los hashes antes y al cerrar. Se leyo todo el TeX, se extrajo el PDF y se inspeccionaron individualmente sus 15 paginas. No se revisa una futura integracion ni material de investigacion posterior.

PROCEDENCIA
Es el mismo revisor involucrado en los dossiers y manuscritos anteriores. No es revision ciega, voto independiente adicional, revision humana ni verificacion formal. Se solicito GPT-6 Astra/xhigh; no existe atestacion independiente del runtime. La evidencia anterior se reutiliza con ambito y hashes explicitos. No se delego a otros agentes, no se editaron entradas, no se publico y no se contactaron personas.
La rubrica se relee en D:\Proyectos\airr-publicacion\scripts\prepare_model_assessment.py: 3 aceptable/substantivo, 4 fuerte, 5 muy bueno, 6 excelente, 7 excepcional, 8 potencialmente transformador del campo, 9 potencialmente historico; 10 reservado a un Millennium reconocido resuelto incondicionalmente y extraordinariamente verificado. No es una probabilidad ni una calificacion escolar.

RAZON DE LA VALORACION
La calidad tecnica 9 refleja una integracion correcta: la clasificacion universal aparece antes que sus aplicaciones y prueba la existencia de su propia semilla; los ebits prestados se pagan, los errores y el transcript publico se incluyen, las hipotesis operacionales se aplican a los canales correctos y el texto no confunde medidas de una copia con sus regularizaciones. El PDF y el suplemento son comprobables. No doy 10 ni presento la revision como certificacion independiente o formal.
La importancia 7 se funda en el teorema finito: una cota computable para cualquier bloque coherente emparejado produce intervalos absolutos, independientes de dimension, para CLDUI y LDOI, y una cota universal de irreversibilidad para cualquier mezcla de un puro con ruido separable, sin condicionar marginales. El mecanismo tambien controla un componente MC mixto y tiene aplicaciones de canal y oscilador. Esa amplitud justifica una contribucion teorica excepcional dentro de su area. No se obtiene el juicio sumando corolarios ni heredando una nota anterior.
Las clases, las primitivas de breeding/hashing, el criterio de reduccion y varios casos de reinicio ya eran conocidos. Las constantes no estan optimizadas, las cotas pueden ser triviales en dimensiones pequenas, el protocolo no es eficiente y la busqueda de prioridad es limitada. No considero demostrada relevancia transformadora del campo, historica ni una solucion de un problema general de entrelazamiento.

1. NUCLEO FINITO: LEMA 1 Y TEOREMA 2, PP.2–4
El Lema 1 es correcto para theta arbitrario finito. X=rho_A>=a theta_A asegura el soporte necesario. De a theta<=rho<=X tensor I, monotonía de log con regularizacion da
log2 a + [S(theta_A)-S(theta)] + D(theta_A||X)<=0.
La hipotesis a 2^u_A>1 contradice la no negatividad de D. Horodecki–Horodecki proporciona una tasa estrictamente positiva tras violacion de reduccion, no solamente NPT. Se atribuye el argumento logaritmico a Vollbrecht–Wolf. La realizacion finita del twirl isotropico por Caratheodory es suficiente a dimension fija.

El Teorema 2 realmente se aplica a cualquier rho finita en una base emparejada:
- El twirl conjugado Z3^d conserva B y deja diagonales en el sector desigual. Los caracteres ordenados son distintos modulo 3. El texto distingue la marginal AB promediada del estado condicionado al registro publico o a la purificacion.
- Uniformizar A en GL(m,2) da la ley geometrica truncada del primer uno; su entropia <=2 y concavidad garantizan un A FIJO con H(J_A)<=h(w)+2(1-w). No se exige un algoritmo eficiente para encontrarlo.
- Los Kraus K_uv=Pi_{u xor v}/sqrt(2) son correctos y no miden el indice de Schmidt. Las filas de un hash sobre varias copias se implementan con la misma paridad local reversible y un Bell consumido.
- El coste por prefijos suma exactamente H(J_A); los hashes tipicos, los abortos de tamanos atipicos y el numero finito de etapas son suficientes a d fijo. En la marginal block-diagonal la probabilidad de clasificacion erronea controla el error de traza. No hace falta afirmar esa estructura despues de condicionar en Eve.
- El superviviente real es theta=B/w, MC, con u>=0. Hashing da G=wu=v. L>0 implica w2^u>1, de modo que la semilla se demuestra para el estado aceptado real, tambien cuando theta es mixto. Ya no se necesita matching marginal ni una semilla externa.
- La eleccion explicita 0<2 eta<G-C, la reserva inicial de O(ell) copias, t_ell creciente suficientemente lento y el error telescopico justifican el neto G-C. No se regalan ebits. La fidelidad final a Bell desacopla cualquier purificacion y transcript publico.
w=0, w=1, d=1 y probabilidades cero estan tratados. El orden de limites es por estado y dimension fijos antes de pasar a familias crecientes.

Para CLDUI, Delta rho es separable y D(rho||Delta rho)=v por suma directa. Su soporte contiene el de rho incluso con diagonales nulas. La cadena E_D<=K_D<=E_R^infty<=E_R<=v y ancho <=log2(5) es correcta. El paso para K_D usa la dependencia especifica HHHO, no una cota exclusiva para E_D.

2. LDOI, MEZCLAS Y CANALES FINITOS, PP.4–6
Corolario 3: la caracterizacion conocida tiene B y bloques positivos 2x2 R_ij. No se realiza una medida global gratuita. La identidad C_Delta=v+c y 0<=c<=1-w es exacta, y el caso de extremo inferior cero tambien satisface la cota de ancho. Por ello C_Delta-E_D, E_R-E_D y K_D-E_D<=log2(9). No hay cota E_C-E_D para LDOI ni solucion de NPT bound entanglement. En los Werner usuales B es diagonal y la cota inferior puede ser cero.

Teorema 4: primero se acondiciona al flag local, luego se aplica el Teorema 2 al estado aceptado. El factor P=lambda+delta multiplica correctamente toda la tasa. Concavidad de la entropia marginal y la cota superior de entropia de mezcla dan
P0 Ic(Gamma/P0)>=lambda u-b(lambda,delta kappa).
La identidad de entropia de tres ramas y h(kappa)+2(1-kappa)<=log2(5) dan la perdida declarada. Los extremos de peso cero no requieren dividir por cero. La semilla ya esta pagada en el Teorema 2 y se calcula con el superviviente, sin volver a imponer una condicion sobre la marginal del ruido.
El superior E_C<=lambda s exige componente bueno puro y ruido separable, como dice el texto. Preparacion por ramas y dilucion pura dan el coste; la brecha <=log2(6) no se presenta como alcanzada ni optima.

Corolario 5: para theta MC, E_R(theta)<=u por la referencia diagonal; convexidad da el superior lambda u con ruido separable. E_D,K_D,E_R^infty,E_R quedan controlados absolutamente cuando q->0, sin q log d->0. No se extiende a E_C de theta mixto.
Corolario 6: la formulacion pura/separable en dimensiones crecientes es correcta; el ejemplo q=(log d)^(-1/2) ilustra una diferencia real frente a continuidad con factor log d.
Corolario 7: cualquier canal EB produce una rama Choi separable. El inferior sale del estado distribuido. La extension clasica de rama y descomposicion separable da una cota de squashed entanglement de canal lambda log d, valida para K2 adaptativa y Q2. No hace falta covarianza.

La frase opcional que confundia una cota E_C del ruido con un superior de E_R de una copia NO esta en el manuscrito. Tampoco aparecen los corolarios opcionales de numero de Schmidt ni 1/(e ln2); no se evaluan aqui ni se transfieren como resultados aceptados.

3. REINICIO DEL OSCILADOR, PP.6–12
Se mantiene la distincion entre reinicio probabilistico y perdida gaussiana. Tau es cualquier densidad fija, sin conmutacion con H y sin exigir entropia o energia finitas.
Lema 9: diferencia de canales de reemplazo, norma diamante exacta 2delta, y cola <=Tr 1_{H>=K} tau; el decoder elimina coherencias entre codigo y complemento, sin perdida cuadratica ni postseleccion.
Lema 10: informacion condicional perdida I(R:F|B)<=S(F|B)<=H(F|Y)=b(lambda,delta). La primera desigualdad usa F clasico; la direccion de data processing es correcta. Informacion coherente y version clasica se deducen sin dimension multiplicativa. Todos los registros usados aqui son finitos.

Proposiciones 11–12 y Teorema 8: el coding inferior se aplica al canal finito codificado/decodificado con holgura estricta. No se aplica una formula con entropia de salida finita al reinicio fisico cuando tau la tiene infinita. Los superiores usan erasure y postprocesado. Se verifican Gibbs, salida y complemento finitos en erasure para Wilde–Qi, y se distingue su tarea privada de discusion publica bidireccional. Antidegradabilidad da Q=P=0 para lambda<=1/2.
Lema 13: formulas exactas de media y entropia de la geometrica truncada, holgura positiva, t<=(N+1)^(-2) y perdida absoluta a_N=o(1) son correctas. La cola de cualquier tau trace-class lleva delta_N a cero. La uniformidad solo sobre conjuntos de energia de reinicio acotada y el orden n primero, N despues se expresan correctamente.

Teorema 14: la semilla y el reciclado usan copias distribuidas por la misma entrada de energia finita; no hay energia inicial sin contar. La cota DSW se aplica a erasure, con coste medio adaptativo sobre marginales promediadas y seguridad de entorno completo. La convencion LOCC numerablemente descomponible es explicita. Esto da las dos tasas asistidas sin S(tau)<infinito.
Corolario 15: la salida distribuida tiene componente puro de peso lambda y rama producto. Dilucion pura por ramas y preparacion local numerable de tau dan el superior de E_C incluso con S(tau)=infinito. El decoder da el inferior de E_D. Es coste de ESTADOS y las operaciones locales no estan energeticamente restringidas. El texto no lo convierte en coste de simulacion de canal.

Teorema 16: M=Psi^n siempre finito; la desigualdad del techo convexo de entropia se obtiene por purificacion/complemento, concavidad y convexidad. Cada patron de supervivencia conserva la marginal B; el promedio da n lambda g(N)+chi(Psi^n). El coding restringido y la regularizacion se usan donde hay entropias finitas. La cota del defecto no depende de Psi y permite el supremo declarado. No se concluye aditividad exacta a N finito ni una afirmacion cuantica/privada.
Corolarios 17–18: time sharing con vacio prueba positividad para cada N>0 cuando lambda>1/2 bajo coste medio, y el bloque d=2 desplazado tiene expectativa de transpuesta parcial -lambda/2+delta/4<0 para K grande. Son consecuencias correctas y los casos de vacio conocidos se reconocen.

4. ANTECEDENTES, CITAS Y FORMULACION
Las citas y la formulacion operacional bastan para los resultados declarados. Se conservan las atribuciones a Hostens, Vollbrecht–Verstraete, Maneva–Smolin y Leung–Shor para primitivas; a Vollbrecht–Wolf para el antecedente isotropico normalizado y el metodo logaritmico; a HH para semilla; a HHHO para la cota de clave; a Johnston–MacLean y Singh–Nechita para las clases y estructura.
Britz–Laurent se cita como trabajo de jerarquias/separabilidad, sin adjudicarle ni negar por inferencia un teorema operacional. Su version referida es de mayo de 2026, aunque su identificador arXiv comienza por 2512.
Catalano et al. conserva el credito por reinicio de vacio, informacion coherente relevante y divergencia sin restriccion; Amosov–Mancini por aditividad de erasure. Los teoremas de coding, hashing, dilucion y upper bounds adaptativos son dependencias reconocidas.
A.W. Leung y J. Britz estan corregidos. El articulo no usado de reverse coherent information fue retirado. Las 23 referencias tienen cita y las referencias internas se resuelven.
Nueva comprobacion de metadatos: la primera pagina editorial de ELA confirma Johnston–MacLean, volumen 35, 156–180, mayo de 2019.
No hay certificacion mundial de prioridad: las lecturas primarias y consultas dirigidas no hallaron un teorema que absorba exactamente el resultado general, pero esa ausencia no demuestra novedad. No he releido completos todos los trabajos; source-register.json declara el ambito reutilizado y nuevo.

Sugerencias no obligatorias:
- Corolario 3: citar tambien la Proposicion 4.1 de Singh–Nechita, donde la suma directa aparece explicitamente.
- Teorema 16: especificar Proposicion 3 del preprint de Holevo para la regularizacion clasica restringida.
- Anadir datos de revista de Devetak–Winter, HHHO y Vollbrecht–Wolf si se desea facilitar consulta; los identificadores arXiv actuales son suficientes.
Ninguna sugerencia cambia la recomendacion ni exige reabrir la demostracion.

5. SUPLEMENTO, TABLA Y PRESENTACION
El ZIP exacto tiene 18 archivos: 17 entradas verificadas por su manifiesto mas el propio manifiesto. Solo contiene scripts, registros y README; no fuentes PDF externas ni revisiones privadas.
Catorce archivos coinciden byte a byte con evidencia previamente comprobada: scripts/registros de 200, 500, 120, 240, 1000 y 480 casos, mas script/registro de la tabla. Se verifico la identidad antes de reutilizar las reproducciones anteriores. No se ejecutaron de nuevo innecesariamente.
Nuevo en esta revision: ejecucion de verify_diagonal_invariant_5.py en una copia separada. Los 264 casos (240 aleatorios y 24 controles), 119 twirls completos y 58 cotas inferiores positivas reproducen todos los campos del registro salvo created_at. Error maximo de identidad entropica 3.1086244689504383e-15, error maximo de twirl 8.881784197001252e-16. No hubo fallo de asercion ni incidente nuevo de arnes.
Se conserva asimismo la evidencia independiente ya archivada, incluidos los 280 LDOI y 35 Werner de la auditoria 8 y las comprobaciones previas de Kraus multicopia, reduccion, MC y ruido general. No se confunden esos casos con los del autor ni se presentan como verificacion numerica de capacidades.
Python 3.12.14, numpy 2.2.6, scipy 1.18.0 y mpmath 1.3.0 coinciden con README.

La tabla es identica a la ya reproducida a 100 digitos y contrastada independientemente a 130 digitos. Se verificaron las 24 cifras actuales en el TeX y en el PDF. Los scripts/registros y formulas son los mismos; no se recalculo innecesariamente. La anterior diferencia de ~4.38e-92 en una cadena numerica de alta precision no afecta a los seis decimales. Es una tabla de cotas analiticas, no una estimacion optimizada de capacidades ni aritmetica intervalar formal.
Se renderizaron las 15 paginas con Poppler a 100 dpi y se vieron individualmente. Texto, formulas, tabla y bibliografia son legibles, sin recortes o superposiciones observados. Las continuaciones de teoremas y pruebas entre paginas son normales. No se recompilo el documento; el manifiesto del autor comunica compilacion builtin y Tectonic, separada de nuestra inspeccion.

LIMITES DEL DICTAMEN
Aceptacion cientifica razonada del documento exacto, no aceptacion de revista ni evidencia de teorema por una nota. Los tests finitos no prueban coding, privacidad, limites asintoticos ni prioridad. La nota de importancia reconoce amplitud y mecanismo, no resultados fuera de lo escrito.
No se afirma reversibilidad de todo mixto, brecha E_C-E_D para LDOI, solucion de NPT bound entanglement, constante optima, eficiencia del protocolo, capacidad exacta a energia finita, uniformidad en toda tau cambiante, coste energetico local de formacion ni simulacion de canales.
Los archivos de entrada y las revisiones anteriores se conservan intactos. Todo este dictamen se guarda en C y se copia con hashes verificados al archivo durable de D; no se borra trabajo activo.
"""
(out/"manuscript-review.txt").write_text(report,encoding="utf-8")
# Identity check at close, including prior frozen assessments and dossiers.
protected={
 root/"input"/"main.pdf":inp["files"]["main.pdf"]["sha256"],
 root/"input"/"main.tex":inp["files"]["main.tex"]["sha256"],
 root/"input"/"supplement.zip":inp["files"]["supplement.zip"]["sha256"],
 Path(r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-manuscript-3\assessment.json"):"c24907731a7694eb8742008ce17e071aa180254312263e7d91da29bf7c060be7",
 Path(r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-adaptive-3\verdict.json"):"f37d220223e7881f66bee393227cc71f002f3ea82f1a2f081f68751e1215cc87",
 Path(r"D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-adaptive-4\verdict.json"):"a655ed033e3fb3519cf8ed8fc870dc5326f1061ad6b09cd58cb70b7be4daada5"
}
pc=[]
for p,h in protected.items():
 assert sha(p)==h
 pc.append(dict(path=str(p),sha256=h,unchanged=True))
(out/"protected-artifacts-check.json").write_text(json.dumps(dict(checked_at=now,files=pc),indent=2),encoding="utf-8")
(out/"reference-check.json").write_text(json.dumps(dict(labels=len(labels),references=len(refs),bibitems=len(bib),all_cited=True,undefined_labels=[],unresolved_pdf_markers=False),indent=2),encoding="utf-8")
inventory=dict(created_at=now,algorithm="SHA256",exclusions=["hash-inventory.json","archive-verification.json"],
 files=[dict(file=p.relative_to(out).as_posix(),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(out.rglob("*")) if p.is_file() and p.name not in ["hash-inventory.json","archive-verification.json"]])
(out/"hash-inventory.json").write_text(json.dumps(inventory,indent=2),encoding="utf-8")
archive.mkdir(parents=True)
for p in out.rglob("*"):
 if p.is_file():
  q=archive/p.relative_to(out);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
copied=[]
for p in out.rglob("*"):
 if p.is_file():
  q=archive/p.relative_to(out);assert sha(p)==sha(q)
  copied.append(dict(file=p.relative_to(out).as_posix(),sha256=sha(p),equal=True))
receipt=json.dumps(dict(created_at=now,source=str(out),destination=str(archive),all_equal=True,files=copied,
 receipt_self_hash_excluded=True,no_active_work_deleted=True),indent=2)
(out/"archive-verification.json").write_text(receipt,encoding="utf-8")
(archive/"archive-verification.json").write_text(receipt,encoding="utf-8")
for p in out.rglob("*"):
 if p.is_file():assert sha(p)==sha(archive/p.relative_to(out))
print(json.dumps(dict(recommendation="accept",technical=9,importance_airr=7,
 archive=str(archive),files=sum(p.is_file() for p in archive.rglob("*")),
 assessment_sha256=sha(out/"assessment.json"),review_sha256=sha(out/"manuscript-review.txt"),
 inventory_sha256=sha(out/"hash-inventory.json")),indent=2))

