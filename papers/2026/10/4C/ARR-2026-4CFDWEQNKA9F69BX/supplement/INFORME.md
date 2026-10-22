# Green 22: N0(2) y N0(3) exactos (21-10-2026)
Definicion (Lean, FormalConjectures Green22): N0(r) = menor N tal que toda r-coloracion de [1,N] tiene x,y>=3 (pueden ser iguales) con x+y y xy en [1,N] del mismo color.
## G0 antecedentes
Busqueda web (Green-Sawhney arXiv 2511.09365, Moreira, Bowen, Alweiss) y lectura del .lean: solo cota superior exp(exp(r^50)) y N0>=9. No se hallo ningun valor exacto publicado para r=2,3 (busqueda limitada; ausencia no es prueba). GS dan (remarks tras Teorema 1.1, arxiv html v2) una coloracion sin {x+y,xy} (x>y>2) para N=(3^r+7)/2: 8 (r=2), 17 (r=3). Consistente con nuestros 53 y 773, muy por debajo.
## Resultados (SAT, 3 solvers: Cadical153, Glucose4, MapleChrono; CP-SAT independiente con otra codificacion y sin rotura de simetria)
- N0(1)=9. **N0(2)=54** (53 coloreable, 54 UNSAT). **N0(3)=774** (773 coloreable, 774 UNSAT).
- Identicos con la variante x<y estricta (x>y>2 como en GS).
- Monotonia (restriccion de coloraciones) implica UNSAT para todo N>=N0; biseccion validada.
- Testigos (coloraciones sin par monocromatico) comprobados por verificador Python puro: witness_r2_N53.txt, witness_r3_N773.txt.
- Rotura de simetria: color(6)=0 (solo permutacion de colores); CP-SAT sin ella coincide.
- Hashes SHA-256: hashes.json. CNFs: n0_r*_N*.cnf. Scripts: n0.py, n0b.py, n0c.py, verify.py.
## Limitaciones
- No hay certificado DRAT: no hay drat-trim/cadical binario. La UNSAT se apoya en 4 solvers/2 codificaciones, no en prueba comprobada. Pendiente G3 (instalar drat-trim, o Lean).
- Mensaje espurio "c found falsified original clause" de pysat/Cadical153 durante n0.py (salida de depuracion); resultados confirmados por Glucose/Maple/CP-SAT.
- Importancia esperable 3: dato computacional pequeno; no mejora la cota asintotica.
## Siguiente
DRAT; calcular N0(4) (probable alcanzable); sin Green 24/37 por ahora.

## Cierre de verificacion (21-10-2026, segunda pasada)
### Pruebas DRUP (Glucose4 con_proof) y comprobador RUP independiente
- Instancias: CNF SIN rotura de simetria (n0_r2_N54.cnf, n0_r3_N774.cnf; 3 literales-color por numero, clausula "al menos un color" y "no mismo color" por par). Pruebas: n0_r2_N54.drup (1 lema), n0_r3_N774.drup (2133 lineas; borrados ignorados).
- Comprobador: rupcheck2.py (propagacion unitaria con 2 literales vigilados, escrito esta sesion; independiente de pysat; NO es drat-trim). Resultado: VERIFICADO en ambas (N=54: 1 lema; N=774: 2132 lemas, conflicto a nivel 0).
- Pruebas falsas rechazadas: clausula vacia directa en 774 (RUP FAIL), clausula vacia contra el CNF satisfacible N=53 (RUP FAIL), proof sin su primera mitad (RUP FAIL), lema falso "1 0" antepuesto (RUP FAIL), y la prueba de 774 contra el CNF de 773 (RUP FAIL en lema 1397).
- Limite: el comprobador de RUP no es un verificador formalmente verificado (cake_lpr); confianza = codigo corto + pruebas negativas.
### Lean 4 (Green22.lean, nucleo, sin Mathlib, Lean 4.35.0)
Compila (exit 0, ~2 min): longitudes y rangos de los testigos; `good 53 (col w2)` y `good 773 (col w3)` por native_decide; `good 53` ademas por `decide +kernel` (sin confiar en el compilador); y busqueda exhaustiva con retroceso `exists_col 2 53 = true`, `exists_col 2 54 = false`, `exists_col 1 8 = true`, `exists_col 1 9 = false` por native_decide.
Honestidad: la busqueda es un programa Lean cuyo resultado se evalua con native_decide (confia en el compilador y en el codigo, no hay teorema "para toda coloracion" ligado formalmente a `search`). No se formalizo N0 de Mathlib/FC ni la correccion de `search`. N=774 (r=3) no se hizo en Lean. `decide +kernel` para 773 (G3k.lean) NO termino en 25 min (timeout, exit 124): el testigo de 773 solo esta comprobado por native_decide y Python.
### Afirmacion exacta establecida
Con la definicion Lean de FormalConjectures (Green22.N0 r = sInf{N | toda c: Icc 1 N -> Fin r tiene x,y>=3, x+y, x*y in [1,N], mismo color}, x=y permitido; es el menor N, y como la propiedad es monotona en N, es el umbral):
- N0(1)=9, N0(2)=54, N0(3)=774.
- Cotas "N0(r) > N" (existe coloracion de [1,N]): rigurosas y comprobadas (Python, Lean native_decide; N=53 tambien en nucleo del kernel).
- Cotas "N0(r) <= N" (UNSAT en N): computacionales; para r=2 y r=3 hay prueba DRUP verificada por un comprobador RUP propio mas 4 solvers; r=2 ademas con busqueda exhaustiva en Lean (native_decide). No hay LRAT/drat-trim ni prueba en Lean-kernel de UNSAT.
### Falta
drat-trim/cake_lpr; UNSAT de 774 en Lean; enlazar `search` con el enunciado de FC (teorema de correccion); N0(4); busqueda de antecedentes mas profunda (MathSciNet/OEIS directo); revision adversarial (G5); no se ha escrito PDF.
