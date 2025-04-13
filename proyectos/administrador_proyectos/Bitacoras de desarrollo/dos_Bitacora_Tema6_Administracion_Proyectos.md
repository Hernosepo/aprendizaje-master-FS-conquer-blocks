# 🗂 Bitácora Técnica – Tema 6: Diccionarios


---

## ✅ Hito técnico alcanzado – Manejo correcto del flujo y persistencia de datos

**Situación resuelta:**
- El programa dejaba de arrancar desde el menú y comenzaba automáticamente con la función `agregar_persona()`.

**Causa detectada:**
- El contador `contador` se pasaba como argumento, pero como es un tipo inmutable (entero), los cambios dentro de la función no persistían a menos que se actualizara correctamente fuera de ella.

**Solución implementada:**
- Se corrigió el control del contador para que se incremente **fuera de la función**, garantizando que el ID de cada persona sea único y progresivo.
- Se aseguró que **la única función que se ejecuta automáticamente** sea el `while True` con `mostrar_menu()`, manteniendo el control de navegación.

**Resultado:**
- El programa ahora permite:
  - Agregar personas y tareas alternadamente sin sobrescribir datos.
  - Volver siempre al menú principal tras completar una acción.
  - Gestionar correctamente el ID incremental para cada persona agregada.

🧠 Este fue un punto clave para garantizar la **persistencia de datos**, el **control del flujo principal** y la **estabilidad del sistema**.

