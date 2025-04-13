# 🗂 Bitácora Técnica – Tema 6: Diccionarios


---

## ✅ Hito técnico alcanzado – Validación correcta de tareas y control de flujo interno

**Bloque trabajado:** asignar_tarea()

---

### 🧩 Situación inicial:
El programa imprimía que la tarea no existía aunque sí estuviera en el diccionario. El mensaje de error aparecía incluso si se ingresaba una tarea válida. Esto generaba confusión porque la lógica general del flujo estaba bien armada.

---

### 🧪 Errores y suposiciones que aparecieron en el proceso:

- ❌ Se asumió que `almacenador_tareas[chequeo_eleccion] == tarea_seleccionada` era la forma correcta de comparar la tarea seleccionada. En realidad, eso comparaba un **subdiccionario** completo contra un string, lo cual nunca dará True.
- ❌ El `else` dentro del `for` se ejecutaba en cada vuelta, haciendo que el mensaje de error se dispare incluso cuando la tarea ingresada sí existía, pero aún no se había alcanzado en la iteración.
- ❌ Se usaron `return` dentro del `for`, interrumpiendo la ejecución antes de completar todas las vueltas del bucle.
- ❌ Se intentó resolver la validación demasiado pronto dentro del bucle, sin esperar al final para saber si la tarea estaba o no.

---

### ✅ Lo que se corrigió y razonó correctamente:

- ✔️ Se entendió que para saber si algo no existe en una iteración, hay que esperar a terminar de revisar todas las opciones.
- ✔️ Se corrigió el foco de la comparación, validando directamente `chequeo_eleccion == tarea_seleccionada`.
- ✔️ Se comprendió el uso adecuado del `else` asociado a un `for`, y se empezó a manejar con lógica de control estructurada.
- ✔️ Se mejoró el criterio para separar mensajes de error reales de pasos dentro del flujo.
- ✔️ Se validó visualmente que los datos se impriman solo cuando corresponden.

---

### 📘 Conceptos técnicos consolidados:

- Diferencia entre **clave** y **valor** en un diccionario.
- Qué devuelve realmente `almacenador_tareas[clave]` → un subdiccionario.
- Flujo de ejecución de un `for` con condicionales internas.
- Problemas de romper la ejecución prematuramente con `return` dentro del bucle.
- Importancia de la **precisión en la comparación de tipos** (`string` vs `dict`).

---

### 🧠 Fortalezas del desarrollador:

- Excelente lectura del flujo de programa.
- Capacidad para comentar sus propios razonamientos y detectar incoherencias.
- Persistencia frente al bloqueo lógico sin caer en pedidos de solución directa.
- Buena comprensión del uso de estructuras complejas (diccionarios anidados).
- Clara disposición al aprendizaje a partir del error.

---

### ⚠️ Puntos a prestar atención:

- Ser preciso con lo que se compara: clave, valor, string, dict...
- Evitar cortar el flujo del `for` con `return` si no se tiene certeza.
- Usar banderas o estructuras alternativas si se necesita validar algo al final del bucle.
- Validar los tipos de datos antes de operar sobre ellos o compararlos.

---

**Frase resumen del hito:**
> “No basta con que la lógica general esté bien: hay que observar con precisión qué se compara, cuándo se ejecuta y cómo se interrumpe el flujo. Ahí está la diferencia entre un código que casi funciona y uno que funciona con claridad.”

