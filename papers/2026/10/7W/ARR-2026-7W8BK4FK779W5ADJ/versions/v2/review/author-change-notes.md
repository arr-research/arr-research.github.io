# CAMBIOS v1 -> v2 (21-10-2026)

Base: `D:\Entregas\airr\2026-10-18_frontera-lyapunov\candidate-1` (v1, sha bec07a6e...). Esta copia: `C:\Trabajo\investigador-airr\v2\lyap-frontera`. D: no se ha tocado.
Los enunciados y resultados del teorema principal NO cambian. No se afirma nada nuevo salvo lo listado como "ampliación demostrada".

## Hecho
1. **Novedad frente a Liu-Fitzsimmons (arXiv:2607.16171v1, texto completo leído, única versión el 21-10).** Lo que prueban: familia (27)-(28) con H=r^2 e^{-b sin2θ} y estabilidad global para todo a>0, b real (Sec. IV-D); Teorema IV.3: para a>0, |b|>=2(a+1) no existe polinomio homogéneo definido positivo con L_fP<=0 (solo polinomios; cota |b|/2<a+1 vía |g_2|<1, Lema III.3); no analiticidad local solo para el campo (1,5) (Teor. II.2(4)). **Corregido v1:** v1 les atribuía también la no existencia analítica local en toda la región |b|>=2(a+1); ahora se dice que el argumento de término principal se transfiere (Sec. 6) pero no lo enuncian para la familia. Cita de factorización: v1 decía "Lemas III.2-III.3"; ahora Lema III.2 (y la prueba del III.3), y se añade prueba directa corta. Nuevo Remark 2: (1+a^{2/3})^{3/2} < sqrt2 (1+a) < 2(1+a), umbral estrictamente dentro de la cota previa. Verificados contra texto: Ahmadi-Parrilo Thm 4.3 y 5.3 (el 5.3 da SOS de grado posiblemente mayor; ahora se dice), Ahmadi-El Khadir Prop. 6.1 (= Prop. VI.1 en Liu). No leídos enteros.
2. **Lema 3 (ahora Lema 4)**, reescrito en 5 pasos con pruebas: factorización de Möbius de M_c, rama de f_c, constante h_c(0)=1, arcos (M_c = c^2-1-2c cot(ψ/2) creciente), y |q_c/f_c| = (s^3/2)|z-η^3|^{1/2}|z-η̄|^{3/2}/|z| (órdenes 1/2 y 3/2, continuidad en el cierre, principio del mínimo). Comprobado con mpmath (40 dígitos, 5 valores de c).
3. **Proposición 5 (ahora 7), compacidad**: prueba completa (isomorfismo formas binarias <-> polinomios trigonométricos, límite con derivadas, lema del factor integrante separado como Lema 6).
4. **Corolario 6 (ahora 8)**, k>=2, ω<0, b<0: reducciones explícitas (escala de tiempo, reflexión, giro π/(2k)), fórmula de L_fP, necesidad para k general (identidades F+HG=c, <G cos kφ>=σc/s), suficiencia con productos de formas binarias, caso analítico local, estabilidad. Comprobado numéricamente en cartesianas (k=1,2,3, ω<0, b<0; N=1024; L_fP/(2kNP)<0 en 20001 ángulos). Observación d sin2θ ahora justificada por giro γ/2. Remark de coeficientes racionales aclarado (no hace falta f racional).
5. **Cota explícita de grado para todo b>=0** (Prop. 4 ahora 5): se define a_*(b)=(max{b^{2/3}-1,0})^{3/2}; para b<=1 la función crítica 1-ibz (a_*=0) con medida sin átomos; cota N<=ceil(256πb^2/δ^3) si δ<=2b y N<=max(1,ceil(32π/δ)) si δ>2b (incluye b=0). Los pasos de la prueba (cota ∂_tK, error de cuantiles) escritos completos. Resumen del abstract: "para b fijo".
6. **Numérica**: se mantiene solo el ejemplo de 2048 factores, etiquetado como anecdótico (con script check_phase30.py y su salida en el suplemento v1). El párrafo de relajaciones de Toeplitz se retira del texto (queda en el suplemento con aviso). Nuevo `check_v2.py` + salida JSON en `supplement.zip` (35 s). Sección de revisión ahora cita revisores Claude Sonnet 5.5 / Haiku 5.5 (no humanos, no independientes) y retira la mención de Astra y "mismo revisor involucrado".
7. Compilado con pdflatex (2 pasadas): 0 warnings, 0 referencias rotas, 11 páginas, todas revisadas como imagen (80 dpi).

## NO arreglado / límites
- Sigue sin haber tasa de grado mínimo emparejada ni selección de cuantiles certificada con enclosures.
- Sin verificación formal (Lean) ni revisión humana; las comprobaciones numéricas no son pruebas.
- Teoremas 4.3/5.3 de Ahmadi-Parrilo y Prop. 6.1 de Ahmadi-El Khadir comprobados solo en su enunciado/introducción, no en la demostración.
- Prioridad mundial no confirmada (búsquedas dirigidas).
- La numeración de teoremas/lemas comparte contador (Lema 3, Lema 4, Prop. 5...), distinta de la de v1 en los números.
- Hash/PDF/Zip: ver `sha256.txt`. Archivos obsoletos de v1 (manifiestos, ESTADO.json, visual-qa.json) NO copiados.
