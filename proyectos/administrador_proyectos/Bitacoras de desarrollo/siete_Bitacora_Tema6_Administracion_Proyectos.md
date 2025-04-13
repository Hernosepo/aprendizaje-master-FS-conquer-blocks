# 🗂 Bitácora Técnica – Tema 6: Diccionarios


---

## ✅ Bloque cerrado – Asignación completa de tareas, responsable y equipo

**Función consolidada:** `asignar_tarea()`

---

### 🧩 Funcionalidad implementada:

- Mostrar lista de tareas y permitir selección por nombre
- Validar existencia de la tarea seleccionada
- Mostrar lista de personas y permitir elegir un encargado por ID
- Validar existencia del encargado y evitar IDs inválidos
- Mostrar nuevamente la lista de personas y permitir selección de integrantes para el equipo
- Validar existencia y unicidad de cada integrante (sin duplicados)
- Guardar correctamente el equipo asignado en la estructura de la tarea

---

### ✅ Resultados logrados:

- El programa ahora **permite la asignación completa** de una tarea a un responsable y su equipo.
- Se utiliza correctamente el campo `equipo_nro` como limitador de integrantes.
- Se muestran mensajes claros en cada etapa.
- El flujo es estable, controlado y sin redundancias.

---

### 📘 Detalles técnicos importantes:

- Uso correcto de `while len(...) < cantidad` para controlar ingreso de equipo.
- Validación doble: existencia del ID + no repetición.
- El equipo se guarda como lista en el diccionario bajo la clave `'equipo'`.

---

### 🧠 Nivel alcanzado:

Este bloque demostró dominio sobre:
- Control de flujo sin `break`
- Validación encadenada
- Manejo de diccionarios anidados y listas
- Claridad en el diseño funcional

**Frase resumen:**
> “La estructura ya no es solo funcional: ahora es robusta, clara y extensible.”

---
