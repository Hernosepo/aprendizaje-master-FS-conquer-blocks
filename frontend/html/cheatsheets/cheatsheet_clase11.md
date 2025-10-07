# 📘 Clase 11 – Formularios II

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend – HTML  
Clase: 11 – Formularios Parte 2

---

## ✅ Contenido principal

- Inputs adicionales
- Checkbox y radio
- Accesibilidad con `label`
- `textarea`
- `select`
- Botones (`button` vs `submit`)
- `fieldset` y `legend`
- Validación y obligatoriedad (modificadores)
- Chuleta final

---

## 🧠 Definiciones y conceptos

### 📥 Nuevos tipos de input

- `checkbox`: selección múltiple (ej: ingredientes de pizza)
- `radio`: selección única dentro de un grupo (ej: color de zapatillas)
- `color`, `date`, `datetime-local`, `month`, `week`, `time`: selección de fechas y colores
- `image`: botón de tipo imagen
- `search`: campo de búsqueda
- `range`: selección por deslizador (slider)
- `tel`: campo para números de teléfono
- `reset`: botón para reiniciar el formulario

> La clave en todos estos inputs es usar correctamente `name` y `value` para que el envío de datos sea consistente.

---

### 🔏 Accesibilidad – `label`

- El uso del atributo `for` enlaza el `label` con su input correspondiente.
- Mejora la accesibilidad: permite hacer clic en el texto para activar el input.
- Puede usarse:
  - Envolviendo al input
  - Usando el atributo `for`
  - En un contenedor común

> Diferencias con `placeholder`: este desaparece al escribir y no es accesible por lectores de pantalla.

---

### 📝 `textarea`

- Se usa para textos largos
- Atributos: `cols`, `rows` para controlar tamaño
- Puede colocarse un texto por defecto entre las etiquetas

---

### 🔽 `select`

- Lista desplegable de opciones
- Atributos:
  - `multiple`: permite elegir más de una opción
  - `required`: obligatorio
  - `size`: cuántas opciones visibles sin desplegar

---

### 🔘 `button` vs `submit`

- Ambos sirven para enviar formularios.
- `submit`: envía el formulario automáticamente.
- `button`: más flexible, se suele usar con JavaScript.

---

### 🧩 `fieldset` y `legend`

- `fieldset`: agrupa elementos del formulario
- `legend`: título semántico para ese grupo
- Mejora visual y estructuralmente la organización del formulario

---

### 🛡️ Modificadores de validación y obligatoriedad

- `required`: campo obligatorio
- `minlength` y `maxlength`: longitud mínima y máxima
- `min` y `max`: valores numéricos
- `type`: valida formato (ej: `email`, `url`)
- `pattern`: validación con expresión regular

> ⚠️ ¡Nunca confíes solo en el front! Validá también en el backend.

---

## 🧠 Conclusión

Esta clase amplía el abanico de elementos disponibles para crear formularios más completos, accesibles y funcionales. Se incorporan prácticas de validación y agrupamiento que hacen más robusto y semántico el diseño.

---

📅 Fecha: 29/09/2025  
✍️ Autor: Hernán Geller
