from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path(__file__).resolve().parent
B=R.parent.parent
D=Path('D:/Proyectos/airr-investigacion/2026-10-18_escape-energetico')
archive=D/'revision-manuscript-3'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj): (R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inputs=json.loads((R/'input-check.json').read_text(encoding='utf-8'))
verification=json.loads((R/'supplement-verification.json').read_text(encoding='utf-8'))
assert verification['passed']
scale=Path('D:/Proyectos/airr-publicacion/scripts/prepare_model_assessment.py')

report='''DICTAMEN DEL MANUSCRITO-3 EXACTO
Dimension-free bounds on entanglement irreversibility and quantum reset capacities
Lluis Eriksson. Working paper, 18 de octubre de 2026. PDF de 13 páginas.

RECOMENDACIÓN Y NOTAS
Aceptar científicamente, con una corrección bibliográfica menor identificada abajo.
Calidad técnica: 9/10.
Importancia AIRR: 6/10, «excelente» según la rúbrica indicada.
No hay una objeción material pendiente ni una revisión matemática bloqueante.

Estas notas corresponden al documento completo exacto y su suplemento. No son una
nota de los dossiers, una certificación de prioridad, una predicción de citas ni
una aprobación editorial externa. La nota técnica juzga la prueba y su exposición;
la importancia juzga la contribución científica. No se ha usado una nota objetivo.

IDENTIDAD DEL OBJETO Y PROCEDENCIA
PDF SHA256 cb01a215647bbf10905915fb2971b3c06b7bb05b5917d48f5c69e07b5607e375
TeX SHA256 49f1774de8d208c639ebc60ecdc9c43fc696b679ec08a10e23d5afc611007c19
ZIP SHA256 4dbe3519ac66c034da399c77105f1306b901fe55e497da99a96ecb5947f70028
Los tamaños y hashes coinciden con el manifiesto y con la encomienda. Se conserva
una copia de los cuatro archivos de entrada. Se ha leído todo el TeX, contrastado
la integración con el PDF y visto cada una de sus trece páginas renderizadas.

Es la continuación del MISMO revisor implicado en auditorías anteriores de esta
investigación. No es revisión ciega ni otro voto independiente. Se solicitó
GPT-6 Astra con esfuerzo xhigh; no se dispone de una atestación independiente de
identidad de runtime. No se usaron otros agentes. No se editó ningún original,
manuscrito previo o dictamen anterior; no hubo publicación ni comunicación externa.
La propuesta posterior de eliminar la hipótesis de marginal coincidente NO forma
parte de este objeto ni de estas notas. Se evaluará, si procede, separadamente.

FUNDAMENTO DE LAS NOTAS
La calidad técnica es alta: la versión integrada presenta el pago de las consultas
no locales, una semilla positiva sin asistencia inicial, un control del error al
reciclar reservas, seguridad frente a una purificación y todo el registro público,
y límites operacionales en el orden adecuado. Evita expresiones de entropía
indefinida en el canal físico: codifica en un canal decodificado finito y aplica
los conversos al canal de borrado. Las atribuciones y restricciones de alcance
son explícitas. Las correcciones indicadas son de precisión editorial, no nuevos
lemas imprescindibles.

La importancia 6 reconoce un resultado especializado excelente con alcance mayor
que el oscilador de reinicio: una cota absoluta independiente de dimensión sobre
irreversibilidad para mezclas pura/separable de marginal coincidente, una cota
uniforme para todo canal identidad/entanglement-breaking en dimensión finita, y
seis límites absolutos de capacidad para cualquier estado fijo de reinicio,
incluso de energía o entropía infinitas. La aportación identificada es la combinación
del clasificador de primera discrepancia de entropía acotada y la contabilidad
operacional para producir pérdidas absolutas. No se atribuyen como nuevas las
consultas bilaterales, partial breeding, hashing, dilución, filtrado isotrópico,
bootstrap o cotas de squashed entanglement.

No asigno 7 o más: la constante no se optimiza, las tasas no dan capacidades
exactas a energía finita ni una implementación eficiente, la familia general
conserva hipótesis específicas y no se resuelve la reversibilidad de estados
mixtos arbitrarios. Hay antecedentes muy próximos para mecanismos y casos
especiales. La búsqueda bibliográfica es dirigida, no una garantía mundial de
prioridad; tampoco hay verificación formal o revisión humana independiente.

AUDITORÍA DE LOS RESULTADOS INTEGRADOS
1. Lema 2, p. 3: válido. La diferencia con borrado es un mapa de reemplazo
X -> Tr(X) A. Su norma diamante es ||A||_1=2 delta, también con referencia
arbitraria. Los bloques positivo y negativo tienen traza delta. La desigualdad
epsilon <= Tr[1_{H>=K} tau] usa la inclusión de proyectores; M/K sólo se emplea
cuando M es finito. No se supone que tau conmute con H.

2. Lema 3, p. 4: válido. El registro de rama F es independiente de la referencia;
I(R:BF)=2 lambda s. La diferencia es I(R:F|B), acotada por S(F|B), y luego por
H(F|Y)=b(lambda,delta) al medir únicamente pertenencia. La dirección de procesamiento
de datos es correcta. Todos estos sistemas son finitos. El cálculo clásico y la
cota b<=h(delta) son correctos; no aparece un factor log d oculto.

3. Proposiciones 4 y 5: válidas bajo las convenciones de p. 2. El coste diagonal
del codificador finito es acotado y hay holgura estricta. Los teoremas citados de
capacidad sólo se aplican al canal finito o al borrado. El converso conserva el
coste de entrada bajo posprocesado del receptor. Las condiciones Gibbs y de
entropía de salida finita están verificadas para borrado; no se trasladan sin
justificación a un reinicio de entropía infinita. La antidegradabilidad da Q=P=0
para lambda<=1/2, incluidos los extremos.

4. Lema 6 y Teorema 1, pp. 5-6: válidos. La media geométrica truncada deja holgura
dt/(1-t)>0, y la expresión de su entropía y t<=(N+1)^(-2) tienen signos correctos.
La pérdida de entropía es o(1), no sólo o(log N). Para todo tau fijo de clase
traza, delta_N tiende a cero. La uniformidad M<=M0 y la mejora con cola térmica
se deducen de cotas explícitas; no se afirma uniformidad sobre todas las densidades.
El bloque de codificación tiende a infinito antes que N, evitando un uso no
justificado de un teorema uniforme en d(N).

5. Teorema 7, pp. 6-8: válido con chi_A=sigma, tal como está enunciado.
La media finita Z_3^d conserva el sector maximally correlated y diagonaliza el
resto: los caracteres asociados a pares ordenados j!=k son distintos. No se
supone que esta diagonalidad subsista condicionando en el registro público.
La ley de la primera coordenada no nula de Az es geométrica truncada y su
entropía condicional es <=2. La concavidad selecciona una matriz A fija para todas
las copias; no se necesita un recurso gratuito de side information variable.

La fórmula de Kraus K_uv=Pi_{u xor v}/sqrt(2) preserva coherencia dentro de cada
paridad; también vale para paridades sobre subconjuntos de copias. Se paga un
ebit por fila. El coste asintótico de clasificar hasta la primera discrepancia
es P H(J_A), por la regla de la cadena y hashing binario típico. El argumento de
colisiones, los tamaños aleatorios, la alternativa de medir todos los bits y el
aborto atípico son suficientes para precisión arbitraria a d fijo. La cota de
error en la marginal promediada sirve para fidelidad final; no necesita diagonalidad
de Eve. El sector superviviente tiene I_c del ruido no negativo porque su matriz
correlacionada tiene la misma entropía que el estado y desfasar aumenta la entropía.
La concavidad y la cota de mezcla dan P0 I_c>=lambda s-b(lambda,delta kappa).

La identidad de tres ramas convierte el coste total en
b(lambda,delta)+delta[h(kappa)+2(1-kappa)]<=b(lambda,delta)+delta log_2(5).
El factor P, el factor delta y el término de descarte son correctos. No se resta
gratuitamente el coste de la semilla ni se confunden rendimientos bruto y neto.

Si L>0, a=lambda/P>1/r. El filtro de Alice en el soporte de sigma pasa ambas
ramas con probabilidad r p_min>0, precisamente por chi_A=sigma. La proyección
posterior de Bob conserva la rama pura y sólo puede aumentar su peso. El estado
filtrado tiene fidelidad >1/r con Phi_r y el criterio isotrópico de Horodecki-
Horodecki proporciona una tasa semilla positiva para ese estado fijo. Los ceros
del espectro se tratan con el soporte; r=1 y P=0 son triviales.

La reserva inicial usa O(ell) copias a tasa positiva, se retiene de cada bloque
posterior y el número de bloques aumenta suficientemente despacio para que
t_ell epsilon_ell ->0. La fracción inicial desaparece. Es suficiente elegir
2 eta<G-C; sería útil escribirlo explícitamente (ver mejoras). La elección
diagonal no exige un exponente de hashing. La proximidad a pares Bell puros
implica desacoplamiento de toda purificación y de los mensajes públicos, por
lo que la seguridad no presupone una Eve restringida a la rama clásica.

Si chi es separable, la formación por ramas y dilución cuesta <=lambda s.
Combinada con E_D<=E_C da (24), incluso si L<=0. El máximo de
h(lambda)+(1-lambda)log_2(5) es log_2(6), en lambda=1/6. La constante es una
cota, no un óptimo demostrado. La hipótesis separable sólo se usa para este
converso de coste; la cota inferior de destilación admite ruido entrelazado con
la marginal coincidente.

6. Corolarios 8 y 9, pp. 8-9: válidos. La desaparición absoluta del defecto no
requiere q log d ->0. Para cualquier canal EB de C^d a C^d, su estado Choi
normalizado es separable y tiene marginal I/d. El teorema da la cota inferior de
tasa mediante destilación. El límite superior de Q2 y K2
proviene de una extensión con bandera y descomposición separable, de CMI
2 lambda S(rho), y de la cota operacional de squashed entanglement. No se
requiere covariancia ni que EB sea un reemplazo. La frase «gap at most log_2 6»
es válida también cuando se recorta la cota inferior a cero.

7. Teorema 10 y Corolario 11, pp. 9-10: válidos para todo tau fijo, sin hipótesis
de energía ni entropía finitas. El canal decodificado produce chi=sigma tensor
theta, con theta finita; así la nueva cota no contiene S(theta). El coste de la
semilla se cuenta dentro de las mismas entradas finitas. Para el límite superior
adaptativo se usa la convención de coste medio y LOCC numerablemente descomponible
de Davis-Shirokov-Wilde, y se aplica su teorema al borrado. La formación del estado
físico usa lambda psi_N+(1-lambda)sigma tensor tau. Toda densidad de clase traza
admite descomposición espectral numerable, por lo que preparar tau localmente
no exige su entropía finita. Las operaciones locales en E_C no tienen restricción
energética. Es coste de estos estados, no coste de simulación del canal.

8. Teorema 12, p. 10: válido. La desigualdad de entropía frente al convex roof
de M se obtiene primero en puros por el complemento y después por descomposición
espectral numerable y convexidad. Se fija M=Psi^{tensor n}, finito para cada n;
no se itera una afirmación sólo probada en dimensiones finitas. Los patrones de
borrado comparten la marginal de B y sus entropías de bandera se cancelan.
La regularización y el coste medio llevan a una cota independiente de Psi,
incluida su dimensión. Se afirma defecto asintótico, no aditividad exacta finita.

9. Corolarios 13 y 14: válidos. El reparto de posiciones de energía alta y vacío
mantiene la energía media y da tasa positiva para todo N>0 si lambda>1/2.
La antidegradabilidad prueba la necesidad. La prueba de no-EB usa d=2, la cola
de clase traza y una expectativa de transpuesta parcial -lambda/2+delta/4,
negativa para K grande. Estos corolarios no se venden como novedad principal.

CITAS, ANTECEDENTES Y ALCANCE DE LA NOVEDAD
Las dependencias operacionales y las atribuciones principales bastan para las
pruebas presentadas. Las lecturas primarias previas se reutilizaron con su registro
de procedencia, sin fingir una segunda revisión independiente ni una lectura
completa de toda fuente. Source-register.json y los archivos anteriores conservan
los ámbitos efectivamente leídos. Catalano (vacío, información coherente y
divergencia sin restricción), Amosov-Mancini (borrado), Vollbrecht-Wolf (tasas
isotrópicas normalizadas), Hostens y Vollbrecht-Verstraete (partial breeding,
descarte y eliminación de asistencia) están distinguidos de la cota absoluta
actual. La construcción no se deduce sólo de aplicar continuidad dimensional:
el punto nuevo candidato es el coste de clasificación acotado y su uso combinado.

Comprobaciones bibliográficas nuevas: la página primaria arXiv de 0702156v3
confirma Alan W. Leung; APS confirma que el título publicado de Horodecki-
Horodecki sí es el abreviado usado aquí; no hay que corregirlo por diferir del
título del preprint. La ficha arXiv de Goodenough-Elkouss-Wehner v2 confirma los
datos de publicación. Se inspeccionó además el resumen primario de Abdelhadi
et al., Phys. Rev. Research 8, 013018 (2026), DOI 10.1103/8kdf-37gp: trata
mejoras de destilación para amortiguamiento y despolarización; esa lectura de
resumen no es una auditoría de su texto completo ni prueba de ausencia de
antecedentes. No apareció una dependencia imprescindible ausente del manuscrito.

CORRECCIÓN MENOR Y MEJORAS OPCIONALES
Obligatoria editorial, no matemática: en referencia [19], p. 13, cambiar
«D. Leung» por «A. W. Leung». Fuente primaria:
https://arxiv.org/abs/quant-ph/0702156v3 . El enlace y el trabajo citado son correctos.

Opcionales para máxima claridad:
- En p. 8, concretar 0<2 eta<G-C al escoger la holgura del reciclado. La elección
  suficientemente pequeña ya permitida en el texto existe; no cambia el resultado.
- Aclarar que, a dimensión fija, el twirl isotrópico puede realizarse con una
  mezcla finita de unitarias mediante Caratheodory (o aproximarse con error
  absorbido). Así queda explícita su compatibilidad con la convención LOCC
  numerable de la aplicación al oscilador. El twirl Z_3^d de la prueba ya es finito.
- La referencia [12] de reverse coherent information queda sin cita en el cuerpo
  tras sustituir ese método. Puede retirarse o conectarse al diagnóstico histórico
  del suplemento. No es una dependencia oculta de la prueba nueva.
- Para facilitar consulta, dar Proposition 3 de Holevo en el paso de
  regularización clásica y datos de revista de Devetak-Winter; las citas
  actuales ya identifican las fuentes suficientes.

REPRODUCIBILIDAD, TABLA Y PDF
El manifiesto interior del ZIP valida todos sus once elementos. Ocho archivos
de scripts/registros coinciden byte a byte con evidencia previa: 200 casos de
verify_escape, 500 de verify_extension_2, 240 de verify_general_noise_2 y los
archivos de 120 casos de verify_mismatch_1. Los tres primeros no se ejecutaron
de nuevo innecesariamente: ya habían sido reproducidos. Se ejecutaron en copias
separadas verify_mismatch_1 y el nuevo verify_table_3. Sus JSON reproducen todos
los campos excepto created_at, como advierte README. Los máximos de los 120
casos incluyen 3.997e-15 en la ley media GL y Kraus exacto a precisión de máquina.

Se reusaron además las comprobaciones independientes anteriores de 500 casos
de reinicio, con Kraus de una y dos copias, y 300 casos generales con 235
espectros de rango deficiente. Son pruebas numéricas finitas, no demostraciones
de codificación, seguridad, semilla, límites asintóticos ni prioridad.

La tabla del autor se reproduce a 100 dígitos. Se calculó por separado a 130
dígitos usando la forma estable de g y S=log_2 Z-mean(j)log_2 r. Las 24 cifras
redondeadas hacia arriba coinciden con TeX y PDF. También coinciden los seis
K y d, se verifica la holgura de energía y t<=(N+1)^(-2). La máxima diferencia
frente a las cadenas numéricas de 95 cifras del autor es 4.379e-92, atribuible
a cancelación en su evaluación de entropía a 100 dígitos; está inmensamente
por debajo del redondeo de seis decimales. Esto no es aritmética intervalar
certificada, y la tabla son cotas analíticas, no capacidades calculadas.

Incidencias de nuestro arnés, resueltas: inicialmente se leyó el texto UTF-8
con la codificación Windows predeterminada; se especificó UTF-8. Un umbral
de comparación 1e-94 era más estricto que los dígitos efectivos tras la
cancelación a N=10^8; se registraron todos los residuos y se usó 1e-88.
Ninguna incidencia afectó a una cifra publicada, al script del autor o a una
afirmación matemática. No se ocultan como pruebas fallidas del candidato.

Las trece páginas se renderizaron con Poppler a 105 dpi y se inspeccionaron
individualmente. Ecuaciones, texto, referencias y tabla son legibles, sin
solapamientos ni recortes observados. La continuación del Corolario 9 entre
pp. 8 y 9 es normal. Las citas resuelven; sólo sobra la referencia no citada
indicada arriba. No se recompiló ni modificó el PDF recibido.

LÍMITES DEL DICTAMEN
Aceptación científica razonada por un revisor de modelo implicado, no aceptación
de una revista, verificación formal ni certificación independiente. La búsqueda
no demuestra prioridad absoluta. Se conserva la hipótesis chi_A=sigma del
manuscrito exacto y la separabilidad para E_C. No se extiende aquí la afirmación
a todo estado mixto, a ruido infinito dependiente de la entrada, a estados tau
que cambien arbitrariamente con N, a coste energético local de formación o a
simulación de canales. No se transfieren estas notas a versiones futuras.
'''
(R/'manuscript-review.txt').write_text(report,encoding='utf-8')

minor=[{'id':'B1','severity':'minor_editorial','location':'Reference [19], PDF p. 13; main.tex bibitem{leung}','issue':'D. Leung is incorrect; the primary preprint author is Alan W. Leung.','correction':'Replace D. Leung by A. W. Leung.','source':'https://arxiv.org/abs/quant-ph/0702156v3','blocking':False}]
optional=[
 'Write 0<2 eta<G-C explicitly in the reserve bootstrap; sufficiently small slack already exists.',
 'State that the finite-dimensional isotropic twirl can be implemented by a finite mixture via Caratheodory, to make countable-LOCC compatibility explicit.',
 'Remove the uncited reverse-coherent-information reference or link it to historical supplemental diagnostics.',
 'Optionally specify Holevo Proposition 3 and add the Devetak-Winter journal reference.'
]
claims=[
 ('Lemma 2','Exact half-diamond distance, arbitrary references, projection and energy-tail bounds'),
 ('Lemma 3','Dimension-free hidden-branch conditional-information bound'),
 ('Propositions 4-5','Finite decoded coding and erasure operational upper bounds'),
 ('Lemma 6 and Theorem 1','Shifted geometric strict cost, entropy and four all-density absolute limits'),
 ('Theorem 7','Stopped partial breeding, coherent Kraus, survivor hashing, paid bootstrap and matching-marginal irreversibility bound'),
 ('Corollary 8','Absolute vanishing irreversibility without q log d restriction'),
 ('Corollary 9','Uniform constant gap for arbitrary finite-dimensional identity/EB channels'),
 ('Theorem 10','All-density oscillator Q2/K2 asymptotics under adaptive mean input cost'),
 ('Corollary 11','Explicit physical and decoded state E_C/E_D limits for arbitrary fixed reset density'),
 ('Theorem 12','Classical additivity defect uniform over all finite partners'),
 ('Corollaries 13-14','Positive Q/P threshold for every positive mean cost and non-EB for lambda>0')
]
assessment={
 'title':'Dimension-free bounds on entanglement irreversibility and quantum reset capacities',
 'local_version':'manuscript-3','pages':13,'canonical_sha256':next(x['sha256'] for x in inputs['input_files'] if x['name']=='main.pdf'),
 'artifact_hashes':{x['name']:{k:v for k,v in x.items() if k!='name'} for x in inputs['input_files']},
 'assessed_at':datetime.now(timezone.utc).isoformat(),'provider':'OpenAI','model_id':None,'requested_model':'gpt-6-astra','requested_reasoning_effort':'xhigh','runtime_model_attested':False,
 'independence':'involved_in_manuscript','provenance':'Same reviewer involved in previous manuscript and dossier audits; exact integrated follow-up, not blind or another independent vote. No subagents.',
 'recommendation':'accept','recommendation_detail':'Scientific acceptance; correct the nonblocking Leung author-name erratum.',
 'technical_quality_score':9.0,'technical_quality_scale':'0-10, separate from scientific importance',
 'millennium_score':6.0,'importance_airr_score':6.0,'importance_label':'excellent','overall_stars':6,
 'score_scale_source':str(scale),'score_scale_source_sha256':sha(scale),
 'score_rationale':{
   'technical':'Valid integrated arguments, correctly paid auxiliary entanglement and seed, public-transcript security, finite decoded coding for infinite-entropy resets, explicit adaptive mean-cost upper bounds, reproducible table and legible 13-page PDF. No material mathematical objection.',
   'importance':'An excellent specialized result: dimension-independent absolute irreversibility control for pure/separable mixtures with matching marginal, a uniform bound for every finite identity/EB mixture, and six absolute reset-capacity limits without entropy or energy restrictions on a fixed reset density. Established protocol primitives and close special cases limit novelty; no optimized constant, exact finite-energy capacities or arbitrary mixed-state reversibility is proved.'
 },
 'criteria':{
  'correctness_confidence':{'stars':5,'basis':'Every integrated theorem checked; no unresolved material objection. Same involved model review, not formal or independent certification.'},
  'rigor':{'stars':5,'basis':'Correct factors and conditional-information directions; coherent parity Kraus; finite fixed-A classification; positive finite-state seed, counted bootstrap and security; valid finite/infinite operational separation.'},
  'novelty':{'stars':4,'basis':'Substantive plausible absolute dimension-free bounds beyond standard relative isotropic limits; foundational partial-breeding and seed machinery explicitly attributed. Search not exhaustive.'},
  'significance':{'stars':4,'basis':'Broad finite-dimensional state and EB-channel applications plus all-density oscillator limits; still specialized, nonoptimal and not an exact finite-energy or general mixed-state solution.'},
  'reproducibility':{'stars':5,'basis':'Hashes and manifests verified; identical prior evidence reused; two author scripts newly reproduced; independent 130-digit check of all 24 table entries; all 13 PDF pages viewed.'}
 },
 'summary':'The exact 13-page manuscript proves the stated matching-marginal dimension-free recovery theorem with no free seed, uses it for arbitrary finite identity/EB mixtures and all fixed oscillator reset densities, and correctly separates operational resource conventions and limits. Scientific acceptance is recommended, with a minor bibliographic author-name correction.',
 'strengths':[
  'Stopped classification has bounded entropy and preserves the nonuniform Schmidt coherence via explicit nondestructive Kraus operators.',
  'A paid isotropic seed and slow-block reserve recycling remove external entanglement assistance without assuming a hashing error exponent.',
  'The dimension-free absolute gap applies to arbitrary separable noise with matching marginal and to all finite-dimensional EB channels in an identity mixture.',
  'Six reset-channel capacity asymptotics and explicit state reversibility hold for every fixed trace-class reset density, including infinite entropy or mean energy.',
  'Adaptive mean input energy, complete security environment, order of limits and state-versus-channel cost are distinguished.',
  'Closest known special cases and protocol primitives are acknowledged; finite diagnostics are not presented as operational proofs.'
 ],
 'weaknesses':[
  'The matching Alice marginal remains a hypothesis of the reviewed finite-state theorem; separability is required for its cost upper bound.',
  'The bound and convergence rate are not optimal, no finite-energy capacity is solved exactly and no efficient implementation is supplied.',
  'Priority search is targeted and underlying coding, filtering, partial breeding and dilution methods are established.',
  'Review is involved model evaluation, not independent human peer review or formal proof verification.'
 ],
 'potential_errors':minor,'unresolved_material_objections':[],'mathematical_revisions_required':[],
 'minor_corrections_required':minor,'optional_improvements':optional,
 'strong_novelty_candidates':[
  'Dimension-independent E_C-E_D bound for pure/separable mixtures with matching marginal, including vanishing absolute loss without q log d ->0.',
  'Uniform O(1) Q2/K2 gap for every finite-dimensional identity/entanglement-breaking mixture, without covariance.',
  'Six absolute high-energy limits and explicit state reversibility for arbitrary fixed reset densities, with no finite entropy or mean energy restriction.'
 ],
 'claim_audit':[{'label':label,'claim':claim,'status':'valid_in_stated_scope'} for label,claim in claims],
 'operational_formulation_sufficient':True,'theorem_citations_sufficient':True,
 'bibliography_has_nonblocking_erratum':True,
 'verification':{'manifest_valid':True,'new_author_script_executions':2,'new_scripts':['verify_mismatch_1.py','verify_table_3.py'],'outputs_equal_except_created_at':True,'reused_only_after_byte_identity':True,'reused_author_case_counts':[200,500,240],'newly_reproduced_author_case_count':120,'previous_independent_case_counts':[500,300],'table_values_checked':24,'author_table_precision_digits':100,'independent_table_precision_digits':130,'maximum_table_difference':'4.37856756912e-92','all_roundings_correct':True,'not_interval_certified':True,'harness_incidents':['UTF-8 read initially used Windows default encoding; corrected.','Initial 1e-94 comparison threshold exceeded effective precision after cancellation in author 100-digit calculation; all residuals logged, threshold 1e-88; six-decimal table unaffected.']},
 'visual_review':{'status':'pass','method':'Poppler independent render at 105 dpi; every page viewed individually.','pages_inspected':list(range(1,14)),'observations':'No clipping, overlaps, unreadable formulas or unresolved references observed; Corollary 9 page continuation normal; all table entries legible.'},
 'limitations':['No formal verification or independent human review.','No exhaustive priority certification.','Matching-marginal hypothesis remains part of this exact manuscript.','No assertion for arbitrary mixed states, channel-simulation cost, finite-N exact capacities, or energy-restricted state formation.','Reset state fixed before high-energy limit; no uniform rate over all densities.','Later reduction-seed dossier excluded from this review and grades.'],
 'published':False,'deposited':False,'inputs_modified':False,'prior_reviews_modified':False,'archive':str(archive)
}
save('assessment.json',assessment)
save('visual-review.json',assessment['visual_review'])

sources={
 'reused_source_registers':[
  str(D/'revision-manuscript-2'/'source-register.json'),
  str(D/'revision-adaptive-1'/'source-register.json'),
  str(D/'revision-adaptive-2'/'source-register.json')],
 'reused_core_dependencies':[
  {'source':'Wilde-Qi 1609.01997','scope':'Previously directly checked Theorems 1-3 and energy/Gibbs/finite-output-entropy hypotheses; reapplied only to finite decoded channel or erasure.'},
  {'source':'Holevo quant-ph/0211170v2 and Holevo-Shirokov 1210.6926v2','scope':'Previously checked constrained classical regularization and EA coding; source-specific hypotheses carried forward.'},
  {'source':'Davis-Shirokov-Wilde 1801.08102v3','scope':'Previously directly checked Theorem 4, equations 101 and 141, adaptive mean cost, full-environment security and countably decomposable LOCC.'},
  {'source':'Devetak-Winter quant-ph/0306078 and BBPS quant-ph/9511030','scope':'Hashing Theorem 10 and pure-state formation/dilution; prior primary reading reused.'},
  {'source':'Catalano et al. 2604.26874v2; Amosov-Mancini 0803.0452','scope':'Previously checked cited vacuum-reset, divergence and erasure strong-additivity antecedents; no new credit assigned to those special cases.'},
  {'source':'Hostens et al. quant-ph/0602205v2','scope':'Previously directly read II.B-III, nondestructive appended-pair measurement and partition-entropy breeding.'},
  {'source':'Vollbrecht-Verstraete quant-ph/0404111v2','scope':'Previously directly read relevant III.B, IV.A-B and V, discard/partial breeding and bootstrap; not claimed entire source reread.'},
  {'source':'Vollbrecht-Wolf quant-ph/0208152','scope':'Previously directly read VI.B-C isotropic normalized high-dimensional saturation; distinguished from absolute bound.'},
  {'source':'Horodecki-Horodecki quant-ph/9708015v3','scope':'Previously directly read pertinent V-VI including 41-45, filtering and isotropic positive distillation.'},
  {'source':'Goodenough-Elkouss-Wehner 1511.08710v2','scope':'Previously directly read III.B-C and appendix 1, channel squashed entanglement convexity and EB vanishing.'},
  {'source':'Maneva-Smolin quant-ph/0003099; Leung-Shor quant-ph/0702156v3','scope':'Prior direct reading: Maneva-Smolin relevant initial sections only; full four-page Leung-Shor. Background adaptive purification, not used to assume unproved non-Bell generalization.'}],
 'new_primary_metadata_checks':[
  {'url':'https://arxiv.org/abs/quant-ph/0702156v3','finding':'Author is Alan W. Leung; manuscript D. Leung incorrect. Primary abstract page read.'},
  {'url':'https://journals.aps.org/pra/abstract/10.1103/PhysRevA.59.4206','finding':'Published title is the shorter title used in manuscript; no correction needed for difference from preprint.'},
  {'url':'https://arxiv.org/abs/1511.08710v2','finding':'GEW v2 metadata and journal reference confirmed.'},
  {'url':'https://journals.aps.org/prresearch/abstract/10.1103/8kdf-37gp','finding':'Abdelhadi et al. PRResearch 8,013018 (2026): primary abstract and references inspected, NOT full paper; adaptive improvements for amplitude damping/depolarization. No exhaustive exclusion of overlap inferred.'}],
 'scope_limit':'Targeted primary-source audit, not a complete literature survey or global priority attestation.'
}
# Copy previous source registers as evidence, without copying or altering prior originals.
(R/'reused-evidence').mkdir(exist_ok=True)
records=[]
for name,live,files in [
 ('manuscript-2',B/'review-manuscript-2'/'output',['assessment.json','manuscript-review.txt']),
 ('adaptive-1',B/'review-adaptive-1',['audit-report.txt','verdict.json','independent-verification.json','source-register.json']),
 ('adaptive-2',B/'review-general-noise-1',['audit-report.txt','verdict.json','independent-verification.json','source-register.json','reproduction-comparison.json'])]:
    for namefile in files:
        p=live/namefile; target=R/'reused-evidence'/f'{name}--{namefile}'
        shutil.copy2(p,target)
        permanent=D/('revision-'+name)/namefile
        assert permanent.is_file() and sha(permanent)==sha(p), (p,permanent)
        records.append({'source_live':str(p),'source_archive':str(permanent),'copy':target.relative_to(R).as_posix(),'sha256':sha(p),'archive_matches':True})
sources['reused_evidence_files']=records
save('source-register.json',sources)

# Freeze after rechecking originals. Inventory excludes itself and the subsequent copy receipt.
for entry in inputs['input_files']:
    assert sha(R.parent/'input'/entry['name'])==entry['sha256']
inventory=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name not in ('hash-inventory.json','archive-verification.json'):
        inventory.append({'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
save('hash-inventory.json',{'created_at':datetime.now(timezone.utc).isoformat(),'review':'manuscript-3 exact involved-review follow-up','files':inventory,'inputs_unchanged':True,'prior_reviews_unchanged':True,'excluded_self_and_copy_receipt':True})
assert not archive.exists(), f'Archive already exists; do not overwrite: {archive}'
archive.mkdir(parents=True)
copied=[]
for p in sorted(R.rglob('*')):
    if p.is_file():
        dest=archive/p.relative_to(R); dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
        assert sha(p)==sha(dest)
        copied.append({'path':p.relative_to(R).as_posix(),'sha256':sha(p),'matched':True})
receipt={'copied_at':datetime.now(timezone.utc).isoformat(),'source':str(R),'destination':str(archive),'files':copied,'all_hashes_match':True,'live_work_preserved':True}
save('archive-verification.json',receipt)
shutil.copy2(R/'archive-verification.json',archive/'archive-verification.json')
assert sha(R/'archive-verification.json')==sha(archive/'archive-verification.json')
print(json.dumps({'recommendation':assessment['recommendation'],'technical':9,'importance_airr':6,'archive':str(archive),'copied_files':len(copied)+1,'report_sha256':sha(R/'manuscript-review.txt'),'assessment_sha256':sha(R/'assessment.json'),'inventory_sha256':sha(R/'hash-inventory.json'),'copy_receipt_sha256':sha(R/'archive-verification.json')},indent=2))
