# Correspondencia entre enunciados y verificadores

Esta aclaración documental se añade al expediente después de la evaluación formal. El PDF, la fuente, los programas, los certificados y la respuesta original del modelo permanecen intactos. No es una decisión editorial ni una reevaluación del modelo.

| Parte del manuscrito v3 | Comprobación pertinente | Alcance |
| --- | --- | --- |
| Teorema 1 y secciones 3–4: techo por inercia | `replay/commutator_inertia.py` | 1.024 testigos de bloques planos, 64 descomposiciones y 31 dimensiones de las constantes Gini recordadas. La prueba general está en el manuscrito. |
| Teoremas 2–3 y secciones 5.1–5.4: nuevas constantes óptimas | `replay/sharp_stability_verify.py` | Tres identidades simbólicas, 87.360 celdas de átomos, 2.016 máximos completos no equilibrados y 504 familias de interpolación/Gini. El coeficiente mejorado es `(n-1)/2`. |
| Teorema 4: constante equilibrada 17/36 | `replay/verify_balanced_three.py` | Enumeración racional por restricciones activas; 22 vértices, 522 ternas, 11.484 desigualdades y extremo agudo. |
| Control distinto del Teorema 4 | `replay/independent_balanced_review.py` | Enumeración geométrica por aristas y generación por tableaux LR; verifica las mismas 11.484 desigualdades. |
| Teorema 5 y sección 6: transporte | `replay/transport.py` | Certificados primal-dual, reconstrucciones y contrastes de costes. No determina el coste matricial general. |
| Ejemplo de coste 4/3 y separación del transporte | `replay/sharp_stability_verify.py`, `replay/independent_review_checks.py` | Certificado de 142 desigualdades y cota inferior coincidente; regeneración alternativa por LR. El segundo programa también comprueba las identidades polinómicas. |
| **Comprobación histórica** de la estabilidad anterior | `replay/stability.py` y `certificates/stability.json` | Conservan el coeficiente antiguo `n/2` y el término `n(1-a_1)`. Su PASS sólo certifica esas cotas anteriores, que siguen siendo verdaderas. No debe citarse ese PASS como comprobación del nuevo coeficiente `(n-1)/2`. |

Los siete programas pasaron en la entrega original y en la nueva evaluación formal. Esta última regeneró los siete certificados sin diferencias de bytes. Los programas históricos se conservan para mantener la trazabilidad, no como sustitutos de los verificadores nuevos.

## Localizadores de antecedentes

Estos localizadores se contrastaron en las copias completas de la versión v1 conservadas en el corpus de investigación. Complementan la bibliografía del PDF sin alterar el archivo revisado ni la evaluación original, que declara su propio límite de acceso a enlaces.

| Referencia del PDF | Localizador | Resultado atribuido |
| --- | --- | --- |
| [1] *Sharp Rank-Adaptive Bounds*, ARR-2026-1D2QV1RP1292JREW | Teorema 1.1 y Corolario 1.2; Proposición 6.2 | Cota por rango, extremos y certificado inferior de una espiga. |
| [2] *One-Spike Inverse Self-Commutators*, ARR-2026-7NPRNBW4488HG90K | Teorema 3.1; Teorema 4.1 | Coste exacto de una espiga, rigidez de óptimos e identidad Gini con constantes de estabilidad óptimas. |
| [9] *The Exact Four-Level Inverse Commutator Cost*, ARR-2026-3M1EEG1T689ADSMW | Teorema 2.2; Teorema 3.1 | Programa general de Horn y fórmula exacta de cuatro niveles. |
| [10] *The Exact Five-Level Inverse Commutator Cost*, ARR-2026-37B8R0QTA894GTFF | Teorema 2.2; Teorema 3.1 | Programa de Horn y fórmula exacta de cinco niveles, antecedente del benchmark. |

Los hashes de las copias consultadas aparecen en `REFERENCE_LOCATORS.json`. Esta identificación no es una comprobación exhaustiva de prioridad externa. El editor puede decidir si incorporar estos localizadores al PDF exigiría una revisión nueva; el presente expediente conserva el PDF aprobado para feedback por el autor.
