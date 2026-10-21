# ACTUALIZACION FINAL (Haiku repetidos importados)
Los 2 Haiku rechazados por esquema (basis > 600 car.) se repitieron (no recortados) y se importaron: 8 de 8 informes en el registro.
Primeros intentos conservados como `*.INTENTO1-esquema-rechazado.json` (+ `.evidence.json` con estado
'not_imported_schema_rejected' y motivo); la evidencia anterior de los fallidos fue sustituida. Notices de procedencia y
adjudicacion de lf y s3 reescritos (Schur c3: la objecion abierta NO se adjudica como error). Validacion: validate_papers OK,
pytest 380 passed (102 subtests), build_site OK.

| paper | n | media final | estrellas | rango |
|---|---|---|---|---|
| ARR-2026-5286KSE6RS984S9P | 2 | 2.75 | 3 Acceptable | 2.0-3.5 |
| ARR-2026-5YJX444B6M95ZTG4 | 2 | 3.45 | 3 Acceptable | 2.5-4.4 |
| ARR-2026-7W8BK4FK779W5ADJ | 2 | 3.30 | 3 Acceptable | 3.2-3.4 |
| ARR-2026-6TQRG7PY6C8JZR2D | 2 | 3.20 | 3 Acceptable | 3.0-3.4 |

(Las secciones siguientes son historicas; donde dicen 6 de 8 importados, queda superado por esta.)

# IMPORT_REPORT_FREE - importacion de informes Claude (sala limpia imperfecta), 21-10-2026

## RESULTADO (actualizado tras las decisiones del director)
- Importados 6 de 8 informes. NO importados por el validador (criteria.*.basis > 600 caracteres, limite del esquema):
  - lf Haiku 5.5 (correctness 662, novelty 740)
  - s3 Haiku 5.5 (correctness 624, novelty 611, reproducibility 657)
  No los he recortado (seria editar texto del modelo). Quedan en
  `registry/assessment-evidence/2026-10-21-claude-subagents/` (original + editado + evidence con
  publication_status 'not_imported_schema_rejected'). Opciones: re-ejecutar Haiku pidiendo basis <= 600 car.
  (politica: rerun solo por esquema), o recorte del operador declarado en operator_edits. Decision pendiente.
- Decisiones aplicadas: independence='unknown' en las 6; review_context y runtime_provenance OMITIDOS; ids PENDING_*
  rellenados; assessed_at = mtime real del fichero informe; recomendaciones y notas intactas; sin coste ni tokens.
  JSON original sin editar (`*.original.json`), editado (`*.assessment.json`), `*.evidence.json` con `operator_edits`
  (campos, de/a, sha256 original y editado). Sin cambios en scripts ni ratinglib.
- 8 operator_notices (2 por paper: procedencia/conteo con la frase sobre discordancia docs/codigo, y adjudicacion).
  Su source_files es el metadata.json del paper (como en el precedente; la adjudicacion completa esta en el mensaje).
- Validacion: record_model_assessment.py sin --publish y luego con --publish (6 ok); `python scripts/validate_papers.py`
  -> passed (223 papers); `python -m pytest -q tests` -> 380 passed, 102 subtests passed; `python scripts/build_site.py`
  -> OK (210 papers, 224 versiones, _site ignorado por git).

## Media / estrellas que muestra el sitio (aggregate_assessments, pesos 1, 'Limited')
| paper | n | media | estrellas | rango |
|---|---|---|---|---|
| ARR-2026-5286KSE6RS984S9P (Schur c4) | 2 | 2.75 | 3 Acceptable | 2.0-3.5 |
| ARR-2026-5YJX444B6M95ZTG4 (Davies c3) | 2 | 3.45 | 3 Acceptable | 2.5-4.4 |
| ARR-2026-7W8BK4FK779W5ADJ (Lyapunov) | 1 | 3.20 | 3 Acceptable | 3.2 |
| ARR-2026-6TQRG7PY6C8JZR2D (Schur c3) | 1 | 3.40 | 3 Acceptable | 3.4 |
Si se importaran tambien los 2 Haiku pendientes: lf (3.2+3.5)/2=3.35 -> 3; s3 (3.4+3.0)/2=3.20 -> 3.
Evidencia 'Limited' en los 4 (un proveedor, contexto no documentado, sin benchmark, recomendaciones no-accept).

## git diff --stat
see commit (registry/model-assessments.json + registry/assessment-evidence/2026-10-21-claude-subagents/ + este informe).

---
# Informe previo (parada, conservado)
# IMPORT_REPORT_FREE - importacion PARADA antes de tocar el registro (21-10-2026)

Estado: worktree `C:\Trabajo\airr-publicacion\rating-free-20261021` creado (rama `rating-free-20261021`,
sobre `rating-lyap3-20261021` = 1cbfe71). NO se ha modificado `registry/model-assessments.json`, ni
evidencia, ni se ha hecho commit/push. `git diff --stat` vacio. Parada por la clausula de discordancia
pedida por el operador; faltan decisiones del dueño.

## 1. Discordancia principal: independence y mediana

- `docs/OPENROUTER_ASSESSMENTS.md`: "Reports marked not_involved enter the median; involved or unknown
  remain visible but do not affect ranking".
- CODIGO real (`scripts/ratinglib.py::aggregate_ratings`): entran TODOS los informes (el ultimo por
  provider+model_id), cualquiera sea `independence`. El campo solo se copia como etiqueta `involvement`;
  no filtra ni pesa. No es mediana sino media ponderada por benchmark FrontierMath (peso 1 si no hay
  coincidencia exacta modelo+effort; sin `reasoning_effort` evidenciado seria peso 1).
