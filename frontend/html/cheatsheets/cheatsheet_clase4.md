# 📘 Clase 04 – Etiquetas HTML más comunes

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 04 – Etiquetas más comunes

---

## ✅ Objetivo de la clase

Conocer y comprender las etiquetas HTML más utilizadas en la estructura básica de una página web.  
Diferenciar entre etiquetas semánticas y no semánticas.  
Practicar la estructura correcta de una página web sencilla.

---

## 🧱 Estructura básica de una página

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Mi primera web</title>
  </head>
  <body>
    <h1>Hola mundo</h1>
    <p>Este es mi primer sitio</p>
  </body>
</html>
```

---

## 🏷️ Etiquetas de texto

| Etiqueta        | Significado                          |
| --------------- | ------------------------------------ |
| `<h1>` a `<h6>` | Encabezados (niveles jerárquicos)    |
| `<p>`           | Párrafo                              |
| `<br>`          | Salto de línea                       |
| `<strong>`      | Texto importante (negrita semántica) |
| `<em>`          | Énfasis (cursiva semántica)          |
| `<span>`        | Contenedor en línea genérico         |

---

## 🔗 Enlaces

```html
<a href="https://www.conquerblocks.com">Ir a Conquer Blocks</a>
```

- Atributo `href`: dirección del enlace
- Puede abrir páginas externas o internas

---

## 🖼️ Imágenes

```html
<img src="imagen.jpg" alt="Descripción de la imagen" />
```

- `src`: ruta de la imagen
- `alt`: texto alternativo (accesibilidad)

---

## 📋 Listas

### Lista ordenada

```html
<ol>
  <li>Primer ítem</li>
  <li>Segundo ítem</li>
</ol>
```

### Lista desordenada

```html
<ul>
  <li>Ítem uno</li>
  <li>Ítem dos</li>
</ul>
```

---

## 🧱 Estructura de contenido

| Etiqueta    | Uso principal                          |
| ----------- | -------------------------------------- |
| `<div>`     | Contenedor genérico en bloque          |
| `<span>`    | Contenedor genérico en línea           |
| `<section>` | Sección de contenido relacionada       |
| `<article>` | Contenido independiente y reutilizable |
| `<header>`  | Encabezado de una sección o página     |
| `<footer>`  | Pie de una sección o página            |
| `<main>`    | Contenido principal del documento      |
| `<nav>`     | Enlaces de navegación                  |
| `<aside>`   | Contenido complementario               |

---

## 🧠 Semántica vs no semántica

- **Semánticas**: transmiten significado (ej. `<article>`, `<header>`)
- **No semánticas**: solo agrupan (ej. `<div>`, `<span>`)

La semántica mejora la accesibilidad, SEO y mantenimiento.

---

## 🧠 Reflexión Clase 4

Esta clase me ayudó a conocer mejor la variedad de etiquetas disponibles para estructurar contenido.  
Entendí la diferencia entre etiquetas semánticas y no semánticas, y por qué es importante usarlas correctamente para mejorar la calidad del código.  
Siento que ya tengo las herramientas para escribir una página sencilla pero estructurada y clara.

---

📅 Fecha: 24/09/2025  
✍️ Autor: Hernán Geller
