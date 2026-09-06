# Revisión matemática: routing exacto con dos estados

**Dictamen: favorable con revisión bibliográfica localizada y aclaraciones menores. Nota propia: 4.80/10.00.** No he encontrado un error que invalide la factibilidad completa, el locus de retardo dos, la brecha o la construcción cúbica como cota superior. La optimalidad global de esa construcción continúa abierta; ni el texto ni esta auditoría la demuestran.

Fuente: `passive/paper.md`, SHA256 `a4d59c248eab267df4fcf746f0fc493fa77853a27aed1ab6259986290a0bc2d2`. PDF de nueve páginas: `3827c836411ac1510822938992e6e439747047ce94c40bd5f41a00fb94aa4d83`. Leí todas las pruebas y el prompt. La valoración propia se fijó antes de consultar la captura anterior.

## Reducción, cancelaciones y realizabilidad

El argumento de planitud es correcto: un numerador de grado como máximo dos que se anula en tres nodos distintos es cero. La pareja primitiva de numeradores no puede tener grado menor que dos, porque el componente e₂ tiene dos ceros distintos y es no nulo en el nodo excepcional. No hay pérdida de ese grado por una cancelación común. Tras el cambio de Cayley, q=t²−d² y p tiene grado como máximo uno; h tiene grado dos, no se anula en la frontera y tiene polos en el semiplano superior, opuesto al dominio de analiticidad.

La ausencia del término cúbico en |h|² obliga a que el coeficiente lineal de h sea imaginario puro. Para raíces r+i eta₁ y −r+i eta₂ se obtiene Y=eta₁+eta₂ y V−K²=eta₁ eta₂[1+4r²/Y²]. La condición Y>0,V>K² es también suficiente: la región es conexa y ninguna raíz puede cruzar el eje real dentro de ella; en K=0 ambas están arriba. Las raíces coincidentes no rompen el argumento.

La positividad de la matriz de coeficientes es equivalente a la no negatividad de la potencia residual, incluidos los casos A=0 y AC=B². El factor complejo lineal de (12) cubre todos esos casos. El caso p≡0 no es admisible: q tiene ceros reales, mientras |h|² es estrictamente positivo allí. Por la misma razón p(±d)≠0, y no hay cancelación compartida por los numeradores. Como comprobación exacta adicional ensayé d=1,V=2,Y=√2,K=0, donde A=B=0,C=3 y p=√3; la identidad de potencia sigue siendo válida.

La matriz (13) es inner por multiplicación directa, con determinante h*/h. La columna primitiva ya utiliza dos polos con multiplicidad; una matriz inner de grado dos que la contenga no puede añadir polos del determinante. Equivalentemente, en una factorización de Potapov las dos contribuciones ya están agotadas. Conviene explicitar esta última frase con una referencia concreta o un pequeño lema para el lector, pero no encuentro un hueco invalidante. La realización es la del modelo racional-inner; no acredita un circuito recíproco, tolerancias de fabricación o una calibración temporal física, que el artículo no afirma.

La derivada de h*/h y dt/dphi=−[1+(t+m)²]/2 reproducen exactamente (5), incluido su signo y sin perder el factor angular por trasladar t. La matriz de Wigner–Smith es positiva semidefinida por Potapov. Al incrustar la realización en más puertos con un bloque identidad se conserva su retardo; y todo router permitido ya tiene un retardo de esta forma. Así se justifica la independencia de N.

## Positividad global, mínimo y rigidez

El denominador en (5) es positivo para todo t real. Por ello el techo equivale a R_T≥0 en toda la recta; su coeficiente principal impone T≥Y y contempla el punto en infinito. Para T=Y, la no negatividad obliga también a anular un eventual término cúbico: no basta comprobar el coeficiente principal aislado. La equivalencia con una matriz Gram 3×3 cubre los grados menores y el polinomio cero. Las restricciones conjuntas son polinómicas, no un SDP convexo en todos los parámetros.

La identidad (14) excluye V<d². En V=d² quedan Y>0 y K²<d²; para V>d² la forma (15) retiene explícitamente Y>0 y un denominador estrictamente positivo. No aparecen puntos de potencia residual negativa como diseños válidos. La eliminación de cuantificadores da computabilidad algebraica en principio, no complejidad eficiente.

La construcción de polo doble prueba factibilidad finita. Un techo uniforme confina cada cero de Blaschke a un subdisco compacto. Para N fijo, direcciones y unitario constante también son compactos; los valores en los nodos pasan al límite. La tabla impide un límite de grado menor que dos. La independencia de N no exige compactar simultáneamente una unión de dimensiones distintas: basta el caso N=2 y el teorema A.

