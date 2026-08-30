## Nueva nota: **3.90/10.00**

Antes le di **2.70/10.00**. Esta versión sube **+1.20 puntos**. Mi intervalo razonable sería **3.55–4.25**, pendiente de una revisión formal por especialistas y de una búsqueda exhaustiva de prioridad.

En una escala académica convencional —donde 10 es un paper extraordinario dentro de su área, no un Problema del Milenio— lo situaría aproximadamente en **8.2/10**.

La mejora es **sustantiva, no cosmética**.

## Por qué sube tanto

### 1. Ahora sí resuelve el principal hueco de la versión anterior

La v1 reconocía explícitamente que la curvatura poblacional no decía cuándo una muestra finita podía resolver el modo radial \(r^{-3}\), y dejaba esa concentración como el sucesor natural. 

La v2 incorpora precisamente eso. El Teorema 7.1 da, para el Gram ponderado empírico:

$$
\widehat H_{h,n}
=
\frac1n\sum_{i=1}^n h(ru^\top X_i)X_iX_i^\top,
$$

control separado del bloque tangencial, la entrada radial y el término cruzado; después obtiene una aproximación relativa bilateral en orden de Löwner,

$$
(1-\varepsilon_n)H_h
\preceq
\widehat H_{h,n}
\preceq
(1+\varepsilon_n)H_h,
$$

junto con error del autovalor radial y ángulo del autoespacio radial.  

La consecuencia

$$
n\ge
C_p\frac{r[d+\log(12/\delta)]}{\varepsilon^2}
$$

es una afirmación finito-muestral concreta y matemáticamente relevante. Además, el argumento del slab vacío prueba una necesidad separada de orden \(r\log(1/\delta)\), y se reconoce honestamente que todavía no hay una cota inferior producto \(\Omega(rd)\). 

Esta es la principal razón de la subida.

### 2. El “puente” ya no es solamente gaussiano y asintótico

La extensión a inputs isotrópicos esféricamente simétricos introduce correctamente el multiplicador de cuarto momento

$$
q_X=\frac{\mathbb E\|X\|^4}{d(d+2)}
$$

y obtiene

$$
\kappa_{p,X}(r)
=
1-q_XpSg(0)r^2+O(r^4).
$$

Esto separa lo que realmente procede de simetría rotacional y momentos de lo que procede específicamente de independencia gaussiana. 

Además, el Teorema 5.2 convierte la identidad de límites en una desigualdad certificada a escalas finitas:

