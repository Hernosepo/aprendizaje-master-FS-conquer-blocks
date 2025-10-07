# 📘 INFORME COMPLETO – Desarrollo del ejercicio "Administración de Proyectos"

**Tema 6 – Diccionarios | Conquer Blocks – Python Avanzado**

---

## 📅 Jornada de trabajo – Resumen general

Durante esta jornada de 12 horas trabajé intensamente sobre las funciones, especialmente `asignar_tarea()` que fue la que mas me costo, dentro del ejercicio "Administrador de Proyectos", correspondiente al Tema 6 del máster. Avancé en cada una de las etapas con razonamiento profundo, control del flujo, validaciones, lógica encadenada y análisis conceptual detallado.

---

## 🧠 Conceptos técnicos aplicados

- **Diccionarios anidados**: uso de estructuras tipo `{clave: {subclave: valor}}`
- **Validación de claves**: evitar accesos inválidos o no existentes dentro de los diccionarios
- **Banderas booleanas**: uso de `tarea_valida`, `encargado_valido`, etc. para evitar `break`
- **Control de flujo sin interrupciones abruptas**: sin `break`, con evaluación posbucle
- **Comparación por identidad de claves** (strings), diferenciando clave de valor
- **Uso de `while len(...) < valor`** para controlar cantidad de personas seleccionadas

---

## 🔍 Observaciones y correcciones importantes

### Errores comunes identificados y corregidos:

- ❌ Comparar un string del usuario contra el **subdiccionario completo** de una tarea.
- ❌ Ubicación incorrecta de `return` y `else` dentro del `for`, que cortaban el flujo o mostraban mensajes en cada vuelta.
- ❌ Suposición de que el `if` detendría el bucle automáticamente tras cumplirse.
- ❌ Mezcla de responsabilidades lógicas sin cerrar correctamente bloques condicionales.

---

### Correcciones clave:

- ✔️ Reemplazo de `return` por **banderas booleanas** para mantener el control sin cortar.
- ✔️ Separación clara de bloques con sus propias validaciones.
- ✔️ Implementación de un control de equipo que permite asignar múltiples personas sin duplicaciones.
- ✔️ Inclusión de `equipo_nro` como parámetro para determinar cantidad esperada.

---

## 💡 Percepciones sobre el desempeño del desarrollador

### Fortalezas:

- 🌟 **Razonamiento progresivo**: cada error dio lugar a un aprendizaje nuevo, sin atajos.
- 🌟 **Perseverancia frente a la frustración lógica** (“el agua se escapa”) hasta entender la estructura.
- 🌟 **Alta conciencia estructural**: no solo se buscó hacer funcionar el código, sino entender cómo.
- 🌟 **Explicación de pensamiento en voz alta**: uso de comentarios para validar hipótesis.
- 🌟 **Consulta inteligente**: no se pidieron soluciones, sino herramientas para pensar mejor.

---

### Frases que resumen la jornada:

> “Me cuesta seguir el flujo, como que se me escapa el agua.”  
> → Resultado: comprensión profunda de `for`, `if`, `else`, banderas y flujo sin `break`.

> “En mi cabeza, esto debería bloquear todo después del if...”  
> → Resultado: entendimiento real de cuándo se ejecutan los bloques y cómo detener comportamientos repetidos.

> “No lo puedo creer.”  
> → Resultado: cierre emocional de un proceso técnico y cognitivo desafiante.

---

## 📦 Resultado funcional

Al final de la jornada, el programa:

- Permite ingresar tareas con campos completos (`descripcion`, `responsable`, `equipo_nro`)
- Permite agregar personas con ID único
- Asigna responsables a tareas seleccionadas
- Asigna equipos completos de forma validada, sin duplicaciones
- Guarda correctamente toda la estructura dentro del diccionario principal
- Muestra mensajes precisos y ordenados según el flujo

---

## 🔁 Recomendaciones para continuidad

- Validar campos vacíos y errores de tipeo con más robustez (input sanitization)
- Considerar persistencia de datos (archivo `.json` o `.txt`)
- Mostrar resumen total de tareas asignadas al cerrar
- Crear función para volver atrás en el menú

---

## 🧾 Cierre

Este documento resume no solo el avance técnico, sino la consolidación de herramientas lógicas, de programación estructurada y de pensamiento computacional. El ejercicio pasó de ser una estructura básica a un proyecto funcional, robusto y flexible.
