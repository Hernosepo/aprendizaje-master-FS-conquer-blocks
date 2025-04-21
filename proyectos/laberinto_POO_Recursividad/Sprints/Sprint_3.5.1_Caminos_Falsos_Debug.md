
# 🧪 Sprint 3.5 – Validación y límites actuales de caminos falsos

## 🎯 Objetivo

Evaluar el comportamiento del método `agregar_caminos_falsos` frente a múltiples configuraciones de caminos y determinar su fiabilidad y aislamiento respecto al camino principal.

---

## 🔍 Hallazgos principales

- El sistema actual permite trazar caminos falsos con `0`s y marcarlos con `4` en ciertos escenarios controlados.
- Sin embargo, en múltiples casos:

  - La celda `falsa_salida` es sobrescrita por el trazado del camino, volviéndola ineligible para recibir el `4`.
  - La celda `falsa_salida` termina adyacente a `0`s del camino principal, invalidando el condicional actual o generando ambigüedad visual.

---

## 🧠 Diagnóstico técnico

- El `if` actual valida que `falsa_salida`:
  - Sea igual a `1`
  - No tenga vecinos con valor `0` arriba o abajo (izquierda/derecha comentados)

- Este control es **insuficiente** en casos donde la geometría del laberinto genera cercanía o cruce entre caminos verdaderos y falsos.

---

## 📌 Conclusión del Sprint

> El sistema actual de caminos falsos **no garantiza aislamiento completo** ni independencia visual/funcional del camino principal.  
> Requiere **una validación más profunda o separación lógica durante el trazado**.

---

## 🛠 Próximos pasos sugeridos

- Crear una estructura auxiliar temporal (lista o máscara) que almacene las coordenadas del camino falso durante su trazado.
- Validar que `falsa_salida`:
  - No esté en dicha ruta
  - No sea adyacente a `0`s de rutas no relacionadas

- Eventualmente: replantear el diseño para que `agregar_caminos_falsos` funcione como una función autónoma de construcción y validación previa.

---

📌 Este Sprint se cierra como un paso de **observación crítica y documentación de límites actuales**, quedando en espera de una mejora en futuros ciclos.
