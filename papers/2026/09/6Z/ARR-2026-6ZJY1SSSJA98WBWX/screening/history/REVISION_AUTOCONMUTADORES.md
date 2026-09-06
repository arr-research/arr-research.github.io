# Revisión matemática: inercia balanceada (5,5)

**Dictamen: favorable como nota especializada, con una corrección editorial concreta. Nota propia: 3.60/10.00.** No he encontrado un error bloqueante en el coeficiente 113/152 ni en los cuatro puntos de igualdad. La contribución es una evaluación exacta adicional de un programa y una estrategia ya desarrollados para N=4; el volumen del cálculo no aumenta por sí mismo su alcance matemático.

Fuente: `commutator/paper.md`, SHA256 `a739718945c9d5ebb60e05766005d60e65ad34ac05cf423c55435e1496b05ae9`. PDF, seis páginas: `9e38457c9c30445e41dfe2318985ab04c85c1e2b279d34a979d651c3bea9faf2`. Leí íntegramente la prueba y el prompt crítico. La valoración está registrada antes de abrir la revisión anterior.

## Hallazgo confirmado C-01

En la línea 106 se indica comenzar con productos de dos «base vertices». Antes, el texto distingue el ápice u de los vértices de la base v_kl. Si se interpreta literalmente ese vocabulario, se omiten los productos con u y, en particular, (e,u) y (u,e); un corte estricto sobre una arista no recupera esos extremos. La frase debe decir que se usan los once vértices de **{u} ∪ {v_kl}**. La enumeración implementada sí los incluye. Es una ambigüedad editorial del algoritmo descrito, no una refutación del resultado ni un fallo de los certificados.

## Normalización, cobertura y Horn

R=CC*/2 y S=C*C/2 tienen espectro común no negativo y traza igual a la cantidad minimizada. Recíprocamente, C=√2 U diag(√s) V* realiza R−S=F. Las entradas de −S, ordenadas, son −s_d,…,−s_1, de modo que el signo y la inversión de índices en (5) son correctos. La igualdad de trazas requerida por Horn es automática: F tiene traza cero. Restar s_d no modifica las desigualdades porque I y J tienen igual tamaño.

El valor del programa es poliédrico y convexo en la cámara ordenada de traza cero. Su uso aquí es válido: las combinaciones de listas decrecientes mantienen el orden, incluso en la frontera con ceros. No se necesita convexidad como función de matrices Hermitianas arbitrarias, que sería falsa. Verifiqué la definición recursiva y suficiencia en [Fulton, sección 1 y teorema 1](https://arxiv.org/pdf/math/9908012).

La parametrización por pasos positivos y negativos de Q_r tiene un ápice y una base cuyas caras con p,q pasos activos tienen dimensión p+q−2. Da los once vértices y treinta aristas. Las aristas de un producto fijan un vértice en un factor; cortar con q(a)=q(b) añade exclusivamente sus intersecciones interiores. Contando los productos con el ápice se obtienen 267 pares ordenados, repartidos en 139 clases por signo. Los 32 dominios orientados cubren también sus caras degeneradas. D_* es afín en cada uno; la convexidad convierte las cotas de todos sus vértices en la cota completa.

Los espectros racionales cumplen el sistema Horn sin comprimir. Los duales combinan desigualdades válidas con pesos no negativos y dejan coeficientes a lo sumo uno sobre variables no negativas; su objetivo coincide con el primal. Eso certifica los costes de los vértices. La cota global necesita solamente factibilidad primal, mientras que los duales aportan exactitud adicional.

## Dimensión ambiental e igualdad

Para −F, la terna I=(1,3), J=(1,d−1), K=(2,d−1) es admisible: igualdad de sumas y tres pruebas recursivas 2≤3, d≤d, 4≤d. Su lado derecho es b₂−a₂; los ceros ambientales no alteran esas posiciones. Combinando con s₂≥b₂ y s_i≥a_i se obtiene (10), con toda la cola positiva. En (A,B), esto da 127/80 en cualquier d≥10. El testigo (9) tiene la misma traza, y puede ampliarse con ceros. No se presupone invariancia general del coste al ampliar la dimensión.

En B_eta, 0<eta<1/5 garantiza orden y positividad estricta. Las dos expresiones que entran en D_* son 19/10−6eta y 19/10+3eta, así que la fórmula elegida es válida en todo el intervalo, no únicamente cerca de cero. Las cotas (11) fijan el límite del coste en cada dimensión d previamente fijada. El cociente converge a (3−127/80)/(19/10)=113/152.

La clasificación de igualdad tampoco se deduce simplemente de cuatro vértices óptimos. La concavidad y no negatividad de g_d reducen cada cero a la envolvente de contactos del mismo dominio. La incidencia deja dos segmentos candidatos. En su punto medio, el testigo de coste 69/40 da holgura 91/160; concavidad propaga una holgura al menos (91/80)min(t,1−t) a todo interior. La ampliación por ceros preserva esta cota inferior de holgura. Los extremos (e,u),(u,e) tienen coste tres por la fórmula de un único valor positivo; los otros dos tienen el coste ya demostrado. La desigualdad es, por tanto, estricta en toda la inercia exacta (5,5).

Revisé además la fórmula de un único valor positivo y la prueba del coeficiente inverso 2 en el predecesor consolidado ARR-2026-24M24KDPZK8HDBQ9, secciones 2 y 5.1–5.4. Esa parte de (2) es heredada y no se cuenta como contribución del artículo actual.

## Ejecuciones y límite de independencia

Los dos verificadores entregados terminaron con PASS mediante el replay en copia. El principal regenera 191.353 ternas y valida **268×191.353 = 51.282.604** condiciones enteras, incluyendo el punto medio, además de geometría y 525 términos duales. Esta cantidad cuenta las pruebas indexadas de esa ejecución; no debe sumarse otra vez como si cada replay aportara nuevas condiciones matemáticas.

El segundo verificador normalmente carga `review/lr_10_independent.json` si su hash de generador coincide. Esa conducta limita lo que demuestra un replay ordinario: comparar y aplicar una tabla guardada no equivale a regenerarla. Creé otra copia sin la tabla, ejecuté el mismo revisor y observé la generación LR para tamaños 1,…,9. Produjo 55, 1287, 12140, 46208, 71973, 46208, 12140, 1287, 55 ternas, con igualdad exacta del conjunto y PASS de todos los certificados. La salvedad queda resuelta para esta auditoría. Los controles de magnitud enteros evitan desbordamiento en los datos efectivamente usados.

## Novedad y alcance

La fuente del predecesor N=4 afirma expresamente que N≥5 estaba abierto, pero ya demuestra la reducción O(N⁵), el método primal, el argumento de dos filas y la exclusión de segmentos por un punto medio. El nuevo 113/152, los contactos específicos y la retención de la cola positiva aportan conocimiento concreto; no constituyen un método nuevo de Horn. [Angel–Schechtman](https://arxiv.org/abs/1503.07980) trata un problema de norma de conmutadores generales con objetivo diferente y no acredita ni refuta esta prioridad particular.

La nota es sólida dentro de su tamaño. Recomiendo corregir C-01 y ofrecer una opción explícita de regeneración sin caché. No se exige resolver N≥6 para sostener estos teoremas. Tampoco se ha demostrado un algoritmo de tiempo total polinómico, ni calculado el coste general del interior, ni acreditado prioridad mundial o arbitraje humano.
