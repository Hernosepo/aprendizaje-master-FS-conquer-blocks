
# 🗂 Bitácora Técnica – Tema 6: Diccionarios  
### Ejercicio: Administración de Proyectos

---

## 🧠 Aprendizajes clave

- El input del usuario es solo el **punto de entrada**, pero las operaciones deben pensarse a partir de la **estructura del diccionario**.
- En Python, los strings vacíos (`""`) son considerados `False` en contexto booleano. Por eso, usar `if nombre:` es más natural y efectivo que `if nombre != False`.
- El uso de `return` dentro de un `for` permite **salir temprano** si se encuentra una coincidencia.
- La ubicación del `print()` y del `return` **define el flujo** de la función. Ponerlos dentro del bucle o fuera cambia completamente el comportamiento.
- "Mirar para arriba" significa **no operar sobre el input directamente**, sino usar el input para recorrer y acceder a la estructura mayor (diccionario principal).

---

## 🧩 Lógicas implementadas

- Diccionario principal `almacenador_tareas` con claves que representan tareas y subdiccionarios con `descripcion` y `responsable`.
- Función `mostrar_menu()` simple, que devuelve la opción del usuario.
- Bucle principal con `while True` y control de opciones con `if`.
- Función `agregar_tarea()` que:
  - Solicita input de nombre.
  - Verifica si ya existe.
  - Agrega nueva tarea con valores por defecto si no existe.

---

## 🧪 Errores detectados y corregidos

- ❌ Uso de `if nombre_tarea != False` para validar input.  
  ✅ Reemplazado por `if nombre_tarea`, que es más pythonic y correcto.

- ❌ Lógica dentro del `for` que ejecutaba la creación de tarea en cada iteración no coincidente.  
  ✅ Corregido usando `return` para salir al detectar existencia y colocando la creación **fuera del bucle**.

---

## ⚙️ Lógicas que no funcionaron al principio

- Comparación de claves directamente con el string de input sin controlar el flujo.
- Intento de validar con bandera sin actualizarla (`bandera_tarea = True` pero sin uso real).
- Confusión inicial entre clave del diccionario y el valor interno del subdiccionario.

---

## 📘 Conceptos técnicos reforzados

- Diccionarios anidados
- Estructuras de control `if`, `for`, `while`
- `input()` y validación booleana en Python
- Reutilización de funciones con paso de diccionario como parámetro
- Uso de `return` como mecanismo de control de flujo

---

## 🔁 Reflexión sobre el proceso

> “Tomé el camino de comparar contra `False` porque una pista mencionaba una bandera booleana. No fue incorrecto, pero después entendí que había una forma más directa y nativa en Python de hacer la validación. Eso me ayudó a afinar mi lectura de pistas y mejorar mi intuición con el lenguaje.”

---

## 🔄 Próximos pasos

- Implementar `agregar_persona()`, cuidando el flujo de validación.
- Avanzar luego con `asignar_tarea()`.
- Mantener esta bitácora como documento vivo.

