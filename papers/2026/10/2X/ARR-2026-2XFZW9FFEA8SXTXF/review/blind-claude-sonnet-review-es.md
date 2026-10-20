# Revision ciega: "Finite convex interpolation for polynomial Lyapunov existence" (candidate-3/main.pdf)

Revisor Claude Sonnet 5.5, no humano, no independiente del autor (misma familia). Fecha 2026-10-20. Solo vi el PDF; no abri informes ni notas previas.

## Escala
Rubrica https://airr.science/assessments/ (leida): escala unica 0-10; 1 "Critical concerns", 2 "Substantial revision needed", 3 "Acceptable" (suelo de publicacion), 4 "Strong", 5 "Very good", 6 "Excellent", 7 "Exceptional", 8 "Potentially field-shaping", 9 "Potentially historic", 10 "Millennium-resolution benchmark". No es porcentaje. Aparte hay perfil de 5 estrellas (correccion, rigor, novedad, relevancia, reproducibilidad). Uso la escala para dos lecturas: calidad (correccion/rigor) e importancia.

## Veredicto
No encontre ningun error que invalide un resultado principal. Los teoremas parecen correctos; los resultados son de nicho y se apoyan en maquinaria clasica. Aporte genuino pero acotado: caracterizacion umbral de existencia de Lyapunov polinomico para campos planos homogeneos rotatorios, via problema de momentos / Pick confluente.

## Lo que intente romper
1. Umbral de momentos (Thm 2.1, 3.1): rehice a mano la derivacion (polar, Lie, Herglotz, signo de H, w_k = i m_k - q_k), el argumento de Jackson (cotas E_N y (6)), la estrictez via h_eps = (1-eps)h + eps(1-iQ) y la aproximacion por medidas empiricas. Todo cierra. A(q) = inf sobre medidas de probabilidad u de sup(q + Hu) es equivalente y limpio.
2. Pick confluente / cuadrante (Lemma 4.1, Prop 4.2, Lemma 4.3, Thm 4.4): dualidad de Slater correcta; el cuadrante via g=f^2 al semiplano es correcto; el conjunto de jets es convexo (convexa combinacion de aplicaciones al cuadrante con Im f(0)=1). Comprobacion independiente: LP de momentos (N hasta 120, rejilla fina) para q = b cos(phi) con b=2 da 0.4504 -> (b^(2/3)-1)^(3/2)=0.45020 (ec. 22 correcta, umbral |b|<(1+a^(2/3))^(3/2)); para el perfil 8.2 la LP converge a 1.6574 (N=120, decreciendo) frente a 1.657217310707 (Prop 8.1). El polinomio R(t) tiene la raiz 4.59278268929256 en (0,19/4) y 25/4 - t = 1.6572173107074 (comprobado con sympy a 30 digitos).
3. Prop 8.2 (grado minimo 8): P(x,y) es positivo (min en circulo 2.08) y -L_X P <0 (max -1.73) en rejilla fina; LP independiente maximizando min d sobre p de grado 2M: negativo para 2M=2,4,6 (-0.23, -0.037, -0.0020) y positivo para 8. Coherente con la identidad dual racional (margen en grado 6 muy pequeno, el argumento exacto es imprescindible y no lo reverifique simbolicamente).
4. Quintica (Lemma 9.1, Thm 9.2): el obstaculo es un promedio sencillo: <G Im h_alpha> = T_G(alpha), media sobre los factores de Fejer-Riesz; los factores de frontera se tratan bien (p no puede anularse donde G != 0 por el argumento de factor integrante). Verifique G0=sin(phi), F0 = -1+5sin^2(phi), <F0>=3/2, T_G0=Re(alpha), margen 1/2-7eps, la identidad (6+5t)^2-11(1-t^2)=(5+6t)^2, |v|<=5 sqrt(11)<17, F+Gv <= -1+18 eps = -1/10 con eps=1/20 (la cota por componente de 6 terminos da <=1/40+... < 1/20). Correcto.
5. Complejidad (Thm 5.1, 5.3): el esquema (K_delta cerrado, convexo, bola interior de radio r0 por Hermite, radio exterior, oraculo de pertenencia exacto por Schur, GLS Cor 4.3.12, contraccion hacia x0) es logicamente coherente y las dependencias de r0 en log T son polinomicas. No pude verificar linea a linea las constantes de la prueba de 5.3 (cotas de Cauchy/Mehlhorn-Sagraloff-Wang, recurrencia de series con L_0); parecen plausibles pero son densas y no estan implementadas.

## Objeciones materiales
- Novedad respecto a Liu-Fitzsimmons (arXiv:2607.16171): solo lei el resumen. Su "Section IV.D" (familia a dos parametros y robustez) no pude leerla; el umbral cerrado (1+a^(2/3))^(3/2) para la familia cubica podria solaparse con su analisis. Hay que comprobarlo antes de reclamar novedad del caso de un armonico.
- Korda 2609.22058: solo resumen; "Part III del suplemento" no verificado. La decidibilidad de estabilidad plana homogenea ya es conocida; lo nuevo aqui es la decidibilidad de existencia de certificado polinomico. Por Tarski, la decidibilidad abstracta es casi inmediata una vez se tiene la reduccion finita; el valor esta en la reduccion (umbral de momentos/Pick), no en la decidibilidad.
- Complejidad: es aproximacion aditiva de un valor + decision bajo promesa de hueco, no cota del tamano del certificado ni decision de igualdad; las cuatro piezas son clasicas (GLS, Pick, raices). Aporte real pero modesto y sin implementacion.
- Thm 9.2/Cor 9.3: la funcion racional (11x^2+y^2)^11/r^20 es del tipo de Ahmadi-El Khadir; la obstruccion es un argumento de promedios; el propio texto reconoce que LF ya dan contraejemplos robustos. El gran "cuadro de 12 dimensiones" es una suficiencia, no una clasificacion con ceros angulares.
- Sin verificacion formal (no Lean); varios pasos largos (5.3) dependen de lectura humana. Las pruebas de 4.3 (jets singulares de Pick) citan Clark 1968; no comprobe esa referencia.
- Honestidad del manuscrito: buena (limites declarados, fallos numericos conservados). Menciona revisor previo "GPT-6 Astra"; irrelevante para mi nota.

## Notas
- Calidad: 5.5/10 ("Very good"): rigor alto en lo comprobado, sin errores hallados, resultados independientes reproducidos numericamente; resta la densidad de 5.3 y las dudas de novedad.
- Importancia AIRR: 3.5/10 (entre "Acceptable" y "Strong"). Comparables: Liu-Fitzsimmons 2607.16171 (contraejemplo cubico con Lean) es claramente mas importante (~5-6) al resolver la conjetura abierta de Ahmadi-Parrilo; Ahmadi-El Khadir (Trans. Autom. Control 2020, ~4) fija la existencia racional; Korda 2609.22058 (indecidibilidad en dim 5, ~6-7). Este trabajo es un refinamiento decisorio/algoritmico para una clase de dimension 2, sin impacto fuera de ella.

Revisor Claude Sonnet 5.5, no humano, no independiente del autor.
