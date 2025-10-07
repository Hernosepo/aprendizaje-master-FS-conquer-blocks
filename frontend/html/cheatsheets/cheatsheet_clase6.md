# 📘 Clase 06 – Estructura Semántica de una Página Web

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 06 – Etiquetas semánticas

---

## ✅ Resumen general

Esta clase introdujo el concepto de **etiquetas semánticas** en HTML5, que permiten estructurar de forma más comprensible y accesible el contenido de una página.  
En lugar de usar `<div>` genéricos, se utilizan etiquetas con un significado claro que ayudan al navegador, desarrolladores y tecnologías de asistencia a entender mejor el contenido.

---

## 🧠 Principales etiquetas semánticas

### `<header>`

Define la cabecera de una página o sección.  
Suele contener el logo, navegación, título principal o slogan.

### `<nav>`

Sección que agrupa enlaces de navegación.  
Indica explícitamente al navegador que esos enlaces permiten desplazarse por el sitio.

### `<main>`

Contenedor del contenido principal de la página.  
Debe haber **solo uno** por documento y **no debe** anidarse dentro de `<header>`, `<footer>`, `<article>` o `<aside>`.

### `<section>`

Representa una sección genérica del documento que agrupa contenido relacionado.  
Útil para dividir la página en bloques temáticos.

### `<article>`

Contenido independiente y autocontenible (como un post, noticia o entrada de blog).  
Puede tener su propio `<header>`, `<footer>`, y suele poder leerse por sí solo.

### `<aside>`

Contenido tangencial o complementario al principal, como barras laterales, widgets, banners o artículos relacionados.

### `<footer>`

Contiene el pie de una página o sección.  
Puede incluir info legal, copyright, navegación secundaria o datos de contacto.

---

## 🧠 Etiquetas adicionales relevantes

### `<address>`

Sirve para mostrar la información de contacto del autor o responsable del documento.  
Normalmente se muestra en el `<footer>`.

### `<time>`

Define fechas u horas, y puede incluir un atributo `datetime` para mejorar la lectura por parte de las máquinas.  
Ejemplo: `<time datetime="2025-09-27">27 de septiembre de 2025</time>`

### `<strong>`

Marca una parte del texto como **importante**.  
El navegador lo renderiza en negrita, pero además tiene **valor semántico**.

### `<em>`

Marca una parte del texto con **énfasis**.  
Se renderiza en cursiva y también tiene significado semántico.

---

## 💡 Beneficios del uso semántico

- Mejora la **accesibilidad**: lectores de pantalla entienden mejor la estructura.
- Facilita el **SEO**: los buscadores comprenden más claramente el contenido.
- Favorece el **mantenimiento** y **colaboración** en equipos de desarrollo.
- Permite separar claramente contenido principal y secundario.

---

## 🧠 Reflexión personal

El uso de etiquetas semánticas me ayuda a visualizar mejor la estructura de una web.  
En lugar de usar solo `<div>`, puedo representar la jerarquía real del contenido.  
Esto no solo mejora la legibilidad del código, sino también el posicionamiento y la accesibilidad.

---

📅 Fecha: 27/09/2025  
✍️ Autor: Hernán Geller
