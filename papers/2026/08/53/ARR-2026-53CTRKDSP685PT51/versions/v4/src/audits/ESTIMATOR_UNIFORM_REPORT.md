# Informe de frontera: estimador etiquetado frente a uniformidad en \((r,u)\)

Fecha de auditoría: 29 de agosto de 2026. No se modificó `src/main.tex`.

## Veredicto ejecutivo

**Ruta recomendada: B, pero en una forma estrecha y demostrable.** El sucesor proof-complete más fuerte que no reproduce de manera inmediata a Chen--Mazumdar, Chardon--Lerasle--Mourtada u Ostrovskii--Bach es una **concentración bilateral, de precisión \(1\pm\varepsilon\), uniforme sobre una corona global de parámetros y válida para todas las potencias \(h_p=\sigma'^p\), \(p>0\)**. Se da abajo un enunciado y una prueba completos. El precio de la prueba elemental por red es un logaritmo adicional. No debe presentarse como tasa óptima ni como la primera concentración uniforme de Hessianos logísticos.

**Ruta A no es una contribución principal defendible en el modelo Bernoulli-gaussiano actual.** Las tasas angular, radial y total, la MLE, el estimador explícito eficiente y hasta el esquema de muestra dividida «MLE para la dirección + MLE unidimensional para la norma + corrección de sesgo» ya están en la literatura primaria de 2024--2026. El Gram evaluado en \(w_*\) no produce por sí solo un estimador: sus pesos dependen del parámetro desconocido. Rehacer la localización de la MLE mediante score y Hessiano uniforme reproduce la arquitectura de Chardon et al. y Ostrovskii--Bach.

Por tanto:

- **B: PASS**, si el claim se limita al teorema global de corona, all-\(p\), bilateral y con precisión ajustable que se formula aquí.
- **A: FAIL como claim de novedad.** Puede añadirse sólo como interpretación exacta score--Fisher y como explicación de las escalas, citando resultados previos. Un nuevo teorema óptimo de estimación en el mismo modelo solaparía frontalmente la literatura actual.

## 1. Modelo y frontera bibliográfica

Sea

\[
X\sim N(0,I_d),\qquad Y\mid X\sim \operatorname{Bernoulli}(\sigma(w_*^\top X)),
\qquad w_*=Ru_*,\quad \|u_*\|=1,
\]

y sea la pérdida logística empírica

\[
L_n(w)=\frac1n\sum_{i=1}^n\{\log(1+e^{X_i^\top w})-Y_iX_i^\top w\}.
\]

Entonces

\[
\nabla L_n(w)=\frac1n\sum_i(\sigma(X_i^\top w)-Y_i)X_i,
\quad
\nabla^2L_n(w)=\frac1n\sum_i\sigma'(X_i^\top w)X_iX_i^\top.
\]

La literatura que fija la frontera es la siguiente.

1. **Chardon--Lerasle--Mourtada.** Para diseño gaussiano, su Teorema 6 prueba, si \(n\ge 1{,}200{,}000\,R(d+t)\), una cota inferior del Hessiano empírico uniforme en un elipsoide de Dikin alrededor de \(w_*\). Su lema de localización combina exactamente score en \(w_*\), cota uniforme inferior del Hessiano y comparación del Hessiano poblacional para obtener existencia y error de la MLE. Véanse el [artículo primario, Teorema 6](https://arxiv.org/html/2411.02137v3#S4.SS3) y el [esquema score--Hessiano, Lema 3](https://arxiv.org/html/2411.02137v3#S4.SS1).

2. **Ostrovskii--Bach.** Su análisis auto-concordante controla uniformemente Hessianos empíricos en el elipsoide de Dikin. En la ecuación (92) obtiene un sandwich bilateral de factor constante, \(0.09H(w_*)\preceq H_n(w)\preceq32H(w_*)\), en una vecindad local. Véase el [artículo primario](https://doi.org/10.1214/20-EJS1780).

3. **Chen--Mazumdar (GD).** Para el mismo modelo gaussiano bien especificado estudian GD sobre la pérdida logística, controlan uniformemente el gradiente por redes y peeling, usan los autovalores radial/tangencial del Hessiano poblacional y dan estimadores explícitos. Véanse el [resumen y contribuciones](https://arxiv.org/html/2606.21683#S1.SS2) y el [teorema de GD](https://arxiv.org/html/2606.21683#S2.SS1).

4. **Chen--Mazumdar (minimax).** Prueban la tasa minimax de norma \(\Theta(\sqrt{R^3/n})\), construyen un estimador eficiente con esa tasa y, al combinarlo con dirección óptima, obtienen
   \[
   \Theta\!\left(\sqrt{Rd/n}+\sqrt{R^3/n}\right)
   \]
   para el parámetro completo. Su algoritmo ya implementa muestra dividida, dirección por MLE, MLE unidimensional posiblemente mal especificada y una corrección U-estadística del sesgo. Véanse el [artículo y resumen de tasas](https://arxiv.org/html/2608.17260#S1) y el [algoritmo de norma](https://arxiv.org/html/2608.17260#S2.SS3).

5. **Hsu--Mazumdar.** Con temperatura inversa conocida y dirección unitaria desconocida, establecen regímenes de complejidad muestral y estimadores de dirección para diseño normal. Véase la [publicación primaria en COLT/PMLR](https://proceedings.mlr.press/v247/hsu24a.html).

El barrido del corpus público de Lluis Eriksson tampoco encontró un estimador logístico etiquetado o una prueba uniforme de paisaje reutilizable. Los repositorios neuronales existentes son implementaciones de juegos, no resultados matemáticos; los activos reutilizables son las rutinas de momentos/certificados y la disciplina de replay descritas en `work/neuron_paper/repo_synthesis.md`.

## 2. Ruta A: qué sí se deduce y dónde aparece el blocker

### 2.1 Identidad exacta score--Fisher

En \(w_*\), ponga

\[
S_n=\nabla L_n(w_*)=\frac1n\sum_i(\sigma(w_*^\top X_i)-Y_i)X_i.
\]

Condicionando en \(X_i\), cada sumando tiene media cero y

\[
n\,\operatorname{Cov}(S_n)
=\mathbb E[\sigma'(w_*^\top X)XX^\top]
=H_1(R,u_*).
\]

Ésta es la conexión exacta con el Hessiano. Es útil para interpretar las escalas, pero es la identidad de información de Fisher, no una contribución de prioridad.

Si \(\alpha(R)\asymp R^{-1}\) y \(\beta(R)\asymp R^{-3}\), la linealización formal \(-H_1^{-1}S_n\) tiene

\[
|\langle u_*,-H_1^{-1}S_n\rangle|=O_{\mathbb P}(\sqrt{R^3/n}),
\]

\[
\|P_{u_*^\perp}H_1^{-1}S_n\|=O_{\mathbb P}(\sqrt{Rd/n}),
\qquad
\sin\angle(w_* -H_1^{-1}S_n,u_*)=O_{\mathbb P}(\sqrt{d/(nR)}).
\]

La derivación es inmediata: la varianza radial del score es \(\beta/n\), cada varianza tangencial es \(\alpha/n\), y la inversión divide respectivamente por \(\beta\) y \(\alpha\). Estas son precisamente las escalas que la literatura reciente ya convierte en estimadores y lower bounds.

### 2.2 Por qué el paso de Gram oracle a estimador no es automático

El objeto del manuscrito,

\[
\widehat H_p(R,u_*)=\frac1n\sum_i\sigma'(Ru_*^\top X_i)^pX_iX_i^\top,
\]

no es calculable sin \((R,u_*)\). En particular,

\[
w_*-\widehat H_1(w_*)^{-1}\nabla L_n(w_*)
\]

es un **one-step oracle**, no un estimador medible a partir de los datos. Sustituir \(w_*\) por un piloto requiere probar simultáneamente:

1. que el piloto cae en una vecindad donde el Hessiano empírico permanece comparable;
2. control del score a lo largo del segmento piloto--verdad;
3. existencia/no separación para la MLE o estabilidad del algoritmo;
4. control del resto no lineal anisótropo.

Esos cuatro pasos son justamente la localización auto-concordante de Ostrovskii--Bach y el lema score--Hessiano de Chardon et al.; el control de trayectorias y gradientes también aparece en Chen--Mazumdar.

### 2.3 El estimador explícito elemental existe, pero es demasiado débil

Defina

\[
M_n=\frac1n\sum_i(Y_i-1/2)X_i,qquad
q(R)=\mathbb E[Z\sigma(RZ)]=R\,\mathbb E\sigma'(RZ).
\]

Por simetría y Stein,

\[
\mathbb E M_n=q(R)u_*,\qquad q'(R)=\mathbb E[Z^2\sigma'(RZ)]=\beta(R)\asymp R^{-3}.
\]

Así, un estimador totalmente explícito es

\[
\widehat u=M_n/\|M_n\|,qquad \widehat R=q^{-1}(\|M_n\|).
\]

Como \(|Y_i-1/2|=1/2\), concentración gaussiana vectorial da, con probabilidad al menos \(1-e^{-t}\),

\[
\|M_n-q(R)u_*\|\le C\sqrt{(d+t)/n}.
\]

Para \(R\ge1\), \(q(R)\) está separado de cero; por normalización y el teorema del valor medio, siempre que el lado derecho sea suficientemente pequeño,

\[
\sin\angle(\widehat u,u_*)\le C\sqrt{(d+t)/n},
\qquad
|\widehat R-R|\le C R^3\sqrt{(d+t)/n}.
\]

Esta construcción pierde un factor \(\sqrt R\) en ángulo y un factor \(R^{3/2}\) en norma frente a las tasas óptimas. La pérdida radial no es sólo de la prueba: si

\[
A=(Y-1/2)Z,
\]

entonces \(\mathbb E A^2=1/4\) y

\[
\operatorname{Var}(A)=1/4-q(R)^2\longrightarrow1/4-1/(2\pi)>0.
\]

Por tanto \(\|M_n\|\) tiene ruido radial de orden \(n^{-1/2}\), y al invertir \(q'(R)\asymp R^{-3}\) se obtiene inevitablemente \(R^3/\sqrt n\) para este estadístico.

### 2.4 Blocker matemático preciso para una ruta A novedosa

Un titular de estimación necesitaría superar o cambiar al menos una de estas fronteras:

- un nuevo modelo (por ejemplo, \(p\ne1\) acompañado de un experimento etiquetado genuino cuya información sea \(H_p\));
- un diseño no gaussiano con hipótesis verificables y tasas anisótropas nuevas;
- constantes finitas exactas o un régimen que los trabajos citados no cubran;
- un algoritmo más simple con una ventaja computacional demostrada y no sólo la misma tasa.

En el modelo actual, «MLE/ERM explícito + error angular/norma + conexión al Hessiano» ya está cubierto. Incluso la aparente alternativa «dirección piloto + MLE escalar» aparece literalmente en Chen--Mazumdar; su Lema 2.1 prueba que el error angular produce el sesgo

\[
R-r^\circ\asymp R^3(1-\langle\widehat u,u_*\rangle)
=\frac{R^3}{2}\|\widehat u-u_*\|^2.
\]

Por eso el blocker no es falta de técnica local: es **solapamiento de prioridad**. Integrar una nueva prueba de las mismas tasas debilitaría la novedad del ARR v3.

## 3. Ruta B: teorema uniforme global que sí es integrable

### 3.1 Enunciado proof-complete

Para \(p>0\), escriba

\[
h_p(s)=\sigma'(s)^p,quad
G_p(w)=\mathbb E[h_p(w^\top X)XX^\top],quad
\widehat G_{p,n}(w)=\frac1n\sum_{i=1}^nh_p(w^\top X_i)X_iX_i^\top.
\]

Sean

\[
m_2(p)=\int_{\mathbb R}s^2h_p(s)\,ds,qquad
b_p=\frac{\varphi(0)m_2(p)}{16},qquad
L_p=p4^{-p}.
\]

Sea \(R_p\) el umbral finito del corolario puntual del manuscrito, de modo que para \(r\ge R_p\),

\[
\lambda_{\min}G_p(ru)=\beta_p(r)
\ge \frac{\varphi(0)m_2(p)}{2r^3}.
\]

**Teorema (corona global, all-\(p\), precisión relativa ajustable).** Fije \(R\ge R_p\), \(0<\varepsilon\le1/2\), \(0<\delta<1/2\), y defina

\[
B_{n,\delta}=\sqrt d+\sqrt{2\log(2n/\delta)},qquad
\mu_{3,d}=\mathbb E\|X\|^3\le[d(d+2)]^{3/4},
\]

\[
A_{p,n,\delta}=L_p(B_{n,\delta}^3+\mu_{3,d}),qquad
\eta=\min\left\{R,\frac{\varepsilon b_p}{32A_{p,n,\delta}R^3}\right\},
\]

y

\[
N=\left(1+\frac{4R}{\eta}\right)^d.
\]

Sea \(C_p\) cualquier constante válida en el corolario puntual

\[
n\ge C_p\,r[d+\log(12/\delta_0)]/\varepsilon_0^2.
\]

Si

\[
n\ge
128C_p\,\frac{R}{\varepsilon^2}
\left[d+\log\left(\frac{24N}{\delta}\right)\right],
\tag{U}
\]

entonces, con probabilidad al menos \(1-\delta\), simultáneamente para todo

\[
w\in\mathcal A_R:=\{w\in\mathbb R^d:R\le\|w\|\le2R\},
\]

se tiene

\[
(1-\varepsilon)G_p(w)\preceq\widehat G_{p,n}(w)
\preceq(1+\varepsilon)G_p(w).
\tag{UG}
\]

La condición es completamente computable, aunque implícita en \(n\) mediante \(B_{n,\delta}\). En notación de orden, una condición suficiente de la misma prueba es

\[
n\gtrsim_p\frac{R}{\varepsilon^2}
\left\{
d\log\left(2+\frac{R^4[d+\log(n/\delta)]^{3/2}}{\varepsilon}\right)
+\log(1/\delta)
\right\}.
\]

No se afirma que el logaritmo de cobertura sea necesario.

### 3.2 Prueba

Primero,

\[
h_p'(s)=p\,h_p(s)(1-2\sigma(s)),
\]

por lo que \(\|h_p'\|_\infty\le p4^{-p}=L_p\). Para cualesquiera \(w,v\),

\[
\|h_p(w^\top x)xx^\top-h_p(v^\top x)xx^\top\|_{\rm op}
\le L_p\|w-v\|\,\|x\|^3.
\tag{1}
\]

La concentración de la norma gaussiana y una unión sobre \(i\le n\) implican, con probabilidad al menos \(1-\delta/2\),

\[
\max_{i\le n}\|X_i\|\le B_{n,\delta}.
\tag{2}
\]

En ese evento, si \(D_n(w)=\widehat G_{p,n}(w)-G_p(w)\), (1) da

\[
\|D_n(w)-D_n(v)\|_{\rm op}
\le A_{p,n,\delta}\|w-v\|.
\tag{3}
\]

Además,

\[
\|G_p(w)-G_p(v)\|_{\rm op}
\le L_p\mu_{3,d}\|w-v\|.
\tag{4}
\]

Tome una \(\eta\)-red \(\mathcal N\subset\mathcal A_R\). Como \(\mathcal A_R\subset2R B_2^d\), puede elegirse con

\[
|\mathcal N|\le(1+4R/\eta)^d=N.
\tag{5}
\]

Aplique el corolario puntual en cada \(v\in\mathcal N\) con precisión \(\varepsilon/8\) y fallo \(\delta/(2N)\). Puesto que \(R\le\|v\|\le2R\), (U) garantiza todas las condiciones puntuales. Una unión proporciona, con probabilidad al menos \(1-\delta/2\),

\[
|x^\top D_n(v)x|\le\frac{\varepsilon}{8}x^\top G_p(v)x
\quad\text{para todo }v\in\mathcal N,\ x\in\mathbb R^d.
\tag{6}
\]

Para todo \(w\in\mathcal A_R\), la cota radial del manuscrito y \(\|w\|\le2R\) dan

\[
\lambda_{\min}G_p(w)\ge b_pR^{-3}.
\tag{7}
\]

Elija \(v\in\mathcal N\) con \(\|w-v\|\le\eta\). Por (3)--(4), (7) y la definición de \(\eta\),

\[
\|D_n(w)-D_n(v)\|_{\rm op}
\le\frac{\varepsilon}{32}\lambda_{\min}G_p(w),
\tag{8}
\]

\[
\|G_p(w)-G_p(v)\|_{\rm op}
\le\frac{\varepsilon}{32}\lambda_{\min}G_p(w).
\tag{9}
\]

De (9),

\[
G_p(v)\preceq(1+\varepsilon/32)G_p(w).
\tag{10}
\]

Finalmente, para cualquier \(x\), (6), (8) y (10) implican

\[
|x^\top D_n(w)x|
\le\left[\frac{\varepsilon}{8}(1+\varepsilon/32)+\frac{\varepsilon}{32}\right]
x^\top G_p(w)x
\le\varepsilon x^\top G_p(w)x.
\]

Esto equivale a (UG). Los dos eventos usados fallan con probabilidad total a lo sumo \(\delta\). \(\square\)

## 4. Qué es nuevo en B y qué debe rebajarse

La combinación exacta no localizada en la búsqueda dirigida es:

- corona **global** \(R\le\|w\|\le2R\), no sólo elipsoide de Dikin alrededor de una verdad fija;
- simultaneidad completa en radio y dirección;
- precisión bilateral \(1\pm\varepsilon\), no sólo factores constantes;
- todas las potencias \(p>0\), con constantes reducibles a los momentos Gamma/poligamma ya certificados en la línea.

Sin embargo, deben mantenerse estas rebajas:

1. No decir «primera concentración uniforme de Hessianos logísticos»: Ostrovskii--Bach y Chardon et al. tienen resultados uniformes anteriores.
2. Para \(p=1\), llamarlo **extensión global de corona y precisión ajustable por una prueba elemental**, no una nueva tasa óptima. Chardon obtiene la cota inferior local con el escalado óptimo \(R(d+t)\), sin el logaritmo de red.
3. Para \(p\ne1\), \(\widehat G_{p,n}\) es un Gram de sensibilidad, no el Hessiano de la likelihood Bernoulli estándar. No usar lenguaje MLE/Fisher salvo \(p=1\) o salvo que se defina otro experimento estadístico.
4. (UG) no da por sí sola error de estimación: faltan labels, score, localización y existencia del minimizador.
5. La prueba usa truncación mediante \(\max_i\|X_i\|\), por lo que sus constantes y logaritmos son conservadores. Mejorarlos requeriría PAC-Bayes, chaining o un proceso matricial localizado, no sólo reciclar la prueba puntual.

## 5. Recomendación de integración para ARR v3

El añadido defendible sería una sección corta titulada, por ejemplo, **“Uniform all-power sensitivity on a global parameter shell”**, con:

1. el teorema (UG) y su prueba;
2. un corolario \(p=1\) que identifique \(\widehat G_{1,n}(w)=\nabla^2L_n(w)\), explícitamente label-free;
3. una comparación frontal con el Teorema 6 de Chardon y la ecuación (92) de Ostrovskii--Bach;
4. una frase de limitación: no es un teorema de MLE, ni pretende mejorar la tasa minimax;
5. un replay numérico que maximice el error relativo sobre una malla declarada de radios y direcciones, etiquetado como diagnóstico finito y no como prueba de la supremacía continua.

La identidad score--Fisher de la Sección 2.1 puede añadirse como corolario interpretativo para explicar por qué los autovalores \(R^{-1}\) y \(R^{-3}\) producen las escalas angular y radial conocidas. Debe ir acompañada de las citas de Chardon y Chen--Mazumdar y no presentarse como estimador nuevo.

## Decisión final

**Persistir con B.** El teorema de corona global all-\(p\) es reproducible, encaja con la línea algebraica existente y añade una afirmación genuinamente más uniforme que el resultado puntual sin invadir las tasas estadísticas ya ocupadas.

**No persistir con A en el modelo actual**, salvo que se cambie sustancialmente el experimento o se descubra una ventaja algorítmica demostrable. El blocker es tanto matemático (un Gram oracle no localiza un estimador) como de prioridad (la construcción y las tasas objetivo ya fueron publicadas en forma más fuerte).
