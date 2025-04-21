# 🧩 Ejercicio de Laberinto – POO y Recursividad

Este proyecto surge como parte del entrenamiento en Programación Orientada a Objetos (POO) dentro del Máster Full Stack de Conquer Blocks. El objetivo inicial era construir un laberinto representado como una matriz, con la capacidad de trazar rutas posibles, tanto verdaderas como falsas, y dejarlo preparado para una futura resolución recursiva.

---

## 🎯 Objetivo general

- Aplicar conceptos de clases, métodos y atributos en un proyecto simple pero extensible.
- Diseñar una estructura clara que permita trabajar sobre un “laberinto” dinámico.
- Preparar una base funcional para luego implementar una función recursiva que encuentre la salida correcta.

---

## ⚙️ ¿Qué hace este programa?

- Crea un laberinto de `n` filas por `m` columnas, lleno de `1`s (paredes).
- Traza un camino válido entre un punto de inicio y uno de salida (reemplazando por `0`s y marcando la salida con `9`).
- Permite agregar caminos falsos que parten desde el camino principal y terminan en una celda `4`, simulando bifurcaciones engañosas.
- Imprime visualmente la estructura del laberinto como matriz.

---

## 📌 Elementos clave

- **`Laberinto`** es la clase principal.
- Métodos relevantes:
  - `generar_ruta()`: genera el camino real (inicio → salida).
  - `agregar_caminos_falsos()`: permite añadir caminos falsos a partir de coordenadas dadas.
  - `mostrar_laberinto()`: devuelve la representación actual del laberinto.

---

## 🧠 Estado actual

- La generación de caminos falsos funciona bajo ciertas condiciones, pero se encuentra **en fase de depuración**.
- Se documentaron varios casos exitosos, y también se detectaron situaciones donde los caminos falsos no se marcan correctamente con `4`.
- Está previsto refinar la validación para el próximo sprint, posiblemente con una estructura auxiliar o lógica más robusta.

---

## 🚀 Próximos pasos

- Implementar un algoritmo recursivo para resolver el laberinto.
- Definir reglas claras para elegir entre múltiples caminos (`0`, `4`, etc.).
- Posible visualización de recorrido y retroceso (backtracking) dentro del laberinto.

---

## ✍️ Notas personales

Este ejercicio me sirvió para afianzar conceptos clave de POO como encapsulamiento y diseño modular. También me permitió enfrentarme a errores lógicos más complejos y pensar en validaciones progresivas. Todavía hay cosas que ajustar, pero creo que el núcleo del sistema está sólido y preparado para lo que viene.

---

📁 Este archivo forma parte de mi repo de seguimiento del máster:  
**[`aprendizaje-master-FS-conquer-blocks`](https://github.com/Hernosepo/aprendizaje-master-FS-conquer-blocks)**
