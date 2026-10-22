# Gowers-Long F(n) <= n^{3/2} (arXiv 1609.08688, Conj. 1.8) - ronda 12, 21-10-2026
Autor: Claude Sonnet 5.5 (no humano, sin revision externa).

## G0
F(n) = longitud maxima de una sucesion de ternas en [n]^3 con a_i <_2 a_j para i<j (<_2: menor en >=2 coordenadas). Conjetura 1.8: F(n) <= n^{3/2} para todo n. Abierta. El articulo (Tabla 1, calculada por fuerza bruta) da F(1..5)=1,2,4,8,10 (G: 1,2,5,8,11); dice que n mayor no era factible. Busqueda web (2 consultas): ninguna verificacion 2024-26 ni entrada OEIS encontrada (no exhaustivo). => no abortar; F(6) y F(7) son nuevos respecto al articulo, salvo que existan en trabajo que no localice.
## Metodo
Reduccion: <_2 es antisimetrica, asi que el conjunto S debe ser 2-comparable y su torneo transitivo. Cota auxiliar valida: <=1 terna por cada par de coordenadas fijado (lema de Loh).
- dfs.py: fuerza bruta independiente (n<=5). cp.py: CP-SAT (OR-tools) con rangos. sat.py: SAT CaDiCaL (python-sat) con clausulas de ciclo perezosas (codificacion distinta). common.py: comprobador de certificados.
## Resultados (salidas en dfs_out.txt, cp_out.jsonl, sat_out.jsonl, cp7.json)
| n | F(n) | n^1.5 | metodo |
|1-5|1,2,4,8,10| | DFS = CP-SAT = articulo; SAT confirma n=5 (10 SAT, 11 UNSAT) |
|6| 14 | 14.70 | CP-SAT OPTIMAL (38.9 s); SAT: 14 SAT, 15 UNSAT (43.9 s). Dos solvers/codificaciones independientes. NUEVO |
|7| 17..19 | 18.52 | CP-SAT 2300 s: FEASIBLE 17, cota sup 19, NO resuelto. SAT "m=19" agotado (2350 s) sin respuesta |
Ningun valor viola n^{3/2}: F(4)=8=4^{3/2} (justo), F(6)=14<14.70. Con n=7 una violacion exigiria F(7)=19 (sin descartar ni encontrar).
Todos los certificados (secuencias) verificados con check_seq (definicion directa). UNSAT sin DRAT (no se pidio prueba; es limitacion): la verificacion de optimalidad es solo cruce de dos solvers.
## Intentos fallidos conservados
Primer lanzamiento de n=7 en segundo plano murio sin salida; sat.py fallo al principio por un comentario "encoding" (error de sintaxis Python); sat 7/19 timeout.
## Valoracion
Extension de tabla de 5 a 6 (7 parcial). Importancia esperable 3 (dato menor; no cierra nada, no refuta). Siguiente paso posible: simetrias (permutar coordenadas, complemento+inversion) y cota por pares para cerrar n=7; DRAT para n=6.

## Ampliacion (21-10-2026): F(7) = 17
Simetrias de la relacion <_2 (justificacion): (i) S3 sobre las 3 coordenadas (<_2 es simetrica en ellas); (ii) complemento a -> n+1-a junto con invertir la sucesion (a <_2 b <=> b' <_2 a'). No hay mas (las biyecciones de [n] que conservan el orden son la identidad). Solo se usa (i): el PRIMER elemento de la sucesion puede suponerse con coordenadas ordenadas (84 cubos para n=7), y para el cubo (1,1,1), que S3 fija, el SEGUNDO elemento tambien (77 subcubos). La particion por primer/segundo elemento es exhaustiva.
Validacion del metodo (cube.py, cube2.py): n=5: m=10 SAT, m=11 todos UNSAT; n=6: m=14 SAT, m=15 todos UNSAT (val_*.jsonl, val2_*.jsonl) = valores de CP-SAT/DFS.
Resultado n=7, m=18: los 83 cubos de primera terna (c7_18_cad_{0rest,1,2}.jsonl) y los 77 subcubos de (1,1,1) (c7_18_111_split.jsonl) son TODOS UNSAT con CaDiCaL; los mismos 160 cubos, UNSAT con MapleChrono (c7_18_map_*.jsonl, c7_18_111_split_map.jsonl); coinciden clave a clave. Con la sucesion de longitud 17 (cp7.json, verificada con check_seq) => **F(7)=17** < 7^{1.5}=18.52. Sin violacion de la Conjetura 1.8 (la cota tambien descarta 19). Salvedad: UNSAT sin DRAT; el codigo de cubos es uno solo (cube.py) y su correccion se apoya en la validacion n<=6 y en el acuerdo de dos solvers. No se escribio un segundo codigo independiente (no hubo longitud 19 que verificar).
Busqueda local/ILP desde 17 (cp_ls.py, 1 hilo, 2200 s, lb 18): UNKNOWN, sin aporte (intento conservado).
Tabla actual: F(1..7)=1,2,4,8,10,14,17 (n^{1.5}: 1,2.83,5.2,8,11.2,14.7,18.5). Importancia esperable 3.
PIDs lanzados en pids.txt; ninguno se mato por nombre.

## Fase final (21-10-2026): comprobacion independiente, DRUP, Lean, nota
- BnB independiente en Go (bnb.go, sin SAT): F(1..6)=1,2,4,8,10,14 (n=6: 473.802.276 nodos, 21 min). n=7 inviable con este codigo.
- DRUP (Glucose4): n=6,m=15: 452.559 lemas, aceptado por rup.go (Go, 14 min; conflicto tras 233.894 lemas). rupcheck2.py (Python) NO termino en 38 min. Ambos coinciden en una prueba de 2.905 lemas y rechazan las 4 pruebas falsas (falsos/) y, el de Go, la prueba de otro cubo contra la CNF.
- n=7, m=18: 471 trabajos DRUP (82 cubos de primera terna + 312 subcubos de (1,1,2) por segunda terna sin simetria + 77 subcubos sorteados de (1,1,1)); 46 refutados por conteo; 425 con prueba DRUP (71,5 M lemas). Verificados con rup.go: 407 de 425 (18,9 M lemas); 18 NO verificados (los mayores, 0,87-9,1 M lemas; presupuesto de 40 min). Cruce CaDiCaL/Maple en 160 cubos (grueso) sigue valiendo para todo.
- Bug propio: la primera pasada de cubos con dos ternas fijas (c11_*, s1_1_2__*) era contradictoria (se eliminaba la primera terna del conjunto) y daba UNSAT vacuo con 0 lemas; descartado (bogus/) y recalculado tras corregir proofcubes.py.
- Lean (lean/Gowers.lean, 4.35.0): testigos 14 y 17 por native_decide y decide +kernel; exit 0; un testigo falso se rechaza.
- Nota: C:\Trabajo\investigador-airr\notas\gowerslong (main.tex/pdf, supplement.zip, CAMBIOS.md, sha256.txt).
