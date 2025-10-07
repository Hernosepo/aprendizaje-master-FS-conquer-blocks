# 📘 Clase 03 – Estructura básica de una página web

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 03 – Estructura básica de una web

---

## ✅ Resumen general

En esta clase se explicó cómo se estructura un documento HTML desde cero, sus partes fundamentales y cómo interactúa con el navegador.  
También se introdujeron otras estructuras de datos como XML y JSON para entender qué es un lenguaje de marcado y cómo se diferencia del formato de datos.

---

## 🧱 Estructura básica de un documento HTML

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Título de la página</title>
  </head>
  <body>
    <!-- Contenido visible para el usuario -->
  </body>
</html>
```

---

## 🧠 Definiciones clave

### `<!DOCTYPE html>`

Indica que el documento está escrito en HTML5.  
Permite al navegador renderizar en modo estándar.

### `<html>`

Elemento raíz del documento.  
Todo el contenido HTML debe estar dentro de esta etiqueta.

### `<head>`

Contiene metadatos:

- Codificación (`<meta>`)
- Título (`<title>`)
- Archivos externos (`<link>`, `<script>`)  
  No es visible para el usuario.

### `<meta charset="UTF-8">`

Define la codificación de caracteres.  
UTF-8 permite escribir ñ, tildes, emojis, etc.

### `<title>`

Título de la página (aparece en la pestaña del navegador).  
También lo usa Google como título en los resultados de búsqueda.

### `<body>`

Sección visible para el usuario.  
Contiene encabezados, párrafos, imágenes, botones, formularios, etc.

---

## ⚙️ Flujo de carga real en el navegador

1. Interpreta `<!DOCTYPE html>` para activar el modo estándar.
2. Lee el documento HTML desde arriba hacia abajo.
3. Procesa el `<head>`:
   - Aplica estilos (`<link rel="stylesheet">`)
   - Descarga scripts (`<script>`) — puede bloquear el renderizado.
4. Renderiza el `<body>` progresivamente.
5. Ejecuta los scripts al final si están abajo o marcados con `defer` o `async`.

---

## 📦 Comparación: HTML vs XML vs JSON

### HTML

```html
<p>Hola mundo</p>
```

- Lenguaje de marcado con etiquetas predefinidas.
- Se usa para mostrar contenido en el navegador.

### XML

```xml
<mensaje>
  <texto>Hola mundo</texto>
</mensaje>
```

- Lenguaje de marcado estructurado y extensible.
- Se usa para transportar datos entre sistemas.
- Etiquetas definidas por el desarrollador.

### JSON

```json
{
  "mensaje": {
    "texto": "Hola mundo"
  }
}
```

- Formato ligero y moderno para transferencia de datos.
- Más legible para las máquinas.
- Muy común en APIs.

---

### 🧠 Conclusión rápida

| Formato | Uso principal                   | Legible para humanos | Legible para máquinas |
| ------- | ------------------------------- | -------------------- | --------------------- |
| HTML    | Visualización web               | ✅                   | Parcial               |
| XML     | Transferencia de datos (legado) | ✅                   | ✅                    |
| JSON    | Transferencia de datos (actual) | ✅                   | ✅                    |

---

## 💡 Buenas prácticas

- Siempre comenzar con `<!DOCTYPE html>`.
- Usar `UTF-8` para evitar errores de codificación.
- Mantener una estructura ordenada y comentada.
- Separar contenido (HTML), estilo (CSS) y comportamiento (JS).
- Indentar correctamente para facilitar la lectura.

---

## 🧠 Reflexión personal

Esta clase me dio claridad sobre cómo está estructurado un archivo HTML y cuál es su diferencia con otros formatos como XML o JSON.  
Me resulta motivador ver que puedo empezar a escribir mis primeras páginas desde cero y entender cómo piensa el navegador.  
También entendí por qué algunas prácticas como el orden del `<script>` afectan directamente la carga de la web.

---

📅 Fecha: 24/09/2025  
✍️ Autor: Hernán Geller