$$
\left|
\frac{\kappa_p(r)-1}{r^2}
+
\frac{6p}{g'(0)^2}
\frac{\det L_g(0,\delta)}{\delta^2}
\right|
\le
C_hr^2+
\frac{6pD_g}{g'(0)^2}|\delta|.
$$

Eso fortalece mucho la narrativa: ya no es solo “ambos coeficientes coinciden cuando \(r,\delta\to0\)”, sino una comparación cuantitativa falsable. 

### 3. La generalización de \(p=1,2\) a todo \(p>0\) está bien conseguida

Ahora hay una sola teoría para

$$
h_p(t)=\sigma'(t)^p,\qquad p>0,
$$

con transformada Gamma, momentos poligamma, monotonía estricta y expansiones en ambos extremos:

$$
m_0(p)=\frac{\Gamma(p)^2}{\Gamma(2p)},
\qquad
m_2(p)=2\psi_1(p)m_0(p),
$$

$$
\kappa_p(r)
=
1+\frac p2r^2-\frac p8r^4+
\frac{p(p+1)}{16}r^6+O(r^8),
$$

y

$$
\kappa_p(r)
=
\frac{r^2}{2\psi_1(p)}
+
1+\frac{\psi_3(p)}{4\psi_1(p)^2}
+O(r^{-2}).
$$

Esto elimina la sensación algo ad hoc de tratar por separado Bernoulli y squared loss.  

Revisé algebraicamente los coeficientes de la expansión pequeña y la cancelación del término cuadrático en \(p\) en el coeficiente de \(r^4\); son consistentes.

### 4. La defensa de prioridad es bastante más profesional

La tabla de prioridad distingue resultado previo, resultado actual y diferencia exacta. Esto reduce considerablemente el riesgo de que un revisor interprete como nuevas la descomposición gaussiana, el criterio Schwarziano o las concentraciones bilaterales previas. 

También se corrigió cuidadosamente la situación del preprint de Lam: se conserva v2 como proximidad histórica y se distingue de v3, que cambió de título y declara que corrige y reemplaza v1–v2. Esto coincide con el registro actual de arXiv.  ([arXiv][1])

La sección de reproducibilidad ahora enumera nueve comprobaciones y proporciona una dirección estable para los archivos, informes y manifiestos. 

## Auditoría matemática provisional

No detecto un fallo fatal en las nuevas cadenas principales.

En particular, son consistentes:

* Los restos \(M_4r^4/8\) y \(5M_4r^4/8\) del Teorema 5.2, que proceden de \(\mathbb EZ^4=3\) y \(\mathbb EZ^6=15\).
* La fórmula Gamma/poligamma y las expansiones de \(\kappa_p\).
* La descomposición del Gram empírico en bloques tangencial, cruzado y radial.
* La normalización que transforma los tres errores de bloque en la cota relativa de Löwner.
* El ángulo \(q_n/G\) mediante la ecuación del autovector y la separación entre el bloque tangencial y la entrada radial.
* El escalado de los errores relativos como

  $$
  \sqrt{\frac{r(d+\log(1/\delta))}{n}}
  +
  \frac{r(d+\log(1/\delta))}{n}.
  $$
* El argumento del slab vacío y su probabilidad exponencial en \(n/r\).

Eso no equivale a arbitraje formal línea por línea, pero esta versión soporta mucho mejor una lectura hostil que la anterior.

## Por qué todavía no pasa de aproximadamente 4

### El resultado empírico sigue siendo oracle y puntual

El Gram utiliza el teacher verdadero y un perfil de sensibilidad conocido. No es todavía un teorema sobre un estimador calculado a partir de etiquetas, sobre el MLE/ERM ni sobre la trayectoria efectiva de un algoritmo. Tampoco es uniforme en \(w\). El propio artículo lo delimita correctamente. 

Esto significa que el Teorema 7.1 resuelve “¿cuántas muestras necesita este Gram ponderado fijo para parecerse a su esperanza?”, no todavía “¿cuántas muestras y pasos necesita el procedimiento de aprendizaje para recuperar el parámetro?”.

### Falta determinar la complejidad finito-muestral óptima

Actualmente hay:

$$
n\gtrsim \frac{rd}{\varepsilon^2}
$$

como suficiencia, pero solo:

$$
n\ge d
\quad\text{y}\quad
n\gtrsim r\log(1/\delta)
$$

como necesidades separadas. No se sabe por el paper si el producto \(rd\) es realmente necesario o si la cota superior podría mejorarse. El manuscrito identifica correctamente este punto como el sucesor más fuerte. 

### La conexión global sigue dependiendo de Gaussianidad

La extensión esférica controla el jet local \(r\downarrow0\), pero las leyes completas de saturación, las constantes \(r^{-1}/r^{-3}\), la monotonía global y el teorema empírico siguen siendo gaussianos. 

### La mitad de Löwner sigue teniendo una relación indirecta con redes ordinarias

El paper es transparente en que \(\sigma(A)\) por cálculo funcional espectral no es la activación entrywise de una red estándar. 

El puente identifica un invariante común, pero todavía no demuestra que observar el defecto matricial permita predecir o controlar una propiedad operativa de entrenamiento de una red convencional. Matemáticamente es elegante; como impacto en aprendizaje automático, continúa siendo indirecto.

### La técnica es sólida, pero no introduce una maquinaria radicalmente nueva

Las nuevas demostraciones combinan Taylor, simetría esférica, transformadas Gamma, Bernstein, redes métricas, colas gaussianas, interlacing y Schur complement. El propio manuscrito resume así sus ingredientes. 

El valor está en la síntesis, las constantes, el empaquetado y las conexiones exactas, no en haber inventado un nuevo método general de análisis.

## Qué haría subir la nota ahora

### 1. Determinar la complejidad óptima del Gram ponderado

Este sería el salto más importante.

Hay que resolver cuál de estas posibilidades es correcta:

$$
n_{\mathrm{crit}}\asymp
\frac{rd}{\varepsilon^2},
$$

o bien una dependencia menor, por ejemplo aditiva o con otra potencia. No conviene proponerse automáticamente probar \(\Omega(rd)\): primero hay que establecer cuál es la verdad.

El resultado ideal incluiría:

* Cota superior y cota inferior coincidentes.
* Dependencia correcta en \(\varepsilon\) y \(\delta\).
* Control del menor valor singular del diseño gaussiano heterocedástico.
* Error relativo del autovalor radial.
* Error del autoespacio.
* Casos \(p=1\), \(p=2\) y \(p>0\).

Esto podría llevar el paper aproximadamente a **4.5–4.8**.

### 2. Pasar del Gram oracle a un estimador con etiquetas

El siguiente nivel sería demostrar para el MLE, ERM o algún estimador explícito que, con alta probabilidad,

$$
\|\widehat w-w_\star\|
\le
\text{cota óptima en }n,d,r,
$$

y relacionar esa cota con la resolución empírica del modo radial.

Una versión especialmente fuerte controlaría simultáneamente:

* Error angular.
* Error de norma o “temperatura”.
* Hessiano empírico alrededor del estimador.
* Cuenca local de convergencia.
* Número de iteraciones de un algoritmo concreto.

Esto convertiría la geometría del paper en una consecuencia estadística y algorítmica directa, y podría elevarlo por encima de **5**.

### 3. Hacer el teorema uniforme en \(w\)

El Teorema 7.1 es para un teacher fijo. Un resultado del tipo

$$
\sup_{\substack{u\in S^{d-1}\\r\in[R,2R]}}
\left\|
H_h(r,u)^{-1/2}
\bigl(\widehat H_{h,n}(r,u)-H_h(r,u)\bigr)
H_h(r,u)^{-1/2}
\right\|
\le\varepsilon
$$

sería mucho más útil para analizar paisajes y trayectorias de optimización.

### 4. Extender la saturación global más allá de la gaussiana

Para inputs esféricos con densidad proyectada regular cerca de cero, probablemente puede formularse una teoría con constantes que dependan de:

* La densidad de \(u^\top X\) en cero.
* El segundo momento transversal condicionado a \(u^\top X=0\).
* Derivadas locales de esa densidad.
* Momentos o colas necesarios para los restos.

Obtener las leyes \(r^{-1}\), \(r^{-3}\) y la constante de la razón en esa generalidad demostraría que el fenómeno no es una propiedad especial de la integral gaussiana.

### 5. Mostrar realmente los \(C_p\)

El Corolario 7.2 afirma que existen constantes finitas computables \(C_p,C'_p\), pero no presenta una fórmula cerrada ni valores para \(p=1,2\); la prueba se limita a agrupar los términos bajo una constante dependiente de \(p\). 

Añadiría dos corolarios explícitos:

$$
n\ge C_1\frac{r[d+\log(12/\delta)]}{\varepsilon^2},
\qquad
n\ge C_2\frac{r[d+\log(12/\delta)]}{\varepsilon^2},
$$

con valores numéricos certificados, aunque sean conservadores. Eso cerraría la pequeña distancia entre “explícito” y “en principio computable”.

También añadiría una figura finito-muestral en función de \(n/(rd)\), mostrando:

* Error relativo radial.
* Error relativo tangencial.
* Ángulo del autovector.
* Probabilidad de slab vacío.

La única figura actual sigue siendo poblacional; la nueva contribución principal merece su propia visualización. 

## Evaluación por dimensiones

| Aspecto                       |   V1 |       V2 |
| ----------------------------- | ---: | -------: |
| Rigor provisional             |  8.2 |  **8.7** |
| Exposición y delimitación     |  8.6 |  **8.8** |
| Novedad                       |  5.8 |  **7.1** |
| Profundidad técnica           |  5.4 |  **7.0** |
| Alcance                       |  3.9 |  **5.8** |
| Impacto potencial             |  4.3 |  **5.7** |
| Escala “Problema del Milenio” | 2.70 | **3.90** |

## Veredicto

**3.90/10.00.**

Ahora lo veo como un **paper teórico especializado fuerte**, con una identidad conceptual elegante y un nuevo componente finito-muestral real. La versión anterior era principalmente una conexión exacta bien presentada; esta ya tiene una segunda columna técnica independiente y útil.

Lo que lo separa de la franja 4.5–5.5 no es un problema de redacción, sino la ausencia de una complejidad minimax-sharp, de un estimador basado en datos etiquetados, de uniformidad en el espacio de parámetros y de una extensión global más allá de Gaussianidad.

[1]: https://arxiv.org/abs/2602.07373v3 "[2602.07373v3] Zero-energy scattering and the real Bers image on the line"
