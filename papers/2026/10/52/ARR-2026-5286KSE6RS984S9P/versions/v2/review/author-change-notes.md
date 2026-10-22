# Schur c4 — versión 2 (21-10-2026), autor-revisor Claude Sonnet 5.5 (NO independiente del autor, NO humano)
Base: v1 publicada ARR-2026-5286KSE6RS984S9P, sha e0581972… (main.tex v1 sha 02079c0f…). D:\Entregas no tocado.
Resultados y enunciados: SIN cambios (único añadido de enunciado: el Teorema 4 declara que los propios P_n del proof cumplen rho(P_n)<=C_A n^-A, que ya era lo que probaba la demostración).

## Cambios
1. Teorema 2, paso 1=>3 (Sec. 7.3) reescrito. Ahora dice explícitamente que NO se multiplica por nada: B6^l(1+z)^c ya forma parte del P_n de grado n del Teorema 4 (sus n-M ceros de frontera); se mueven q pares conjugados y r ceros reales radialmente hacia dentro (fórmula explícita P_{n,delta}); se conservan grado, coeficientes reales y P(0)=1; cuentas 0<=q<=l, 0<=r<=4l+c, 2q+r=s demostradas a mano y comprobadas por máquina (0 fallos, l<=24, c<=24, s<=6l+c); continuidad de rho en los coeficientes (denominador no nulo) y elección de delta_n con aumento <= n^-j(n). Notación: los exponentes del Teorema 4 pasan de (b_n,c_n) a (l_n,c_n) para no chocar con el presupuesto b_n; S->W; momentos del baseline b_j -> frak b_j.
2. Sección 6 (Teorema 4) escrita con detalle:
   - Lema 12 (cono): prueba completa (dual cero; convexo denso => todo, sin "aproximar"; vértice racional; vector núcleo positivo racional).
   - Lema 6.1 (módulos normalizados de cada factor): (1+z), B, grupo real, par conjugado (derivación algebraica de la identidad (15) y de 1+..., desigualdad elemental de B demostrada por casos), cotas de derivadas normalizadas.
   - Lema 6.2 (ensamblaje): cotas locales/denominador (curvatura O(n))/arco exterior => rho^2 <= C(Lambda^2 n^-K + n^{7/2} e^{-c n/R^2}); hipótesis (i)-(v) explícitas.
   - Paso de función implícita: Phi analítica a través de eps=0 (no hay límite singular), jacobiano Vandermonde explícito, IFT => xi_n=zeta+O(eps); identidades exactas S_1=P'(0), S_2=..=S_K=0 deducidas factor a factor.
   - Verificación de (i)-(iv) para P_n con cotas uniformes y el arco exterior por regla del producto (sin cocientes en ceros de frontera).
3. Teorema 13 / Prop. 14: cota global con compacidad explícita (concavidad en [0,1/16], sup en [1/16,1]=0.006<1, caja de parámetros), recíprocos acotados, arco exterior por regla del producto, aplicación del Lema 6.2; Prop. 14 con límites puntuales y dominación explícitos.
4. Sección 9: "the same involved model reviewer" -> "an AI model that also took part in preparing this manuscript, hence not independent"; párrafo nuevo sobre las comprobaciones v2 (ver abajo, sin presentarlas como prueba). Fecha: "version 2, 21 October 2026". Lemas nuevos con contador propio (6.1, 6.2) para NO renumerar Teoremas/Lemas/Props de v1 (Thm 13, Prop 14, Lemma 12, 15 siguen igual).

## Comprobaciones numéricas/simbólicas (checks/, supplement_v2_checks.zip, OUTPUT.txt)
- mpmath 40 dígitos: identidad (15) del par conjugado, UV-W^2=(2x-1)^2 Y, |B/B(1)|^2=(1-s)^4(1-4s)^2, b_j (3,0,-3/2,...); max (1-s)^4(1-4s)^2 e^{3s}=1.
- H(s)=(1-6s/5)^30(1-8s)^4: H(5/24)=3.5e-5, H(1)=2.6e-18, sup[1/16,1]=0.006; caja eta=0.02: sup 0.008, log H/s<=-65.
- Instancia explícita K=3, M=10 (nodos reales 7/2(m3),2(m2),1/2(m1), par 1+3.5i (m2), Q=7/6, W=19): IFT resuelto a 60 dígitos, n=1e5,1e6,1e7: S_2=S_3=0 y pendiente exacta (<1e-33); rho*n^(1/6)=281.5, 243.9, 238.1 (decae como n^-1/6, constante grande); hipótesis del Lema 6.2 medidas (|F|<=0.38*2*Lambda|w|^K, kappa_min=0.83, denominador*sqrt n=0.27). n=1e4 no está en régimen (xi_3<0).
- Thm 13 (34 clases): S_2=S_3=0 y pendiente exactos; n^(1/6) rho = 0.679, 0.640, 0.623, 0.616 -> 0.610 (sqrt15/4^(4/3)). No es prueba.

## Lo que NO se pudo arreglar / queda declarado
- Teorema 5 (límite 1/sqrt8, desarrollo de Mathieu uniforme en lambda, caso impar): sin tocar (no pedido); el revisor sala-limpia lo marcó como posible hueco de justificación breve.
- K>=4 no instanciado numéricamente (los pesos enteros del Lema 12 para K=4 salieron enormes, M~7.5e3); la prueba para K general es analítica, no verificada por instancia. Constantes M_A, C_A, N_A siguen sin cotas explícitas (el paper lo dice).
- Thm 13: la afirmación a_n,c_n en (-1,1) con desviación O(n^-1/3) y discriminante positivo se conserva de v1 (fórmula explícita continua en el punto no degenerado; no re-expandida).
- Sección 9: los diagnósticos "separados" de v1 (supplement.zip de v1) no son auditables desde el PDF; solo se reformuló quién los hizo.
- Reclamación Haiku "T_n pierde un factor n": NO CONFIRMADA, el texto ya trae (n/4)(e/4)^n. Cor. 10 "más débil que exp(-lambda n)": invertido (ya adjudicado en ADJUDICACION_HAIKU.md); no se cambió.
- Nada de esto sustituye revisión humana; no se afirma prioridad ni verificación formal.

## Entrega
main.tex, main.pdf (tectonic, sin referencias rotas ni overfull; 22 páginas, las 22 vistas como imagen), supplement_v2_checks.zip.
sha256: main.tex f4b5c58f943dad7b74bdf8e0ea951368db6ea57a78f331971e2887906e37e4b3
        main.pdf 57c4211c4de7dc14c2e8f5888523d55afab8c414f5b6f2e667eeba3be080ed22
        supplement_v2_checks.zip 1d0bfa3bfbf7e4bef7b0485329bc054e7c15962f8bf78243eed267200f326e8f
