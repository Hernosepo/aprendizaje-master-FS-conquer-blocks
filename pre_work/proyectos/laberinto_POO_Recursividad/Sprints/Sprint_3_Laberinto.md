
# 🧭 Sprint 3 – Caminos Falsos con Coordenadas Manuales

## 🎯 Objetivo del Sprint

Agregar uno o más caminos falsos al laberinto utilizando coordenadas definidas manualmente para representar ramificaciones que simulan rutas posibles pero terminan en un callejón sin salida, marcado con un `4`.

---

## ⚙️ Implementación

- Se creó el método `agregar_caminos_falsos(self, falso_inicio, falsa_salida)` que traza una ruta con `0`s entre dos coordenadas.
- Se utiliza un `if` para validar que la celda de `falsa_salida`:
  - Tiene valor original `1`
  - No está rodeada (por arriba y abajo) de `0`s, para asegurar que no se una visual ni funcionalmente con la ruta principal

- Si se cumplen esas condiciones, se marca con `4` como final del camino falso.

---

## ✅ Resultado final del Sprint 3

- El laberinto ahora tiene al menos un camino falso bien definido que:
  - Nace desde la ruta principal
  - Se extiende lateralmente con `0`s
  - Finaliza con un `4` como marcador de callejón sin salida

- El `4` es útil tanto visualmente como para futuros algoritmos recursivos que puedan detenerse en él.

---

## 🧠 Reflexión técnica

- Se identificó un bug importante: si las celdas vecinas laterales (`izquierda`, `derecha`) son parte del mismo camino falso, el `if` lo bloqueaba por considerar que estaba conectado con `0`s, incluso si esos `0`s eran del mismo desvío.
- Solución temporal: se comentaron las validaciones de izquierda y derecha, manteniendo solo arriba y abajo.
- Tema pendiente: pensar una forma de **distinguir los `0`s del camino falso actual** para no falsear la validación.

---

## 🚩 Laberinto listo para Sprint 4:
Implementar resolución recursiva, considerando caminos múltiples y finales válidos (`9`) o falsos (`4`).
