# Sharp inertia ceilings and optimal stability for inverse self-commutators

Autor: Lluis Eriksson. Fecha: 5 de septiembre de 2026.

Este paquete corresponde a *Sharp inertia ceilings and optimal stability for inverse self-commutators*, revisión 3. Incluye la fuente completa y el PDF de 15 páginas. Primera versión pública prevista en ARR: v1; la etiqueta interna del PDF es revisión 3. El autor ha aprobado el depósito. DEPOSIT_DECISION.json documenta su firma, el conflicto de autor-editor y la excepción específica a la regla editorial ordinaria.

## Mejora principal

La sección 5.5 demuestra que, para inercia (3,3), las dos constantes óptimas son 17/36 y 1: (17/36) D_* <= delta <= D_*. La enumeración geométrica abarca 22 vértices. Los testigos comunes satisfacen 11.484 desigualdades de Horn en aritmética racional. La revisión interna independiente regenera las 522 ternas mediante tableaux de Littlewood-Richardson y obtiene los mismos vértices por intersección de aristas. El extremo y su aproximación dentro del estrato funcionan con cualquier número fijo de ceros ambientales.

El artículo reúne la cota óptima por inercia, las constantes óptimas no equilibradas, la clasificación de casi extremizadores y el transporte con su ejemplo de separación. El caso equilibrado de multiplicidad >=4 sigue abierto en una dirección. No se afirma prioridad externa exhaustiva ni arbitraje humano.

## Reproducir los certificados

Desde el directorio de este archivo, con Python 3.10 o posterior:

```text
python replay/verify_balanced_three.py
python replay/independent_balanced_review.py
python replay/commutator_inertia.py
python replay/stability.py
python replay/transport.py
python replay/sharp_stability_verify.py
python replay/independent_review_checks.py
```

Los primeros cinco programas sólo necesitan la biblioteca estándar. Los últimos dos requieren SymPy (comprobados con 1.14.0). El verificador nuevo usa `balanced_exploration.json` como una lista de testigos racionales propuestos; no ejecuta optimización flotante ni confía en los valores propuestos sin verificarlos. La suficiencia clásica de Horn es una dependencia matemática explícita.

`INDEPENDENT_REVIEW.md` delimita la revisión separada. `VERIFICATION.json` registra los replays ejecutados en este paquete. `MANIFEST.sha256` identifica los archivos entregados. `certificates/` y los JSON junto a los verificadores conservan los resultados.

## Reproducir el PDF

```text
python -m pip install reportlab matplotlib pillow
python typeset/build_pdf.py
```

El PDF se compone con ReportLab y fórmulas a 480 dpi. Los archivos de composición son auxiliares; el texto matemático completo está en `paper.md`. La revisión visual cubre todas las páginas finales.

## Bibliografía consultada

La nueva comprobación usa la descripción primaria de Fulton, https://arxiv.org/abs/math/9908012, y los antecedentes de Eriksson identificados en el manuscrito. Consulta bibliográfica acotada del 5 de septiembre de 2026; no certifica prioridad. Las consultas «self-commutator stability inertia», «inverse self-commutator 36 17» y «self-commutator Hilbert-Schmidt minimum stability» no identificaron un enunciado primario coincidente. Los resultados irrelevantes no se usaron como soporte matemático.

## Alcance editorial y correspondencia de certificados

Este depósito founder_pilot cuenta con aprobación del autor-editor Lluis Eriksson. No cuenta con una decisión editorial humana independiente. La evaluación interna de GPT-6 Astra Max se conserva íntegra en screening/ y en el registro de evaluaciones; no participa en la puntuación agregada de modelos independientes.

CERTIFICATE_MAP.md identifica los programas que respaldan cada resultado y distingue el coeficiente histórico n/2 del coeficiente nuevo (n-1)/2. REFERENCE_LOCATORS.json proporciona los localizadores de los antecedentes comprobados. El PDF y la fuente matemática conservan exactamente los hashes revisados por el autor.
