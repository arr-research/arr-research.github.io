# Prompts de depósito ARR para agentes

Estos prompts autorizan preparar, validar e integrar un registro en ARR. Sustituye los campos entre corchetes y adjunta las rutas reales. No autorices al agente a inventar resultados, evaluaciones, licencias, relaciones ni marcas temporales.

## Research paper

```text
Publica este trabajo en ARR — Archive for Rigorous Research como un RESEARCH PAPER independiente.

Material entregado:
- PDF o fuente canónica: [RUTA]
- Fuentes y reproducción: [RUTA O "no suministradas"]
- Metadatos de envío: [RUTA O DATOS]
- Autoría: [AUTORES]
- Registros ARR relacionados: [IDS Y RELACIÓN, O "ninguno"]

Requisitos obligatorios:
1. Inspecciona el PDF y las fuentes; calcula tú mismo tamaño, número de páginas y SHA-256. No confíes sólo en valores declarados.
2. Crea el candidato exclusivamente con `python scripts/new_record.py --author "[DEPOSITANTE]" --type research-paper`. No inventes el ID.
3. Usa `schema_version: 1.1` y `record_type: research_paper`. No añadas el objeto `technical_note`.
4. Conserva la fuente canónica y proporciona `paper.md`; si el origen es PDF, conserva `paper.pdf`, añade `paper.txt` y registra hash y tamaño canónicos. Incluye LaTeX, bibliografía, Lean, Python, datos y replay en formatos puros cuando existan.
5. Completa autoría, autorización de depósito, procedencia, licencias por alcance, uso de IA, conflictos editoriales, limitaciones y relaciones ARR. No atribuyas una licencia a material de terceros sin base.
6. Ejecuta sólo las comprobaciones realmente disponibles. `not_assessed` debe permanecer visible. No declares screening de IA, reproducción, revisión bibliográfica, Lean ni peer review si no se realizaron bajo el protocolo aplicable y sobre esta versión exacta.
7. Valida el registro, ejecuta las pruebas, construye el sitio y revisa visualmente la página generada. Corrige cualquier fallo antes de publicar.
8. Integra mediante rama y pull request, espera CI, fusiona, crea la release inmutable y espera GitHub Pages. No anuncies publicación antes de que la ficha pública y la release respondan correctamente.
9. Registra después las horas exactas de depósito y publicación con zona horaria explícita y sus bases verificables; no uses una hora aproximada ni futura.
10. Verifica finalmente la URL pública, la release, los activos, los enlaces relacionados y el SHA-256 descargando de nuevo el PDF.

Entrega final: ID ARR, ficha pública, release, tipo de registro, fechas y horas exactas, hashes recalculados, archivos preservados, resultados de CI y comprobaciones, y cualquier aspecto no evaluado. Distingue publicación técnica de validación científica.
```

## Technical note

```text
Publica este trabajo en ARR — Archive for Rigorous Research como una TECHNICAL NOTE independiente, no como research paper.

Material entregado:
- PDF, Markdown, LaTeX u otra fuente canónica: [RUTA]
- Código, Lean, datos o reproducción: [RUTA O "no suministrados"]
- Metadatos o descripción: [RUTA O DATOS]
- Autoría: [AUTORES]
- Registros ARR relacionados: [IDS Y RELACIÓN, O "ninguno"]

Requisitos obligatorios:
1. Determina y documenta una sola clase de nota: `result`, `proof`, `formalization`, `computational`, `replication`, `negative_result`, `method`, `data`, `software` o `protocol`. Si el material no permite escogerla sin una decisión científica del autor, detente y pregunta.
2. Define `maturity` como `preliminary` o `complete_in_scope`. Redacta un `scope_statement` preciso y unas `limitations` explícitas. Una nota puede ser estrecha o breve, pero no vaga ni exenta de evidencia.
3. Inspecciona el objeto entregado y calcula tú mismo tamaño, páginas cuando haya PDF y SHA-256. No confíes únicamente en valores declarados.
4. Crea el candidato exclusivamente con `python scripts/new_record.py --author "[DEPOSITANTE]" --type technical-note`. No inventes el ID.
5. Usa `schema_version: 1.1`, `record_type: technical_note` y completa el objeto `technical_note`. La página debe quedar bajo `/notes/` y mostrar visiblemente la etiqueta TECHNICAL NOTE.
6. Conserva la fuente canónica y una versión `paper.md` legible por máquinas; para origen PDF conserva también `paper.pdf` y `paper.txt`. Incluye código, Lean, datos, tests y resultados en formatos puros cuando existan.
7. Completa autoría, autorización, procedencia, licencias por alcance, uso de IA, conflictos y relaciones ARR. Si amplía un registro anterior, usa `extends`; el registro anterior no se sobrescribe.
8. Ejecuta únicamente comprobaciones reales. `not_assessed` es válido. No presentes una nota como paper, no inventes evaluación de modelos, reproducción, certificación Lean, peer review, novedad ni corrección científica.
9. Valida el registro, ejecuta pruebas, construye el sitio y revisa la ficha generada. Integra mediante rama y pull request, espera CI, fusiona, crea la release inmutable y espera GitHub Pages.
10. Registra las horas exactas de depósito y publicación con zona horaria y base verificable. Comprueba la ficha pública, release, activos, enlaces y hash descargando nuevamente el archivo canónico.

Entrega final: ID ARR, ficha `/notes/`, release, clase y madurez de la nota, alcance, limitaciones, fechas y horas exactas, hashes recalculados, archivos preservados, resultados de CI y comprobaciones, y todo lo que permanezca `not_assessed`. Distingue publicación técnica de certificación científica.
```
