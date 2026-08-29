# Auditoría hostil final de reproducibilidad y consistencia — ARR v3

Fecha: 29 de agosto de 2026  
Objeto auditado: `work/neuron_paper_v3/src/main.tex`, PDF compilado, `repro/`, certificados y figuras.  
Restricción respetada: no se editó `main.tex`.

## Veredicto

**PASS técnico para el candidato de publicación.** No encontré un fallo en los replays, las constantes \(C_p\), el lower bound de complejidad, la extensión uniforme de corona, las referencias internas ni la frontera de claims sobre estimación.

**HOLD obligatorio post-publicación:** a la hora de esta auditoría, la URL ARR citada sirve aún la versión v2. Después de publicar v3 hay que comprobar que la página estable muestra v3, el título nuevo, el SHA-256 canónico del PDF efectivamente publicado y los assets de fuente/replay/auditoría. Ésta es una condición de secuencia externa, no un defecto matemático del candidato local.

Hay una observación editorial menor no bloqueante: el panel de probabilidad de slab recorta la curva exacta a \(10^{-8}\) sin identificar explícitamente ese suelo gráfico.

## 1. Entorno y ejecución independiente

Entorno observado:

| componente | versión |
|---|---:|
| Python | 3.12.6 |
| NumPy | 2.5.1 |
| SciPy | 1.18.0 |
| Matplotlib | 3.11.1 |
| python-flint | 0.9.0 |
| LuaTeX | 1.24.0, MiKTeX 25.12 |

Las cuatro dependencias Python coinciden exactamente con `repro/requirements.txt`.

Se ejecutaron desde un entorno limpio de proceso:

```text
python repro/verify_saturation_law.py
python repro/finite_sample_phase_diagram.py
python repro/verify_v3_additions.py
```

Resultado: los tres procesos terminaron con código cero. El primer replay certificó el witness Arb, momentos, jets, puentes, tres realizaciones de bloques y brackets finitos. El segundo regeneró la figura de resolución con semilla `2026082917`, \(d=12\), \(r=6\), 320 repeticiones y tamaños

```text
18, 36, 72, 144, 288, 576, 1152.
```

El tercero recalculó \(C_1,C_2\), los coeficientes del lower bound, \(Q_R\) gaussiano y los límites de esfera fija.

### Hashes antes y después del replay

Los hashes fueron idénticos antes y después:

| artefacto | SHA-256 |
|---|---|
| `figures/saturation_law.pdf` | `093d683fcc2b2a344255920ce0055641f694a91e37f767a9c580bd2bf0aadb97` |
| `repro/saturation_certificate.json` | `b40a9bb318b48206fc0c5c9fc592c7b699d48a26b9b12b4ecc4805cf6215b9d1` |
| `figures/finite_sample_resolution.pdf` | `358eecd0dd8e75568c4916c594b056df7232db610a5e6b49f48ef67af7c3d0fa` |
| `repro/finite_sample_resolution.json` | `4bd3e130d11670c3a51d51ff0a4d962078ae415e95f4e90260e23da9293f9def` |

Coinciden con los cuatro valores declarados en `repro/README.md`.

## 2. Close-out del README de build

### Hallazgo inicial

La primera versión auditada decía ejecutar `lualatex` sobre `src/main.tex` desde la raíz del manuscrito. Esa invocación no resolvía `../figures/saturation_law.pdf`, porque las rutas gráficas están escritas para un directorio de trabajo `src/`.

### Reauditoría del fix

El README actual dice explícitamente cambiar a `src/` y ejecutar `lualatex main.tex` tres veces, y advierte que la invocación desde la raíz no resuelve las figuras. **Fix PASS.**

Con

```text
SOURCE_DATE_EPOCH=1787961600
FORCE_SOURCE_DATE=1
```

se ejecutaron tres pases desde `src/`, seguidos de un cuarto pase de control. Resultado:

- 22 páginas;
- cero warnings LaTeX, referencias indefinidas, labels duplicados, `Overfull` o `Underfull`;
- el hash del cuarto pase coincidió con el del tercero;
- hash local al cierre auditado: `c66007bd4c9bcda8a8a8b04bfb724ab4f25a760554152e0d0c08aa3ace1f8ba0`.

Este hash es una evidencia del toolchain local, no una promesa de identidad binaria entre distribuciones TeX no fijadas. Para una reclamación fuerte de byte-reproducibilidad pública conviene registrar también la versión de LuaTeX/MiKTeX y el SHA del PDF de release.

## 3. Revisión independiente de \(C_p\)

El script define

\[
a_0=\frac{\varphi(0)m_0(p)}2,\qquad
b_0=\frac{\varphi(0)m_2(p)}2,
\]

y usa los envelopes del manuscrito para escribir, con

\[
s=d+\log(12/\delta),\quad
x=\sqrt{rs/n},\quad y=rs/n,
\]

