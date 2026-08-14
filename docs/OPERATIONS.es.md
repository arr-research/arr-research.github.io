# Operación cotidiana de ARR

## Dónde se guarda cada cosa

- Git: texto, LaTeX, Markdown, Lean, Python, metadatos y pruebas pequeñas.
- GitHub Releases: PDF, ZIP completo, datos grandes y otros archivos pesados.
- GitHub Pages: páginas web ligeras y catálogo.
- Repositorio privado de entrada: borradores todavía no aceptados.

## Publicar un trabajo aceptado

1. Asignar un identificador ARR.
2. Completar la plantilla del paper.
3. Abrir una propuesta de incorporación.
4. Resolver los errores y objeciones.
5. Aprobar e integrar la versión exacta.
6. Ejecutar la acción **Create ARR record release**.
7. Confirmar que la página enlaza la release y que los hashes coinciden.

## Regla esencial

La web nunca debe alojar directamente el corpus pesado. Si ARR cambia de dominio, el material continúa disponible en las releases de GitHub y sólo se actualizan los enlaces del catálogo.

## Capacidad

La recepción futura, el registro público y los artefactos se operan como planos separados. Antes de llegar a 1 GB de repositorio o de que el volumen de PR afecte al trabajo editorial, se activa una revisión de migración. Los identificadores `record_id` y `version_id` no contienen dominio ni proveedor, por lo que la migración a PostgreSQL y almacenamiento de objetos no altera las citas.

No se abrirá recepción pública hasta disponer de cuarentena, límites, retención, contacto de privacidad/retirada y ejecución aislada de código. Las propuestas rechazadas no se conservan indefinidamente.
