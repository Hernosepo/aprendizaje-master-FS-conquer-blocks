# 📘 Clase 09 – Tablas en HTML

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 09 – Tablas en HTML

---

## ✅ Resumen general

En esta clase se abordó el uso de **tablas en HTML** para representar información organizada en filas y columnas.  
Se cubrieron las principales etiquetas, atributos como `colspan` y `rowspan`, y se introdujeron buenas prácticas para el uso semántico y accesible de tablas.

---

## 🧱 Estructura básica de una tabla

(backticks)html

<table>
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Edad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Juan</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Laura</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
(backticks)

---

## 🧠 Etiquetas importantes

### `<table>`

Etiqueta contenedora principal de una tabla.

### `<tr>` (table row)

Define una fila dentro de la tabla. Puede contener celdas de encabezado (`<th>`) o de datos (`<td>`).

### `<th>` (table header)

Define una celda de encabezado. Aparece en negrita y centrado por defecto.  
Se recomienda agregar el atributo `scope` para indicar si es encabezado de columna (`scope="col"`) o de fila (`scope="row"`).

(backticks)html

<th scope="col">Nombre</th>
(backticks)

### `<td>` (table data)

Define una celda de datos estándar dentro de una fila.

### `<thead>`

Agrupa los encabezados de la tabla.  
Mejora la organización semántica y es útil para accesibilidad.

### `<tbody>`

Agrupa el cuerpo principal de la tabla (las filas con datos).  
Facilita el procesamiento por parte de scripts o estilos.

### `<tfoot>`

(opcional) Agrupa el pie de tabla, como totales o resúmenes.

---

## 🧩 Atributos útiles

### `colspan`

Permite que una celda ocupe varias columnas:

(backticks)html

<td colspan="2">Nombre completo</td>
(backticks)

### `rowspan`

Permite que una celda ocupe varias filas:

(backticks)html

<td rowspan="2">Ventas acumuladas</td>
(backticks)

---

## 🧼 Buenas prácticas

- Usar `<thead>`, `<tbody>` y `<tfoot>` para separar las secciones de la tabla.
- Emplear `<th>` para encabezados con sus `scope` correspondientes.
- No usar tablas para maquetación visual. Solo para datos tabulados.
- Asegurarse de que la tabla tenga sentido al ser leída de arriba a abajo y de izquierda a derecha.
- Usar CSS para dar estilo en lugar de atributos obsoletos como `border`, `bgcolor`, etc.

---

## 🧠 Reflexión personal

Esta clase me ayudó a entender cómo estructurar correctamente una tabla HTML y cómo usar atributos como `colspan` o `rowspan` para lograr diseños más complejos.  
También me queda más claro el propósito semántico de `<thead>`, `<tbody>` y el valor de un HTML accesible.

---

📅 Fecha: 29/09/2025  
✍️ Autor: Hernán Geller
