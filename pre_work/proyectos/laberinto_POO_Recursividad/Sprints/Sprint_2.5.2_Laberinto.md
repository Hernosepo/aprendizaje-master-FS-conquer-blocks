
# 🧭 Sprint 2.5 – Ruta Precisa Conectada de Inicio a Salida

## 🎯 Objetivo del Sprint

Ajustar el método `generar_ruta()` para que trace una **ruta mínima y precisa** desde la posición `inicio` hasta `salida`, sin desbloquear filas o columnas completas.  
La ruta debía estar compuesta solo por `0`s, y la salida marcada con `9`.

---

## ⚙️ Implementación

- Se ajustó `generar_ruta()` para que:
  - Recorra las filas desde `inicio[0]` hasta `salida[0]` manteniendo la columna fija (`inicio[1]`)
  - Luego recorra las columnas desde `inicio[1]` hasta `salida[1]` manteniendo la fila fija (`salida[0]`)
  - Finalmente se marca `self.matriz[self.salida] = 9` como punto de llegada

- Se utilizó `range(..., ... + 1)` para incluir el índice final, ya que `range()` excluye el límite superior por defecto.

---

## ✅ Resultado final del Sprint 2.5

- El laberinto tiene una única ruta clara y mínima de `0`s desde `inicio` hasta `salida`
- No se modificaron otras celdas fuera de ese camino
- La ruta es visualmente reconocible
- El método está listo para permitir caminos falsos y aplicar recursividad posteriormente

---

## 🧠 Reflexión técnica

- Se entendió con claridad cómo usar `range()` para incluir el punto de llegada
- Se afianzó el concepto de acceso a celdas puntuales con `self.matriz[fila, columna]`
- Se ganó confianza en la manipulación precisa de NumPy 2D sin afectar toda la estructura

---

## 🚩 Listo para avanzar al Sprint 3:
Agregar caminos falsos y preparar el laberinto para ser resuelto recursivamente.