- `docs/MODEL_ASSESSMENT_POLICY.md` ("Prior participation..."): la participacion previa "no tiene penalizacion
  numerica ... supersede la exclusion anterior"; informes con contexto incompleto "siguen siendo usables como
  evidencia limitada". build_site.py solo muestra `independence` y `review_context.mode`; tests
  (test_rating.py:28, test_assessments.py:102) confirman que un informe `involved` cuenta.
- Conclusion: OPENROUTER_ASSESSMENTS.md esta desactualizado respecto a codigo y politica. Con cualquier valor de
  `independence` los 8 informes ENTRARIAN en la puntuacion publica. Tu instruccion era parar si hay discordancia;
  la decision (¿entran o no? ¿corregir el doc?) es del dueño. Cambiar a `unknown` no los sacaria de la media.

## 2. El esquema NO admite la procedencia honesta pedida

- `runtime_provenance.basis` y `review_context.basis` solo admiten `platform_runtime_metadata`,
  `author_verified_ui`, `operator_verified_ui` (`RUNTIME_PROVENANCE_BASES`). 'operator_declaration' seria rechazado.
  Usar `operator_verified_ui` afirmaria una verificacion de UI que no existe: no lo he hecho.
- `reasoning_effort` debe ser uno de none/minimal/low/medium/high/xhigh/max/ultra; null/'unknown' rechazado.
- Ambos exigen `evidence_sha256` (hash de evidencia retenida; se podria usar el del dossier de la sala limpia).
- Pagina publica: con `review_context` mode 'shared' sale "review context: shared"; sin el, "unknown". Omitir
  `runtime_provenance`/`review_context` (permitido, ver politica) es la via honesta sin tocar el esquema: la cabecera
  usaria provider/model_id del informe y la nota de "sala limpia imperfecta" iria en un operator_notice y en evidence.json.
  Alternativa: ampliar el esquema (`operator_declaration`, effort 'unknown'), cambio de politica del dueño.
- operator_notices exige message de 40..1800 caracteres, source_files bajo `papers/<...>/<ARR-ID>/` con sha
  (hay que colocar la adjudicacion dentro de papers/..., p.ej. review/), un notice por paper y PDF.

## 3. Datos verificados (todos los sha coinciden con metadata.json, v1, working_paper)

| carpeta | ARR-ID | version_id | sha PDF |
|---|---|---|---|
| s4 | ARR-2026-5286KSE6RS984S9P | arr:version:ad53b9f2-00c6-4b3c-9198-809c023d24b4 | e0581972...a439d ok |
| d3 | ARR-2026-5YJX444B6M95ZTG4 | arr:version:43861a4b-558a-413c-8864-386538badd98 | a6382c9e...1e3e ok |
| lf | ARR-2026-7W8BK4FK779W5ADJ | arr:version:43d33522-87d1-4a10-a9cb-85574dcb648c | bec07a6e...66bc ok |
| s3 | ARR-2026-6TQRG7PY6C8JZR2D | arr:version:4bbcde1c-c05b-4a7d-832c-c9666d31cb2f | 28ed664c...097e ok |

Ninguno de los 4 papers tiene informes previos en el registro (177 informes, 29 notices actuales).

Informes (score / estrellas / recomendacion / assessed_at original):
- s4: Sonnet 3.5/4/minor 06:32:02+02; Haiku 2.0/2/major 06:33:26+02
- d3: Sonnet 4.4/4/major 12:00+02 (nominal); Haiku 2.5/3/major 00:00+00 (nominal)
- s3: Sonnet 3.4/3/minor 12:00+02 (nominal); Haiku 3.0/3/major 00:00+00 (nominal)
- lf: Sonnet 3.2/3/minor 12:00+00 (nominal); Haiku 3.5/4/major 00:00+00 (nominal)
Los 8 llevan independence 'not_involved_in_manuscript' y paper_id/version_id PENDING_*; todos tendrian que
reescribirse (ids, y assessed_at nominal por mtime) => hace falta operator_edits + original intacto.

## 4. Puntuacion publica prevista (pesos 1, sin coincidencia de benchmark; media aritmetica)

Calculo aproximado si se importaran los 2 informes por paper (media simple; el sitio redondea a estrella entera):
- s4: (3.5+2.0)/2 = 2.75 -> 3 estrellas
- d3: (4.4+2.5)/2 = 3.45 -> 3 estrellas
- s3: (3.4+3.0)/2 = 3.20 -> 3 estrellas
- lf: (3.2+3.5)/2 = 3.35 -> 3 estrellas
Evidence backing 'Limited' en todos (un solo proveedor, contexto no aislado, benchmark sin coincidencia, adversos
bloqueantes por recomendaciones major_revision). No verificadas con build real (no se construyo el sitio).
Atencion: dos modelos de la misma familia cuentan como 2 voces (model_id distinto), no como independientes.

## 5. Que necesito del dueño para continuar

1. ¿Entran en la puntuacion publica (es lo que haria el codigo) o se quiere un mecanismo para solo mostrarlos?
   (exigiria cambio de codigo/politica; corregir de paso docs/OPENROUTER_ASSESSMENTS.md).
2. Procedencia: ¿omitir review_context/runtime_provenance (recomendado, honesto) o ampliar el esquema con
   basis 'operator_declaration' y reasoning_effort 'unknown'?
3. ¿independence 'unknown' (honesto, sin efecto numerico) como indicaste condicionalmente?
Con eso, el resto (evidence.json con operator_edits y sha256 original/editado, notices de adjudicacion, validacion,
pytest, build) es mecanico. Pendiente: validate_papers.py, pytest y build_site no ejecutados.
