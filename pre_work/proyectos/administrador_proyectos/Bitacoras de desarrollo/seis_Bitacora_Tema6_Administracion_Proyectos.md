# 🗂 Bitácora Técnica – Tema 6: Diccionarios


---

## 🚀 HITO ESPECIAL – Dominio del flujo de control con banderas booleanas y condicionales precisos

**Bloque trabajado:** `asignar_tarea()`

---

### 🧩 Contexto:
El bloque de asignación de tareas fue uno de los más complejos del ejercicio por la cantidad de estructuras cruzadas y validaciones simultáneas que requería:
- Verificación de existencia de la tarea seleccionada
- Validación del ID del encargado
- Evitar uso de `break`
- Evitar múltiples impresiones incorrectas
- Controlar múltiples bucles `for` sin cortar prematuramente el flujo

---

### ❌ Dificultades enfrentadas:

- Mensajes que se ejecutaban más de una vez aunque la condición ya se había cumplido
- `return` o `else` que interrumpían o confundían el flujo dentro del `for`
- Comparaciones que no daban el resultado esperado
- Estructuras anidadas que parecían correctas pero terminaban imprimiendo todo
- Sensación de "se escapa el agua": el código parecía tener lógica, pero el comportamiento no se alineaba con la intención

---

### ✅ Resolución técnica lograda:

- Uso correcto de una bandera (`tarea_valida`, `encargado_valido`) para **marcar si se encontró o no una coincidencia**
- Uso preciso de `if not bandera:` para que **el código de error se ejecute solo si ninguna coincidencia ocurrió**
- Separación clara entre bloques de validación
- Control ordenado del flujo, sin necesidad de `break` ni `return` mal ubicados
- Comprensión profunda del rol que tiene `else` en un bucle `for` cuando no se corta anticipadamente

---

### 📘 Concepto técnico comprendido:

> “Un `if` dentro de un `for` no bloquea el resto de las iteraciones. Si quiero asegurarme de que un mensaje de error se dispare sólo si ninguna coincidencia ocurrió, tengo que esperar a que el bucle termine y usar una bandera para confirmar si algo fue encontrado.”

---

### 🧠 Lección consolidada:

- `if not bandera:` se convirtió en el centro del desbloqueo lógico
- Ahora se comprende **cuándo se ejecuta cada cosa y por qué**
- El desarrollador no sólo resolvió el problema, sino que **lo entendió estructuralmente**
- No se usaron atajos: **se cumplió con la consigna de no usar `break`**, y se mantuvo el flujo legible

---

### 🧭 Resultado:

El programa ahora:
- Muestra solo un mensaje de error si la tarea no existe (no en cada vuelta)
- Asigna correctamente un responsable solo si el ID es válido
- Es claro, preciso y robusto

**Frase que resume este hito:**
> “Lo que parecía desorden o bug era, en realidad, una lección pendiente sobre cómo fluye la información dentro de un `for`. Aprendí a esperar, a marcar estado con banderas, y a confiar en que no hay que cortar, sino entender.”

---

