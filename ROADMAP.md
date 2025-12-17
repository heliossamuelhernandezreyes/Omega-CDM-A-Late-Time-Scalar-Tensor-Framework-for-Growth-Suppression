# 🗺️ Hoja de Ruta: El Programa de Investigación Omega

Este documento define la trayectoria del marco teórico **Omega**, dividiéndolo en dos pilares fundamentales que conectan la cosmología de gran escala con la física de campos fuertes.

---

## 🔵 Fase 1: Omega-CDM (Completada)
**Estado:** Estable, calibrada numéricamente y validada observacionalmente.

Esta fase establece la base cosmológica del programa:
* **Resolución de Tensiones:** Proporciona un mecanismo para aliviar la tensión $S_8$ mediante una supresión del crecimiento del **5%--8%** en $z=1$.
* **Implementación Numérica:** Código v1.1 basado en integración de segundo orden (`solve_ivp`) con acoplamiento $\beta = 0.25$.
* **Firma Observacional:** Predicción de un índice de crecimiento $\gamma \simeq 0.63$, distinguible de la Relatividad General.

---

## 🔴 Fase 2: Omega-Strong (Próximamente)
**Estado:** En fase de diseño conceptual y desarrollo de métrica.

La hipótesis central es que el mismo grado de libertad escalar $\Omega$ que actúa en la cosmología puede regularizar las singularidades gravitacionales.



### 🎯 Objetivos de Investigación:

1. **Completitud No Lineal:** Evolucionar el acoplamiento disformal para que dependa de invariantes locales de curvatura y densidad:
   $$\beta \longrightarrow \beta(\rho, R, X)$$.
2. **Núcleos de de Sitter:** Investigar soluciones de objetos compactos donde la singularidad de Schwarzschild es reemplazada por un núcleo de vacío regular de curvatura finita.
3. **Unificación de Escalas:** Asegurar que el límite de baja densidad recupere la fenomenología de Omega-CDM:
   $$\lim_{\rho \to 0} G_{\mathrm{eff}}^{\text{strong}} = G_{\mathrm{eff}}^{\text{CDM}} \longrightarrow 1$$.

---

> **Perspectiva:** Omega-CDM proporciona la validación observacional necesaria, mientras que Omega-Strong representa la exploración hacia el comportamiento ultravioleta de la gravedad.
