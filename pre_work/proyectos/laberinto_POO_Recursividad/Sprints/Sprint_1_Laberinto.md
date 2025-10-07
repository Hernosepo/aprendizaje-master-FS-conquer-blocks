
# 🧭 Sprint 1 – Generación de Laberinto Vacío

## 🎯 Objetivo del sprint

Crear la clase `Laberinto` con la estructura mínima necesaria para:

- Definir una grilla de tamaño personalizado (`filas` x `columnas`)
- Establecer coordenadas de `inicio` y `salida`
- Generar una matriz de paredes (`1`s) como base del laberinto

---

## ⚙️ Implementación

- Se utilizó **NumPy** para construir una matriz inicial de paredes, usando:
  ```python
  np.ones((filas, columnas))
  ```

- Se definieron los siguientes atributos en la clase:
  - `filas`: cantidad de filas del laberinto
  - `columnas`: cantidad de columnas
  - `inicio`: coordenada de entrada al laberinto
  - `salida`: coordenada de salida del laberinto
  - `matriz`: grilla base del laberinto, inicialmente toda con `1`s

- Se implementó un método auxiliar `mostrar_laberinto()` que permite visualizar la matriz generada.

---

## ✅ Resultado final del Sprint 1

- Clase funcional instanciada con valores de prueba: `4 x 4`, inicio en `(2,1)`, salida en `(4,1)`
- Matriz correctamente construida como una cuadrícula 2D llena de `1`s
- Impresión de la matriz validada correctamente desde la instancia

---

## 🧠 Reflexión técnica

- Se identificó correctamente la diferencia entre métodos y atributos en Python
- Se resolvió una estructura de comprensión anidada incorrecta
- Se validó el uso de NumPy como herramienta válida para esta etapa
- Se afianzó el concepto de estructura de datos 2D

---

## 🚩 Listo para avanzar al Sprint 2:
Generación de una ruta válida de `0`s desde `inicio` hasta `salida`
