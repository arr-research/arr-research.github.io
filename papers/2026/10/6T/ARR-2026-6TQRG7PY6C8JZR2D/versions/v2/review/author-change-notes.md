# CAMBIOS v1 -> v2 (Schur candidate-3), 21-10-2026

Base: `D:\Entregas\airr\2026-10-18_residuos-schur\candidate-3\main.tex` (sha256 aa03f631...; PDF v1 publicado ARR-2026-6TQRG7PY6C8JZR2D, sha 28ed664c...). D: no tocado; trabajo en `C:\Trabajo\investigador-airr\v2\schur-c3`.
Autor-revisor: Claude Sonnet 5.5 (no humano, no independiente). Resultados y enunciados NO cambian (Teoremas 1-3, 11, Prop. 12, Cor. 8-9 idénticos; numeración idéntica).

## Hecho (con prueba escrita en el texto)
1. **Nuevo Apéndice A** (Lemas A.1-A.4, Prop. A.5, "estimación maestra" con constantes explícitas):
   - A.1 módulos de la base: forma exacta de H_c(s), punto y valor del máximo secundario, (1+c)^6/[729(1-c)^2] < 0,631 para 0<=c<=3/4 (derivación completa, pedida en 2), H_{1/2} <= e^{-3s}, H_c <= e^{-2s} si |c-1/2|<=1/10, y H_{a,c} <= e^{-6s} cerca de (-2/3,3/4) (existencia de eps0 por continuidad).
   - A.2 factor interior (cota (16) de v1): identidad exacta 1+8(x^2-x-Y)s+16UVs^2, UV-(x^2-x-Y)^2=(2x-1)^2 Y, cota e^{4(U+V)s}; derivada normalizada L<=6|v|^2.
   - A.3 cota local (17): serie exacta con momentos anulados, |P'/P-lambda| <= 2|z-1|^K sum|v|^{K+1}; cota inferior del denominador exp(-4 Sigma2 theta^2) (segunda derivada de log|z-beta|^2).
   - A.4 arco exterior: regla del producto por grupos, sin cocientes en ceros; |P'|/|P(1)| <= Lambda e^{sT/2}.
   - A.5 acotación final de rho^2 con todas las constantes.
2. Pruebas de Teoremas 2 y 11 reescritas sobre esas estimaciones (verificación de hipótesis una a una). Independencia de las 34 clases de residuo: probada (mapa analítico (d,t)->(X,Y), discriminante 289/2*529/2>0, cotas uniformes en k). Las 6 clases del Teor. 3: cubiertas por A.1(d).
3. Lema 10 (pesos positivos): demostración rehecha; se explicita que el funcional es real (columnas reales), con lo que la observación "a_l real" de Haiku queda cubierta; racionalidad y positividad estricta detalladas.
4. Lema 4: m_1 real y >= 1/2 vía media de Re v_j, con Re v_j >= 1/2 derivado de |1-beta|^2 <= 2(1-Re beta).
5. Teorema 3: aclarado que el desarrollo de Mathieu es de una variable (O(L^{-1/2}) uniforme en L>=L0, sin uniformidad extra en lambda); paso explícito de cuadrado a raíz (1/8 -> 1/sqrt 8); párrafo "convención de cuadrados" (rho=O(n^{-1/6}) <=> rho^2=O(n^{-1/3})).
6. Sección 8: párrafo "Versión 2" con lo que sigue sin probar/efectivo. Fecha del título actualizada.

## Comprobaciones numéricas (carpeta `verif\`, logs en `verif\logs\`; no forman parte de ninguna prueba)
- v2_lemmas: A.1 en rejilla de 2e6 puntos; identidad del par interior (1e5 pruebas, 0 fallos); construcción Thm 11 a 60 dígitos (D-d, T-t ~ 1e-60 hasta n=1e15).
- v2_thm11: identidades exactas sum v=P'(0), sum v^2, sum v^3 (~1e-45) hasta n=1e9; rho^2 n^{1/3} = 0,46 (n=1e4) ... 0,37 (n=1e12); círculo completo coincide con ventana; exponente global ~ -1,1 n s (mi cota usa -n/7); la cota maestra con mis constantes es >= rho^2 real pero solo < 1 para n >~ 1e21.
- v2_cone/v2_thm2 (K=3): solución racional exacta del cono (Q=2, nodos reales 1,2,3 con m=2; pares (1+i)/2 m=47, (1+3i)/2 m=7; M=114); IFT resuelta a 60 dígitos; identidades exactas; rho^2 n^{1/3} -> 771 (constante enorme, estable) de n=1e9 a 1e21. K=4,5: solo comprobada por LP la existencia del cono, sin solución racional ni residuo.

## NO se pudo arreglar / sigue siendo esbozo o no efectivo
- M_A, C_A, N_A siguen sin cota efectiva; el entorno del teorema de la función implícita (Thm 2) y eps0 (A.1(e)) son solo de existencia.
- Las constantes de la Prop. A.5 son astronómicamente pesimistas (cota <1 solo para n >~ 1e21 en Thm 11); no se afirma ningún grado inicial numérico.
- No tocados (fuera de lo pedido): el argumento de grado impar (|p| en H^1) y la cita del desarrollo DLMF 28.8.1 (no demostrado aquí); la cota local C(1+|theta|+m theta^2) del Teor. 3 sigue esbozada; prioridad/novedad no certificadas; auditoría de 34 clases y suplemento citados en la Sec. 8 son los de v1 (`v1_meta\supplement.zip`, no regenerado).
- Teorema 2 con K>=4 solo respaldado por la prueba, no por cálculo numérico completo.

## Archivos
- `main.tex`, `main.pdf` (17 páginas; compilado con tectonic, 0 referencias rotas, 0 overfull; las 17 páginas revisadas como imagen).
- sha256 main.pdf = 75332dab56cc67dbb3df0f61ffa49f532e258ce8c22ac2b7439477dc35ebaf44
- sha256 main.tex = f6b5195f0974bc812ca3a924b285028f3ed009fddce1b099767f7c4972f5a46b
- `v1_meta\`: manifiestos, PDF y fuente de v1 (obsoletos para v2).
- Incidente: un `taskkill` de python.exe mío para cortar un script colgado pudo terminar procesos python de otras sesiones; conviene revisar hilos en marcha.
