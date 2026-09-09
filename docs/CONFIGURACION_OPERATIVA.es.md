# AIRR.SCIENCE — ficha de configuración y continuidad

**Estado documentado:** 9 de septiembre de 2026  
**Fase:** archivo personal/piloto con recepción privada abierta  
**Criterio de capacidad:** mantener la configuración actual mientras el volumen sea principalmente el de los trabajos del fundador.

Este documento explica dónde funciona AIRR, qué debe vigilarse y cómo crecer sin perder papers ni romper citas. No contiene contraseñas, claves API, secretos TOTP, códigos de recuperación ni la clave privada de descifrado. Esos valores nunca deben guardarse en Git.

## Arquitectura activa

| Componente | Proveedor | Función | ¿Es otro servidor de AIRR? |
|---|---|---|---|
| Dominio y DNS | Porkbun | Registro y DNS de `airr.science` | No |
| Web y catálogo público | GitHub Pages | Páginas de papers, búsqueda, metadatos y archivos de cita | No; es la proyección pública |
| Repositorio y publicaciones | GitHub | Código, registros aceptados, historial, Actions y Releases inmutables | No; es el registro público y su historial |
| Aplicación privada | Netcup VPS | Cuentas privadas, recepción de PDFs, cuarentena, revisión editorial y estadísticas | **Sí; es el único servidor operativo de AIRR** |
| Correo transaccional | Brevo | Avisos técnicos y de nuevas sumisiones desde `submissions@airr.science` | No |
| Copia externa | Backblaze B2 EU Central | Copias cifradas fuera del VPS | No; no sirve la web ni recibe sumisiones |

OVH no pertenece a AIRR y no forma parte de esta arquitectura.

## Estado comprobado

- Versión instalada en Netcup: commit `243735ff8a83761f557f3d2b733b7fb2d0fc9500`.
- Recepción pública de sumisiones: abierta.
- Datos preservados durante la actualización: 6 sumisiones, 1 cuenta privada y 8 códigos de recuperación.
- Comprobación del 9 de septiembre de 2026: aplicación, Caddy/HTTPS, ClamAV, correo, mantenimiento, copias locales, copia externa y actualizaciones de seguridad en estado correcto.
- La página pública ya explica que los trabajos del fundador requieren dos modelos identificados distintos.
- Límite de una cuenta: 10 sumisiones en una ventana móvil de 24 horas.
- Tamaño máximo por PDF: 25 MiB.

## Flujo para publicar trabajos del fundador

1. Subir el PDF desde el espacio privado de AIRR.
2. Confirmar el registro privado y el hash SHA-256 de la versión exacta.
3. Declarar en el expediente que Lluis Eriksson es autor y fundador/editor bajo `AIRR-FOUNDER-1.0`.
4. Registrar dos revisiones reales de dos modelos identificados distintos sobre ese mismo PDF. Si algún modelo participó antes en el trabajo, declararlo.
5. Resolver objeciones materiales o solicitar una versión corregida.
6. Firmar la decisión editorial. La publicación mostrará `author-editor acceptance`; no afirmará revisión humana independiente.
7. Autorizar separadamente la publicación, autoría mostrada y licencia de la versión exacta.
8. Crear e integrar el registro público y ejecutar **Create AIRR record release**.
9. Comprobar la página estable, PDF, hash, manifest, BibTeX, RIS y CSL JSON.

Una sumisión privada recibe un número `SUB-...`; todavía no es una publicación. Tras la liberación recibe un identificador público `ARR-YYYY-...`, una URL estable del registro y otra URL inmutable por versión. El prefijo histórico `ARR` se conserva para no romper citas aunque la marca sea AIRR.SCIENCE.

## Copias y recuperación

- El volumen privado del VPS está cifrado con LUKS2.
- La copia local cifrada se programa diariamente alrededor de las 04:10, con variación de hasta 15 minutos.
- La transferencia y verificación en B2 se programa alrededor de las 04:40, con variación de hasta 5 minutos.
- Se conservan las tres últimas copias locales y ninguna debe superar siete días.
- B2 utiliza un bucket privado en EU Central, prefijo `intake/`, y recibe archivos ya cifrados.
- La regla prevista en B2 oculta objetos después de cuatro días y los elimina un día después; la eliminación del proveedor puede no ser instantánea.
- El servidor solo conserva la clave pública de cifrado. La identidad privada necesaria para restaurar debe permanecer fuera del VPS.
- Tras reiniciar el VPS puede ser necesario desbloquear manualmente el volumen cifrado desde la consola de Netcup antes de iniciar AIRR.

