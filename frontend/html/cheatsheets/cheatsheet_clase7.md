# 📘 Clase 07 – Listas, viñetas y numeraciones

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: Frontend  
Módulo: HTML  
Clase: 07 – Listas, viñetas y numeraciones

---

## ✅ Resumen general

En esta clase se explicaron los tres tipos principales de listas en HTML:

- Listas desordenadas (`<ul>`)
- Listas ordenadas (`<ol>`)
- Listas de definición (`<dl>`, `<dt>`, `<dd>`)

También se mostraron sus principales atributos y cómo se representan visualmente en el navegador.

---

## 🧾 Tipos de listas en HTML

### 🔹 Lista desordenada (`<ul>`)

- Representa una lista de elementos sin un orden específico.
- Se muestran con viñetas.

```html
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ul>
```

### 🔸 Lista ordenada (`<ol>`)

- Representa una lista con orden (numérico, alfabético, romano).
- Usa el atributo `type` para cambiar el estilo del numerado.

```html
<ol type="1">
  <li>Primer paso</li>
  <li>Segundo paso</li>
</ol>
```

Atributos comunes para `<ol type="">`:

| Valor | Descripción            |
| ----- | ---------------------- |
| `1`   | Números (1, 2, 3)      |
| `a`   | Letras minúsculas      |
| `A`   | Letras mayúsculas      |
| `i`   | Números romanos (min.) |
| `I`   | Números romanos (may.) |

También se puede usar `start="3"` para comenzar desde otro número.

### 📘 Lista de definición (`<dl>`, `<dt>`, `<dd>`)

- Se usa para definir términos y sus descripciones.

```html
<dl>
  <dt>HTML</dt>
  <dd>Lenguaje de marcado para estructurar contenido web.</dd>
</dl>
```

---

## 💡 Buenas prácticas

- Usar listas para estructurar mejor el contenido.
- Elegir el tipo de lista según el objetivo:
  - `ul` para ítems sin orden.
  - `ol` para pasos, rankings, etc.
  - `dl` para glosarios o definiciones.
- No abusar de estilos visuales que rompan la semántica.

---

## 🧠 Reflexión personal

Esta clase me ayudó a entender cuándo conviene usar cada tipo de lista.  
Pude ver claramente cómo cambia el significado del contenido según se utilice una lista ordenada o desordenada.  
También me pareció interesante conocer el uso de listas de definición, algo menos habitual pero muy útil para glosarios o fichas técnicas.

---

📅 Fecha: 29/09/2025  
✍️ Autor: Hernán Geller
