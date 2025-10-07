# 📘 Clase 08 – Tablas en HTML

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 08 – Tablas en HTML

---

## ✅ Resumen general

En esta clase se explicó cómo funcionan las tablas en HTML, su estructura básica, sus principales etiquetas y atributos.  
Además, se mencionaron buenas prácticas y casos de uso comunes como su utilización en correos electrónicos HTML o en estructuras de información tabular.

---

## 📐 Estructura de una tabla en HTML

(backticks)html

<table>
  <thead>
    <tr>
      <th>Encabezado 1</th>
      <th>Encabezado 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dato 1</td>
      <td>Dato 2</td>
    </tr>
  </tbody>
</table>
(backticks)

---

## 🧠 Definiciones clave

- **`<table>`**: Contenedor principal de la tabla.
- **`<thead>`**: Sección para los encabezados de columna.
- **`<tbody>`**: Sección para los datos del cuerpo de la tabla.
- **`<tfoot>`**: Opcional. Contiene los totales o pies de página.
- **`<tr>`**: Table Row. Define una fila.
- **`<th>`**: Table Header. Define una celda de encabezado (por defecto en negrita y centrado).
- **`<td>`**: Table Data. Define una celda de datos.

---

## 🔧 Atributos útiles

- **`colspan`**: Permite que una celda ocupe varias columnas.
- **`rowspan`**: Permite que una celda ocupe varias filas.
- **`border`** (obsoleto): Define el borde de la tabla (se recomienda usar CSS).
- **`align`**, **`valign`**: Alineación horizontal y vertical (también se recomienda usar CSS).

---

## 📫 Tablas en emails HTML

- **Motivo**: Se utilizan porque los clientes de correo no soportan bien CSS moderno.
- **Solución alternativa moderna**:
  - [MJML](https://mjml.io/): Framework que simplifica la creación de emails responsive usando una sintaxis declarativa.

---

## 🧠 Comparación rápida

| Elemento  | Significado                  |
| --------- | ---------------------------- |
| `<th>`    | Celda de encabezado (header) |
| `<td>`    | Celda de datos (data)        |
| `<tr>`    | Fila completa (row)          |
| `<thead>` | Cabecera de la tabla         |
| `<tbody>` | Cuerpo principal             |
| `<tfoot>` | Pie de tabla (opcional)      |

---

## 💡 Buenas prácticas

- Usar etiquetas semánticas (`<thead>`, `<tbody>`, `<tfoot>`) para mejorar accesibilidad y legibilidad.
- Evitar estilos inline como `border`, `align`, `bgcolor`, etc.
- Utilizar CSS externo para separar estructura y estilo.
- Minimizar el uso de tablas para maquetación (excepto en emails donde es necesario).

---

## 📎 Recursos útiles

- [HTML Tables – W3Schools](https://www.w3schools.com/html/html_tables.asp)
- [HTML Emails – Hubspot Blog](https://blog.hubspot.com/website/html-email-table)
- [MJML – Responsive Email Framework](https://mjml.io/)

---

## 🧠 Reflexión personal

Aunque las tablas no son tan comunes en maquetación moderna, esta clase me ayudó a comprender cómo estructurar datos tabulados de forma ordenada.  
También entendí por qué se siguen usando en emails y cómo frameworks como MJML permiten solucionar esa limitación.

---

📅 Fecha: 29/09/2025  
✍️ Autor: Hernán Geller
