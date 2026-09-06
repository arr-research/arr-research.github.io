# Auditoría acotada de los tres manuscritos del ciclo 4

**No he encontrado errores matemáticos bloqueantes en los enunciados revisados.** Las pruebas y los seis verificadores respaldan los resultados dentro de sus hipótesis. La valoración se formó antes de abrir las puntuaciones anteriores.

| Artículo | Nota /10 | Decisión propia |
|---|---:|---|
| Cuántica: clasificación ternaria | **4.70** | Favorable con aclaraciones menores |
| Autoconmutadores: inercia (5,5) | **3.60** | Favorable como nota especializada; precisar la enumeración |
| Redes: routing de dos estados | **4.80** | Favorable con comparación bibliográfica adicional |

Se usa la escala solicitada: 10 equivale a resolver incondicionalmente un problema del milenio. Las notas valoran mérito, novedad y alcance; no son porcentajes de corrección. La clasificación cuántica y la factibilidad de redes ofrecen resultados estructurales más amplios que la evaluación del siguiente caso de inercia. Los tres trabajos siguen resolviendo problemas especializados acotados.

## Qué quedó comprobado

- Cuántica: ambas direcciones de la reducción POVM, el factor 1/d, multiplicidades centrales para d=3^k, rigidez del cuadrado, 150 familias, unicidad, espectros, longitudes, doce excepciones de dos etiquetas, rangos exactos y fallo de la conclusión en el umbral.
- Autoconmutadores: normalización, hipótesis de Horn, cobertura de 267 pares y 32 dominios orientados, 525 términos duales, cota ambiental, cociente 113/152, perturbación de inercia exacta y clasificación de los cuatro contactos.
- Redes: planitud, grado y cancelaciones, estabilidad, potencia residual, completado inner, positividad global incluido infinito, compacidad, locus de retardo dos, brecha cuantitativa, cota geométrica y certificado cúbico como cota superior.

Los seis programas se ejecutaron con `C:/Python312/python.exe` mediante el replay que trabaja en una copia temporal: **6/6 PASS**. Entorno observado: Python 3.12.6, NumPy 2.5.1, SciPy 1.18.0 y SymPy 1.14.0. Los originales se comprobaron mediante hashes y permanecen intactos.

El replay normal de LR reutiliza una tabla guardada. Lo complementé con una segunda copia sin esa tabla: reconstruyó las 191.353 ternas y obtuvo PASS. El primer verificador comprobó 51.282.604 condiciones Horn indexadas; las ejecuciones adicionales revisan esencialmente el mismo sistema y no multiplican su contenido matemático.

Mis controles nuevos incluyen cardinalidades centrales exactas en 2.665 pares, POVM de varios factores con ancilla compleja, identidades simbólicas del retardo, una degeneración de potencia residual y búsquedas numéricas acotadas de contraejemplos. No encontraron refutaciones. La búsqueda en redes no mejoró la rama cúbica en cuatro valores agudos, pero no demuestra su optimalidad.

## Problemas y mejoras concretas

**C-01, editorial:** `commutator/paper.md:106` usa «base vertices» de forma ambigua. Debe nombrar expresamente los once vértices {u}∪{v_kl}. El código sí incluye u; el teorema y sus certificados no fallan por ello.

**P-01, bibliográfico:** falta comparar redes con la interpolación all-pass con control de retardo de Appaiah–Pal (2020) y Bharath y colaboradores (2022/2023). El segundo optimiza trazas en nodos prescritos, una especificación distinta del pico global con dos estados del manuscrito. La omisión merece revisión, pero no se ha probado una duplicación. Véase el [texto primario de Bharath y colaboradores](https://arxiv.org/abs/2210.14015).

**R-01, reproducción:** distinguir carga de caché LR y regeneración independiente. Esta auditoría efectuó ambas; la salvedad está resuelta para sus resultados.

También conviene declarar la convención de vectorización cuántica y hacer más explícito por qué la columna de redes agota los dos estados. Son aclaraciones de exposición. No se ha encontrado un contraejemplo que obligue a cambiar los enunciados.

## Novedad y revisión anterior

La novedad interna está respaldada frente a los predecesores concretos inspeccionados. Las multiplicidades Weyl, Horn, el método de reducción N=4, la existencia de dos estados, la compacidad y la factorización espectral permanecen atribuidos como antecedentes. La prioridad bibliográfica mundial y el arbitraje humano no quedan acreditados.

La captura anterior daba 6.20 a cuántica y 5.80 a autoconmutadores. Mi desacuerdo numérico es de calibración del mérito; las observaciones matemáticas principales coinciden. El acceso a certificados resuelve especialmente la reserva anterior sobre Horn y aumenta la confianza sin aumentar el valor intrínseco del resultado. La captura no incluye una evaluación terminada de redes.

## Entrega

Los informes detallados son `REVISION_CUANTICA.md`, `REVISION_AUTOCONMUTADORES.md` y `REVISION_REDES.md`. `COMPARACION_REVISION_ANTERIOR.md` explica el contraste posterior. `REVIEW.json` identifica las versiones, comprobaciones, hallazgos y archivos de evidencia. `source_hashes.json` registra los hashes de los 48 archivos pertinentes del paquete congelado. No se rehízo el inventario del corpus ni se ejecutaron desarrollos Lean, no se subdelegó y no se publicó nada.
