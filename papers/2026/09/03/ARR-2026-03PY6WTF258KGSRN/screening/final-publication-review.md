# Dictamen final de publicación — passive

**PASS — ARR-2026-03PY6WTF258KGSRN, v1.** No se ha detectado ninguna objeción bloqueante en el alcance inspeccionado.

**Two-state exact routing: algebraic feasibility and sharp delay-two rigidity**  
Autor: Lluis Eriksson. PDF: 9 páginas. Fecha de inspección: 2026-09-06T12:42:14.915188+00:00.

| Archivo o referencia | SHA-256 |
|---|---|
| Fuente final, paper.md | `9a4d1a206d5a994c7d32f7ab1bdbd7786fe9cff00e13a8f146f4676c3873b8ad` |
| PDF canónico, paper.pdf | `c40efa3df98b69cf2b1bd8ebddbc4bed11a54f5d9195db26d0c208006680e1a9` |
| Fuente aceptada, revisión 1 | `2e105f5027d0abdbd4cd0b97c971aea20a3b16d080eb5d0611a664637b78b886` |
| Diferencia de publicación | `ac1da4584ee5b71de0ea7e7e4c48d5fba07d8da8e7a905794547129fab2601c6` |

## Alcance y continuidad

Comprobé personalmente los hashes de los archivos finales, la copia de la fuente aceptada y la diferencia real entre ambas. Una sustitución exacta y limitada de las frases de publicación reproduce íntegramente la fuente final; los enunciados, pruebas, referencias y límites matemáticos se conservan. La fuente incluida en research coincide con paper.md.

Sustitución del estado de borrador por ARR v1 e identificador; última frase actualizada a la autorización de publicación del autor.

Comprobé la continuidad de todos los archivos Python de research con la revisión 1. El único cambio es el enlace al nuevo hash, un comentario y la etiqueta del informe en el verificador de redes; su árbol sintáctico completo coincide después de normalizar esos valores.

Este dictamen continúa REVIEW.json y DELTA_REVIEW.json (DELTA_ACCEPTED). No emite una nueva nota ni un ARR-ASSESS: las valoraciones anteriores siguen ligadas a las versiones originalmente puntuadas. Los informes previos permanecen sin cambios.

## Inspección visual y correspondencia

Rendericé y examiné individualmente las 9 páginas finales, incluidas sus imágenes matemáticas, a aproximadamente 953×1348 píxeles por página. Contrasté su contenido con la fuente. La extracción de texto fue un apoyo; no fue la base exclusiva de la aprobación. Verifiqué título, autor, ARRid y v1, los metadatos de título/autor y la identificación y numeración de cada pie de página.

| Página | Contenido inspeccionado |
|---|---|
| 1 | Título, autor y ARR v1; resumen con optimalidad aguda abierta; modelo de dos estados, coste angular y coeficientes A,B,C. |
| 2 | Condiciones Y>0, V>K² y matriz 2×2 semidefinida positiva; retardo, cuártica y rigidez; planitud y grado exactamente dos. |
| 3 | Factor espectral, raíces en el semiplano superior, positividad, reconstrucción y completación matricial; inicio del agotamiento de polos. |
| 4 | Agotamiento de polos con multiplicidades; desigualdad V≥d² y Y>0 en (15); coeficientes de la cuártica y matriz de Gram 3×3 en (17). |
| 5 | Alcance algebraico de factibilidad, construcción finita, compacidad y consecución; inicio de la rigidez por Fourier. |
| 6 | Equivalencia a=b≥π/2, construcción completa y factor complejo; cota cuantitativa y comienzo de su prueba. |
| 7 | Fin de la cota, límite geométrico y proposición D explícitamente como cota superior; cúbica, parámetros y T2(a,a)≤T*. |
| 8 | Prueba cúbica, certificado R=(T*−Y)(t²−x)², mejora estricta y ejemplo w=11/5; exclusión global aún abierta. |
| 9 | Límites del modelo y óptimos abiertos; antecedentes Appaiah–Pal y Bharath et al. con alcance de lectura; autorización y asistencia de IA. |

No encontré omisiones materiales, fórmulas alteradas, símbolos perdidos, recortes, solapamientos o discrepancias de identidad que bloqueen estos PDFs. El JSON adjunto conserva los hashes de cada página renderizada y el detalle de los controles.

## Límites preservados

El modelo conserva exactamente dos estados, tres nodos, rayos ortogonales, fases libres y pico de retardo angular. La proposición D prueba una construcción alcanzable y una cota superior en el caso agudo simétrico: NO demuestra el mínimo global. La optimalidad aguda sin restricciones y el mínimo asimétrico general siguen abiertos.

No repetí los verificadores matemáticos en este pase final ni realicé una búsqueda bibliográfica nueva. Los replays finales y los controles de publicación ARR corresponden al coordinador. Este PASS cubre exclusivamente las fuentes y PDFs identificados arriba.

## Identidad de la revisión

Screening interno por IA de la misma familia de modelos, con configuración local **gpt-6-astra, xhigh**. Evidencia: registro turn_context de esta tarea, timestamp `2026-09-06T12:32:36.450Z`, línea 306; SHA-256 del registro sin salto final: `7a1141ec6ccbd69ea7acb6b812084fa17ea30a5a844e5272f7a9bf85ad1efd0c`. La ruta exacta del registro y el identificador de turno figuran en el JSON. Es evidencia de configuración local, no una atestación independiente del servicio. No es revisión humana ni arbitraje externo.

Objeciones pendientes dentro de este alcance: ninguna. No modifiqué los candidatos ni publiqué o envié los artículos. Recalculé los hashes de fuente y PDF al cerrar este dictamen.

Continuidad documental:

- REVIEW.json: `9a1a97d494a9b767d1f7cdcef67fecf31787a8b900e55e94d50b1be8f501ac07`.
- DELTA_REVIEW.md: `ac16e6afe694e1a4c32b9dcd1a023867abd0f5bf662e298ad6f93f268ec4a7f3`.
- DELTA_REVIEW.json: `9f309df20cfcbe517d332bf8db3870c9fd525ba2eef18d1579f9ae2fb737d818`.
- valoracion_propia_previa.json: `3744bdc583f99cad7f175c1e34a3a20ec09292452804c69bf0563860f5af74b5`.