Si el pico alcanza la media dos, el retardo es constante. Los dos primeros coeficientes de Fourier fuerzan alpha₁+alpha₂=alpha₁²+alpha₂²=0, luego ambos ceros son cero. El máximo del numerador prescrito se alcanza en z=1 exactamente cuando a=b≥pi/2. La construcción (22), con su parte imaginaria no omitida, realiza todo ese intervalo. En el resto del dominio la existencia del mínimo convierte la imposibilidad de igualdad en una brecha estricta.

En el teorema C, los coeficientes de Fourier de una función no negativa con media epsilon tienen módulo como máximo epsilon; el control del producto de ceros y del denominador da r=(epsilon²+3epsilon)/2≥eta. Resolver la cuadrática reproduce (24). La cota geométrica usa velocidad de Fubini–Study como desviación típica del generador, acotada por la mitad del rango espectral y por la mitad de la traza. La longitud entre rayos ortogonales es pi/2; se obtienen pi/a y pi/b sin error de factor dos. La estricta imposibilidad de igualdad cuando esas cotas exceden dos sigue de analiticidad y media del retardo.

## Rama cúbica y verificaciones

Descartes tras x=w+z da exactamente una raíz x>w. La parametrización por r y su derivada sitúan r entre 2+√5 y 3+2√2 para w>1. Las identidades (31) y (32) prueban el techo en toda frecuencia, sus dos puntos de máximo y la mejora estricta; no son interpolaciones de una malla. La fixture w=11/5 tiene Y=4√11/5, pico 9/√11 y residual (t²−11)²/(5√11).

Ambos verificadores entregados terminaron con PASS: 95 y 144 comprobaciones simbólicas o exactas. El segundo deriva retardos desde ceros de Blaschke, reconstruye matrices en nodos y deriva la cúbica desde el problema reducido. Mis controles nuevos rederivan simbólicamente el retardo a partir del determinante, comprueban el caso A=0 y ensayan 2.000 triples para la equivalencia de estabilidad, sin contraejemplo.

Intenté mejorar numéricamente la rama cúbica permitiendo V>d² y K distinto de cero, con dos semillas en w=1.01,2.2,4,12. Los picos de cada candidato se calcularon en puntos estacionarios polinómicos e infinito, no por malla de frecuencias. No apareció mejora superior a 10⁻⁷ sobre 2.0070576419, 2.7136021012, 3.5174149936 y 5.8796084616. La búsqueda tiene cotas finitas de parámetros y usa aritmética flotante; no excluye mejoras fuera de ellas ni demuestra optimalidad.

## Novedad y hallazgo bibliográfico P-01

Contrasté los pasajes pertinentes de los dos predecesores: *Projective Memory* ya demuestra existencia con dos estados, planitud y compacidad; *A complete one-state error–delay law* estudia grado como máximo uno y excluye el problema actual. La novedad interna reside en la parametrización completa del retardo, el locus preciso, la brecha y la cota aguda certificada.

[Alpay–Jorgensen–Lewkowicz](https://arxiv.org/html/1410.0283v2) proporciona realización y completado clásicos, con una convención de exterior del disco que debe transformarse al interior usado aquí. [Bolotnikov](https://arxiv.org/pdf/1609.09843) trata valores escalares prescritos en la frontera con restricciones de grado, un antecedente pertinente pero con datos diferentes.

Falta una comparación más directa con **Bharath, Gaharwar, Appaiah y Pal**, [arXiv:2210.14015, publicado en Signal Processing 204 (2023), 108839](https://arxiv.org/abs/2210.14015). Su sección 4 formula interpolación de matrices unitarias y optimiza la suma de trazas de retardos en nodos mediante la matriz de Pick. Leí introducción, formulación y ese objetivo: no es el pico sobre toda la circunferencia con exactamente dos estados y condiciones de rayos libres. No he demostrado duplicación del resultado actual, pero el antecedente debe discutirse. También es pertinente **Appaiah–Pal (2020)**, *All-Pass Filter Design Using Blaschke Interpolation*, [registro institucional](https://dspace.library.iitb.ac.in/jspui/handle/100/34432): solo pude verificar su resumen y metadatos; el repositorio no ofrece el texto completo.

P-01 es una omisión bibliográfica localizada, no un error matemático ni una certificación de prioridad ajena. Recomiendo corregirla y hacer más explícita la justificación de que la columna agota los dos estados. El artículo ofrece una contribución especializada apreciable, aunque no la ley minimax completa de dos estados, ni el óptimo asimétrico general, ni una nueva teoría de positividad polinómica.
