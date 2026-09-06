# Dictamen limitado: ciclo 4, revisión 1

**Delta aceptado. Las observaciones revisadas quedan atendidas; no introduzco ninguna objeción matemática nueva.** Se conservan las notas anteriores: cuántica 4.70, autoconmutadores 3.60 y redes 4.80. No se realizó una nueva evaluación del mérito.

Comprobé los seis archivos identificados en `revision_source_hashes.json`, comparando sus bytes con los originales de `cycle4`, y reconstruí `CHANGES.diff`: coincide exactamente con esos cambios. Revisé `CAMBIOS.md` y la documentación de reproducción. El alcance es la modificación de fuentes y controles de caché; quedan fuera los PDF, el ajuste del maquetador y una nueva búsqueda bibliográfica general.

| Observación | Decisión | Fundamento del cierre |
|---|---|---|
| Convención de vectorización cuántica | Atendida | La definición da Tr_canal(|B⟩⟩⟨⟨B|)=(B*B)^T y el twirl d I_d⊗(B*B)^T. Transponer la normalización recupera ΣB*B=dI_r. Se conserva correctamente el factor 1/d del POVM. |
| Ejemplo de triángulo | Atendida | Recalculé las nueve celdas con fracciones exactas. Las privadas son (0,2),(2,0),(2,2); los seis valores no nulos son 1/2,1/3,1/6,5/6,2/3,1/2. Coinciden con el texto y con `triangle_example_check.json`. |
| C-01: vértices iniciales | Cerrada | La nueva frase nombra los once vértices {u}∪{v_kl} e incluye expresamente los pares con el ápice. Desaparece la ambigüedad señalada. |
| R-01: procedencia LR | Cerrada en el delta | `--fresh-lr` evita la lectura de caché, fuerza la generación y registra `lr_source` y `lr_cache_reason`. El replay transmite la opción únicamente al revisor LR. |
| P-01: antecedentes all-pass | Cerrada dentro del alcance bibliográfico declarado | Se incorporan Appaiah–Pal con la limitación explícita a resumen/metadatos, y Bharath y colaboradores con la distinción entre suma de trazas en nodos y pico global sobre el círculo. La comparación coincide con las fuentes ya inspeccionadas en la auditoría original y no pretende acreditar prioridad. |
| Agotamiento de polos en redes | Atendida | La columna primitiva tiene multiplicidad total dos; restringir una realización matricial a esa entrada no aumenta ninguna multiplicidad local. La cota global dos fuerza igualdad en cada polo, incluidos los repetidos. El determinante inner tiene las mismas multiplicidades mediante Potapov; se identifica así con h*/h salvo fase constante. Se aclara la conversión de convención interior/exterior. |
| Vinculación del verificador de redes | Aceptada | El hash esperado coincide con la nueva fuente. Se conserva el anterior en un comentario. Tras normalizar la etiqueta del primer control, las funciones matemáticas son idénticas en su estructura sintáctica. No se atribuye al informe antiguo la lectura de la revisión 1. |

El triángulo tiene seis celdas positivas y suma de valores de dρ/3 igual a tres; por tanto trρ=1 y rango 2d/3. Las tres líneas son no paralelas y no concurrentes. La repetición del valor 1/2 no interfiere con las celdas privadas. Los mínimos tres de lista y de cuadrados se siguen de los teoremas ya auditados.

Para R-01 ejecuté únicamente el bloque real de selección de caché, extraído del código revisado, con un generador sustitutivo diminuto. Cinco escenarios dieron PASS: caché coincidente, hash antiguo, ausencia de caché y modo forzado con caché coincidente o JSON inválido. En los dos modos forzados no se leyó la caché. Ocho combinaciones verificaron el envío de la opción desde el replay. Estos ensayos prueban el control de flujo y la procedencia; **no constituyen otra regeneración matemática de las ternas LR**.

Además, las funciones auxiliares LR y toda la sección posterior que valida los certificados tienen estructura sintáctica idéntica a la original. Nueve archivos matemáticos no modificados —generadores, verificadores, geometría y datos centrales— conservan sus hashes. No se alteran las desigualdades o el contenido de las verificaciones para obtener un PASS.

Leí `replay_revision1.json`, producido por la coordinadora: registra seis PASS y, para LR, `lr_source=regenerated`, motivo `--fresh-lr requested` y 191.353 ternas. Sus seis hashes de programa corresponden a los archivos revisados. Lo incorporo como evidencia de una ejecución **de la coordinadora**; no he repetido el replay completo en este turno.

Los hashes SHA256 de los nuevos manuscritos son:

- Cuántica: `ea86bffcb4cf8af6dccf96fedbef4621821ba6f8b4d2eba008840867d8a2546f`.
- Autoconmutadores: `7b925d88c6b6700ced4666eabf6979b0aa1ba9c9ef5d88228bd60e315ae868b2`.
- Redes: `2e105f5027d0abdbd4cd0b97c971aea20a3b16d080eb5d0611a664637b78b886`.

`DELTA_REVIEW.json` conserva los hashes originales y revisados de los seis archivos, los documentos auxiliares leídos, los ensayos ejecutados y las decisiones. La adición final a `CAMBIOS.md` informa de una corrección del tratamiento de `\bigcap` y del espaciado. Esa modificación de maquetación queda a cargo de la coordinadora y **no está validada por este dictamen**, que tampoco se extiende a versiones posteriores con otros hashes.

No modifiqué la entrega original ni la revisión 1, no publiqué nada y no cambié las notas ni los informes de la auditoría original.
