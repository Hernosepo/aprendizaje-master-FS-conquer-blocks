# 📘 Clase 05 – Texto en HTML

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 05 – Texto en HTML

---

## ✅ Resumen general

Esta clase presenta las principales etiquetas para trabajar con texto en HTML. Se revisan títulos, párrafos, enlaces, citas, espacios en blanco, énfasis semántico y entidades.  
También se destaca la importancia de usar etiquetas con significado (semántica) en lugar de solo visuales.

---

## 🧠 Elementos de texto

### Títulos

- `<h1>` a `<h6>`: Jerarquía de encabezados (siendo `<h1>` el más importante).

```html
<h1>Título principal</h1>
<h2>Subtítulo</h2>
```

### Párrafos

- `<p>`: Define un párrafo de texto.

```html
<p>Este es un párrafo.</p>
```

### Línea horizontal

- `<hr>`: Inserta una línea divisoria horizontal. No tiene etiqueta de cierre.

---

## ✍️ Énfasis y semántica

- `<strong>`: Resalta texto con importancia (semántica + visual).
- `<em>`: Da énfasis (cursiva) con valor semántico.
- `<b>` y `<i>`: Solo efectos visuales (negrita/cursiva), sin semántica.

```html
<p><strong>Importante</strong> y <em>con énfasis</em></p>
```

---

## 🔗 Enlaces

- `<a href="URL">Texto</a>`: Crea un enlace.
- Atributos importantes:
  - `target="_blank"`: Abre en nueva pestaña.
  - `rel="noopener noreferrer"`: Seguridad y performance.

```html
<a href="https://conquerblocks.com" target="_blank" rel="noopener noreferrer">Conquer Blocks</a>
```

---

## 🧾 Citas

- `<blockquote>`: Cita en bloque.
- `<cite>`: Fuente o autor de una obra.
- `<q>`: Cita corta (entre comillas).

```html
<blockquote cite="https://ejemplo.com">
  Esto es una cita larga.
</blockquote>
<cite>— Hernán Geller</cite>
```

---

## 🧬 Código y abreviaturas

- `<code>`: Muestra código en línea.
- `<abbr title="Hypertext Markup Language">HTML</abbr>`: Abreviatura con significado.

```html
<p>Ejemplo de código: <code>console.log("Hola")</code></p>
```

---

## 🔡 Espacios en blanco y saltos de línea

- `&nbsp;`: Espacio no separable.
- `<br>`: Salto de línea.
- `<wbr>`: Sugerencia de corte de palabra.
- `<pre>`: Conserva saltos de línea y espacios del texto original.

```html
<p>Hola&nbsp;&nbsp;&nbsp;mundo</p>
<pre>
  Línea 1
  Línea 2
</pre>
```

---

## 📦 Entidades HTML

- Sirven para representar caracteres especiales.

| Entidad | Resultado | Descripción       |
|---------|-----------|-------------------|
| `&nbsp;` |           | Espacio no separable |
| `&lt;`   | <         | Menor que         |
| `&gt;`   | >         | Mayor que         |
| `&amp;`  | &         | Ampersand         |

---

## 💡 Buenas prácticas

- Usar etiquetas semánticas (`<strong>`, `<em>`) en lugar de visuales (`<b>`, `<i>`).
- Evitar abusar de `<br>` para separar contenido.
- Usar `&nbsp;` para separar palabras que no deben dividirse.
- Agregar `rel="noopener noreferrer"` cuando uses `target="_blank"`.

---

## 🧠 Reflexión personal

Esta clase me ayudó a entender la diferencia entre estilos visuales y significado semántico.  
El HTML no solo se trata de "cómo se ve", sino de estructurar el contenido con sentido para que navegadores, buscadores y lectores de pantalla lo interpreten correctamente.

---

📅 Fecha: 24/09/2025  
✍️ Autor: Hernán Geller
