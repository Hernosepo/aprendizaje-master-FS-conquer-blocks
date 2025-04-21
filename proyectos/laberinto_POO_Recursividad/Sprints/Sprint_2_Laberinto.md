
# 🧭 Sprint 2 – Generación de Ruta Válida en el Laberinto

## 🎯 Objetivo del Sprint

Modificar la matriz del laberinto generada previamente para construir una **ruta continua de `0`s** desde la posición de `inicio` hasta `salida`, marcando la salida con un `9`.

---

## ⚙️ Implementación

- Se implementó el método `generar_ruta()` dentro de la clase `Laberinto`.
- Se realizaron las siguientes operaciones:
  - Uso de `self.matriz[:, self.inicio[1]] = 0` para modificar una **columna completa** desde el punto de inicio (ruta vertical).
  - Uso de `self.matriz[self.salida[0]] = 0` como forma de marcar una **fila completa** que representa la conexión horizontal (siguiente paso a refinar).
  - Posicionamiento exacto de la salida con `self.matriz[self.salida] = 9`.

---

## ✅ Resultado final del Sprint 2

- La matriz del laberinto ahora contiene una ruta clara de `0`s entre `inicio` y `salida`, usando una combinación de trazado vertical y horizontal.
- Se logró comprender y aplicar:
  - Acceso a columnas completas en NumPy (`:`)
  - Diferencia entre acceso vertical y horizontal en matrices 2D
  - Escritura de valores dinámicos en celdas específicas

---

## 🧠 Reflexión técnica

- Se detectaron errores comunes en el acceso a coordenadas (confundir `fila` con `columna`).
- Se comprendió la sintaxis de NumPy para acceder a subconjuntos de una matriz.
- Se validó que adaptar código externo (consciente y reflexivo) puede aportar valor real si se comprende lo que se aplica.

---

## 🚩 Listo para avanzar al Sprint 3:
Agregar caminos falsos y preparar la matriz para resolución recursiva.
