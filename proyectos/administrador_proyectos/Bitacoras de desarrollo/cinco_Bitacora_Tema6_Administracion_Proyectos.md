# 🗂 Bitácora Técnica – Tema 6: Diccionarios


---

## ✅ Análisis técnico – Comparación lógica entre bloques similares que no producen el mismo resultado

**Bloques comparados:**
1. Comparación entre `encargado_seleccion` y claves de `almacenador_tareas`
2. Comparación entre `nombre_tarea` y claves de `almacenador_tareas`

---

### 🧪 Confusión observada:

Ambos bloques usan una estructura de `for` + `if` aparentemente similar, pero solo uno de ellos funciona como se espera. Esto generó frustración y llevó a revisar si el problema estaba en el operador, en las variables, o en ambos.

---

### 🧠 Descubrimiento y análisis:

- En el primer bloque, se compara un **ID de persona** (`P1`, `P2`, etc.) contra las claves de un diccionario que contiene **tareas**, no personas. Es un problema de **universo de búsqueda**: la estructura que se recorre no contiene lo que se intenta encontrar.
  
- En el segundo bloque, se compara un string (`nombre_tarea`) con las claves del diccionario correcto (`almacenador_tareas`), por lo tanto el comportamiento es coherente con lo esperado.

---

### 📘 Concepto técnico aprendido:

> “Dos bloques pueden parecer iguales en forma, pero si el conjunto sobre el que iterás y el tipo de dato que comparás no coinciden en naturaleza, el resultado será lógicamente distinto aunque sintácticamente se vea similar.”

---

### ✅ Fortalezas reforzadas:

- Buen ojo para detectar inconsistencias lógicas aunque la sintaxis parezca correcta.
- Persistencia para revisar desde lo conceptual y no solo desde el código.
- Correcto enfoque al pedir explicación **sin resolución**, priorizando la comprensión.

---

### ⚠️ Punto a reforzar:

- Siempre validar si las estructuras que se recorren contienen realmente el tipo de dato o valor que se espera comparar. Esto reduce falsos negativos en condicionales y previene errores lógicos.

---

### 🔁 Aplicación directa:

Este aprendizaje permite construir comparaciones más sólidas en estructuras cruzadas y refuerza la atención sobre el uso correcto de claves y valores.