Una copia dentro del mismo VPS no protege frente a la pérdida completa del servidor. Backblaze se conserva por ese motivo, aunque Netcup sea suficiente como servidor.

## Fechas y renovaciones que deben vigilarse

| Elemento | Fecha o frecuencia conocida | Acción |
|---|---|---|
| Netcup VPS | Facturación mensual; el contrato indicaba preaviso de 31 días | Mantener el pago activo y revisar avisos de factura |
| Dominio `airr.science` | Registro multianual en Porkbun | Anotar en el calendario la fecha exacta mostrada por Porkbun y activar renovación automática con método válido |
| Clave Brevo `AIRR Netcup intake` | Caducidad configurada: 7 de septiembre de 2027 | Sustituirla durante agosto de 2027 y enviar un correo de prueba |
| Clave B2 `AIRR-Netcup-backup-2026-09` | Caducidad configurada: 7 de septiembre de 2027 | Crear una nueva durante agosto de 2027, actualizar Netcup y verificar una copia completa |
| Certificado HTTPS | Renovación automática por Caddy | Investigar cualquier alerta; no renovarlo manualmente mientras Caddy funcione |
| Actualizaciones de seguridad | Comprobación semanal, domingo aproximadamente a las 02:15 | Programar reinicio manual si el monitor indica que es necesario |
| Prueba de restauración | Trimestral durante el piloto | Restaurar en un entorno aislado sin sobrescribir producción |

## Accesos que el propietario debe poder recuperar

- Porkbun: dominio, DNS y renovación.
- GitHub: organización/repositorio, Pages, Actions, Releases y alertas.
- Netcup CCP: contrato, facturación y DPA; Netcup SCP: consola del servidor.
- AIRR editor: contraseña, TOTP y ocho códigos de recuperación.
- Brevo: dominio autenticado, registros DNS, clave SMTP/API y registros de entrega.
- Backblaze: bucket, clave limitada y reglas de ciclo de vida.
- Identidad privada `age`/clave de recuperación del archivo cifrado, guardada fuera de Netcup.

El correo personal puede servir para recuperar cuentas, pero no debe utilizarse como almacén único de secretos. Como mínimo, conservar una segunda copia offline de los códigos de recuperación y de la clave privada de las copias cifradas.

## Operación normal

No hace falta administrar el servidor cada día. Los temporizadores realizan correo, mantenimiento, copias y comprobaciones. Actuar únicamente ante una alerta o antes de una actualización relevante.

Después de una alerta:

1. Abrir Netcup SCP y comprobar que el VPS está encendido.
2. Ejecutar el monitor sin notificaciones para identificar la comprobación fallida.
3. Revisar el servicio correspondiente y los registros del proveedor.
4. Corregir la causa; no reenviar correos con estado incierto sin revisar antes Brevo.
5. Repetir el monitor y confirmar que devuelve `ok: true`.

Antes de un reinicio o actualización:

1. Pausar temporalmente la recepción.
2. Finalizar correo y mantenimiento pendientes.
3. Crear y verificar una copia local y otra externa.
4. Aplicar el cambio con instantánea de reversión.
5. Si hubo reinicio, desbloquear y montar el volumen cifrado.
6. Reabrir la recepción únicamente después de comprobar la aplicación, el formulario, el panel editorial, correo y copias.

## Cuándo ampliar Netcup

No se contratará otro servidor por anticipado. Se revisará capacidad cuando ocurra alguno de estos hechos:

- acercamiento sostenido a 1.000 registros públicos;
- repositorio próximo a 1 GB;
- falta recurrente de disco o memoria;
- recepción simultánea que cause errores o tiempos de espera;
- procesamiento de PDFs que retrase el trabajo editorial;
- copias cifradas próximas al límite operativo de 500 MB;
- necesidad medida de búsqueda dedicada, PostgreSQL, colas o almacenamiento de objetos.

Mientras el uso sea principalmente el de los papers del fundador, Netcup es suficiente. GitHub Pages seguirá sirviendo el catálogo y Backblaze seguirá siendo la copia independiente.

## Documentos relacionados

- `docs/INTAKE_OPERATIONS.md`: recepción, límites y retención.
- `services/intake/deploy/OPERATIONS.md`: despliegue, cifrado, copias y recuperación.
- `docs/ANALYTICS_OPERATIONS.md`: estadísticas privadas de visitas.
- `docs/GOVERNANCE.md`: decisiones del fundador y conflictos.
- `docs/WORKFLOW.md`: publicación y creación de releases.
- `docs/SCALE_READINESS.md`: fases y señales de migración.