\[
\frac{e_T}{\alpha}\le a_Tx+b_Ty,qquad
\frac{e_R}{\beta}\le a_Rx+b_Ry,qquad
\frac{q_n}{\sqrt{\alpha\beta}}\le a_Qx+b_Qy.
\]

La absorción del término \(x^{3/2}\) en \(x\) es válida porque la condición final implica \(x\le1\). Los factores usados en el script se obtienen correctamente de

\[
u_0=(d-1)\log9+\log(12/\delta)\le \log9\,s
\]

y de \(\sqrt m+\sqrt{2t}\le(1+\sqrt2)\sqrt s\).

Para el gap,

\[
\alpha-\beta\ge a_0/r,qquad
\frac{e_T+e_R}{a_0/r}
\le 2\frac{e_T}{\alpha}+\frac23\frac{e_R}{\beta},
\]

que explica exactamente `a_gap` y `b_gap`. La elección

\[
C_p=\left\lceil\max\{1,4a^2,b,4a_{\rm gap}^2,b_{\rm gap}\}\right\rceil
\]

garantiza tanto \(\varepsilon_n\le\varepsilon\) como \(e_T+e_R\le(\alpha-\beta)/2\) para \(0<\varepsilon\le1/2\).

Valores recalculados:

| \(p\) | \(R_p\) | \(C_p^{\rm raw}\) | \(C_p\) | \(C'_p\) |
|---:|---:|---:|---:|---:|
| 1 | 3.71718255692737 | 22928.076528193553 | 22929 | 22.479248806962307 |
| 2 | 2.1530165380915105 | 294161.04736338166 | 294162 | 52.36896222874753 |

Coinciden con la tabla del manuscrito y el replay. Una búsqueda numérica adversarial sobre \(d\in\{2,3,10,100\}\), confidencias desde \(0.999999\) hasta \(10^{-6}\), varios \(r/R_p\) y \(\varepsilon\) no encontró violación; las constantes son muy conservadoras.

**Resultado \(C_p\): PASS.**

## 4. Matching lower complexity

Se rederivaron los tres pasos Paley--Zygmund.

1. Para \(S_0=\sum W_i^2\), si \(n\gamma_0\ge H^2\),
   \[
   \mathbb P\{S_0\ge n\gamma_0/2\}\ge1/8.
   \]
2. Condicionalmente en los pesos, \(T_0=\sum W_i^2Y_{i1}^2\) satisface \(\mathbb ET_0^2\le3S_0^2\), luego
   \[
   \mathbb P\{T_0\ge S_0/2\mid W\}\ge1/12.
   \]
3. La norma de los \(d-2\) elementos restantes de la columna off-diagonal es una chi-cuadrado condicional, y
   \[
   \mathbb P\{\chi^2_{d-2}\ge(d-2)/2\}\ge1/12.
   \]

El producto es \(1/1152\), y en ese evento

\[
\|C/\alpha-I\|_{\rm op}
\ge\sqrt{\frac{(d-2)\gamma_0}{8n\alpha^2}}.
\]

La cota finita

\[
\frac{\gamma_0}{\alpha^2}
\ge \frac{m_0(2p)}{2\varphi(0)m_0(p)^2}r
\]

produce el coeficiente de la ecuación explícita. El replay devuelve

\[
\frac1{96\varphi(0)}=0.02611071119407292
\]

para \(p=1\), y

\[
\frac9{560\varphi(0)}=0.04028509727085537
\]

para \(p=2\).

El argumento de confianza mediante una entrada off-diagonal gaussiana condicional da correctamente \(r\varepsilon^{-2}\log(1/\delta)\), y la combinación con el término dimensional usa \(\max\{a,b\}\ge(a+b)/2\). El texto mantiene las restricciones \(r\) grande, \(d\ge3\), \(\delta\le\delta_p\), y especifica que se trata de pérdida bilateral relativa pointwise, no de un lower bound minimax de estimación.

**Resultado lower complexity: PASS.**

## 5. Uniform shell

Se verificaron las constantes y cada transición de la red:

- \(h'_p=p h_p(1-2\sigma)\), de modo que \(\|h'_p\|_\infty\le L_p=p4^{-p}\);
- \(\mathbb E\|X\|^3\le[\mathbb E\|X\|^4]^{3/4}=[d(d+2)]^{3/4}\);
- con probabilidad \(1-\delta/2\), \(\max_i\|X_i\|\le B_{n,\delta}\);
- la red de la corona tiene cardinal a lo sumo \((1+4R/\eta)^d\);
- para \(R\le\|w\|\le2R\), \(\lambda_{\min}G_p(w)\ge b_pR^{-3}\), con \(b_p=\varphi(0)m_2(p)/16\);
- aplicar el corolario pointwise con error \(\varepsilon/8\), fallo \(\delta/(2N)\) y radio a lo sumo \(2R\) multiplica la constante por \(2\cdot8^2=128\), exactamente el factor de la condición uniforme;
- el traslado net--punto cuesta \(\varepsilon/32\) para \(D_n\) y \(G_p\), y
  \[
  \frac\varepsilon8(1+\varepsilon/32)+\frac\varepsilon{32}<\varepsilon.
  \]

La dependencia implícita de \(N\) en \(n\) sólo pasa por \(B_{n,\delta}\) y está declarada. No se reclama optimalidad del logaritmo.

**Resultado uniform shell: PASS.**

## 6. Labels, citas, metadatos y frontera de estimación

Comprobación sintáctica del fuente más una compilación estable:

```text
labels duplicados: 0
refs/eqrefs sin label: 0
bibitems duplicados: 0
citas sin bibitem: 0
warnings LaTeX: 0
```

El título y autor del metadata PDF coinciden con portada y fuente:

```text
The Schwarzian Bridge in a Single Sigmoid Neuron:
Sharp Empirical Complexity and Global Spherical Saturation
Lluis Eriksson
```

Los `pdfkeywords` son válidos, aunque no están completamente sincronizados con la lista visible: omiten `spherical design` y `finite-sample concentration`. Esto es cosmético.

La frontera estimator/oracle es correcta y aparece en todos los lugares materialmente relevantes:

- para \(p=1\), el Gram es exactamente el Hessiano logístico y no usa labels;
- para \(p\ne1\), se denomina sensibilidad Gram, no Hessiano de la likelihood Bernoulli;
- el lower bound es pointwise para un teacher fijo y pérdida Loewner bilateral;
- el teorema uniforme no se convierte en garantía de estimador;
- se cita expresamente que Chen--Mazumdar ya construyen estimadores etiquetados minimax, incluido el esquema dirección/norma con corrección de sesgo.

**Resultado frontera de claims: PASS.**

## 7. Certificados y figuras

El certificado principal tiene schema `single-sigmoid-geometry-certificate-v3`. El certificado finito tiene schema `arr.finite-sample-resolution.v1` y sus campos coinciden con script, caption y figura.

Se renderizaron visualmente las 22 páginas del PDF y las dos figuras en resolución ampliada. No se observaron textos cortados, solapes, glifos rotos ni tablas fuera de margen. Las figuras son legibles e incorporan las muestras, repeticiones, ejes y distinción mediana/percentil 90 declaradas.

### Hallazgo menor: suelo no declarado de la curva exacta

En `finite_sample_phase_diagram.py`, la curva exacta se dibuja como

```python
np.maximum(exact, 1e-8)
```

pero la leyenda sólo dice `exact Gaussian probability`. Los valores exactos del certificado para \(n=144,288,576,1152\) son aproximadamente

```text
1.3193e-9, 1.7406e-18, 3.0296e-36, 9.1782e-72,
```

mientras que la gráfica muestra un plateau en \(10^{-8}\). El certificado es correcto y los puntos de frecuencia cero sí están identificados como plotting limit; falta identificar el clipping de la curva exacta. Recomendación no bloqueante: etiquetar `exact probability (clipped at 1e-8)` o ampliar el eje.

**Resultado visual/certificados: PASS con observación menor.**

## 8. Verificación ARR post-publicación

En la auditoría, `https://arr-research.github.io/papers/ARR-2026-53CTRKDSP685PT51/` respondió `200 OK`, pero mostró:

- título v2: *Spherical Inputs, All-Power Laws, and Empirical Resolution*;
- versión visible: v2;
- SHA canónico v2: `32bd46179e26475b5563666f2fc4a1230fdb5fcd77643db8d6f7850963952d90`;
- historial v1/v2, sin v3.

Eso es esperable antes de publicar, pero significa que las frases en presente sobre el registro público todavía no describen los nuevos teoremas locales. Tras el release v3 hay que verificar, como condición de cierre:

1. que la página estable seleccione v3;
2. que el título sea el nuevo;
3. que el SHA canónico coincida con el PDF publicado, no necesariamente con un PDF recompilado después;
4. que el release incluya fuente, `requirements.txt`, los cuatro scripts, los dos JSON, las dos figuras, README, auditorías y manifest;
5. que los cuatro hashes declarados sigan coincidiendo al descargar y repetir.

Hasta completar esa verificación, el estado es **PASS técnico / HOLD de publicación**. Si los cinco puntos pasan, el veredicto final se convierte en **PASS integral** sin requerir un nuevo cambio matemático.

## Resumen de close-outs

| ítem | estado |
|---|---|
| tres replays | PASS |
| cuatro hashes declarados | PASS |
| \(C_1,C_2,C'_1,C'_2\) | PASS |
| matching lower theorem | PASS |
| uniform shell theorem | PASS |
| labels/citas/compilación | PASS |
| metadata PDF interna | PASS |
| frontera oracle/estimator | PASS |
| fix README `cd src` | PASS |
| figuras/certificados | PASS, observación menor |
| registro ARR v3 | HOLD hasta publicación |

**Decisión operativa:** el candidato local puede publicarse. No declarar cierre reproducible integral hasta ejecutar la verificación ARR post-publicación.
