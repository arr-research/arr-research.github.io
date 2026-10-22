# Davies v2 — lista de cambios (21-10-2026)

Base: `D:\Entregas\airr\2026-10-17_capacidad-davies\candidate-3\main.tex` (PDF v1, sha a6382c9e…; D: no tocado).
Autor-revisor: sesión Claude Sonnet 5.5 (no humano, no independiente del autor).
Entrada: informes Haiku 5.5, Sonnet 5.5 (sala-limpia/d3), Sonnet 5.5 (hilos/d3-sonnet) y ADJUDICACION_HAIKU.md.

## Cambios hechos (ningún teorema, hipótesis ni cifra de v1 cambia)
1. **Fang (arXiv:2609.14621)**: citado en introducción (párrafo nuevo) y en «Several overlaps». Descrito solo según resumen + HTML v2 (Cor. 2: C=χ para todo γ,N∈[0,1]; exponente strong-converse; aditividad Rényi α>1). Dicho en el texto: en λ²=k la igualdad C=χ del Teorema 1 NO es nueva respecto a Fang (ni OpenAI); lo añadido es el interior, la aditividad con compañero arbitrario (el resumen de Fang no la enuncia), complemento y simulación. Sus pruebas NO las he comprobado (dicho en el texto).
2. **Subaditividad (eq. 18, antes 17)**: prueba completa en 4 pasos (representación producto, registros clásicos I,J, marginales por trazo-preservación, cadena SSA), cita explícita Tang App. C, Lemas C.1/C.2. Resultado un poco más fuerte (puntual en entradas conjuntas). La cadena de v1 no estaba «garbled»: era correcta pero escueta; ahora no depende del lector.
3. **Pasos «asertados» escritos**:
   - Fórmula de Kraus de G_M para entradas singulares (HJW), concavidad (ínfimo de cóncavas), continuidad (√σ continua + continuidad de E_F), maximizador diagonal para Φ^c (promedio con Z).
   - Prop. 12: identidad de la cuerda (Bayes, eq. 21), concavidad de e_p ⇒ G=J en el intervalo explícito p∈(13/27−√595/54, 13/27+√595/54)≈(0.0298,0.9332), J'(1/2)=(1/10)ln(2⁶3⁹/7⁷) deducida, comparación; se separa qué parte usa solo entradas producto (la desigualdad estricta NO usa (18) ni la igualdad del Teorema 10).
   - Cor. 11: región c≤x≤k = región de convexidad (Vieta: raíces de 4AD−B² son c y c', c+c'=2k+4ab, cc'=k², k²≤c≤k≤c'), cierre del revés (c(a_p,b_p)=Lc), sustitución t_p(t)=p, máximo en p=1/2. La convexidad de e (antes citada a Hellmund–Uhlmann) se demuestra directamente (Sección 4: √v norma afín; G'(s)=2y/sinh y).
   - Teorema 9: promedio de fase explícito. Teorema 1: notación ω̄_{B'} y contabilidad de la desigualdad.
4. **Apéndice A «Reproducibility»**: tabla guion → qué reproduce → comparación. Descomprimido el supplement.zip, ejecutados los 9 guiones (Python 3.12.6, numpy 2.2.6, scipy 1.18.0, mpmath 1.3.0): todas las cifras del texto coinciden (tabla 0.503934607/0.407849860/0.296671803/0.436551160; complementos; formación; 0.600876037; 0.704192652/0.704712865; 16000 y 9000/27000/1200/300 sin violación).
5. Dos guiones nuevos (`supplement-v2.zip → checks/`): `verify_v2_steps.py`, `verify_flat_region.py` (sympy: J'(1/2), intervalo, Bayes, cuerda=J, Vieta).
6. Párrafo «Version 2» (honesto sobre autoría IA y dependencias), bibliografía +4 (Fang, HJW, Nielsen, Winter), fecha de versión.

## Corrección menor numérica
- «0.704712865 near p=0.516949108»: 0.516949108 es el valor de malla; el máximo con 75 dígitos es 0.516949105. Se dice ambas cosas. Nada más discrepó.

## Lo que NO se pudo arreglar / sigue como dependencia
- **Lema 2 (Tang Thm 4.2 / OpenAI Thm 2.1) sigue externo**: toda la cadena depende de él. Comprobé el enunciado de Tang en su PDF local, no su prueba. La nota OpenAI [3] no se ha re-localizado en esta revisión.
- Continuidad de E_F (Nielsen, Winter), teorema HJW y fórmula operativa de Berta et al. (Thm 12) son externos (declarados). Winter/Nielsen solo se verificaron por su resumen arXiv.
- Fang: solo resumen/HTML, pruebas no leídas.
- No ampliados (los revisores los llamaron escuetos): extremalidad con ≤2/3 átomos (Prop. 8 y eq. 10, bordes), identificación de dilaciones en Teorema 6 (complemento), cierre/continuidad en Teorema 10 en bordes, Lipschitz en m=0, comparación de Teorema 6 con literatura de no aditividad. No se inventó nada para ellos.
- Numéricas siguen sin certificación por intervalos; no independientes (misma familia de modelos).
- La objeción «Lema 2 no verificado» del revisor Sonnet no es resoluble desde el manuscrito.
