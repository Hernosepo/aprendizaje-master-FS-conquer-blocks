# 📘 Clase 10 – Formularios HTML (Parte 1)

Curso: Máster en Desarrollo Full Stack – Conquer Blocks  
Tema: HTML  
Clase: 10 – Introducción a Formularios

---

## ✅ ¿Qué es un formulario?

Un formulario HTML es un bloque de contenido que contiene campos para que el usuario introduzca datos que luego pueden ser enviados a un servidor.  
Es uno de los mecanismos más comunes para recolectar datos en la web.

---

## 🎯 Objetivos de los formularios

- Facilitar la entrada de datos del usuario
- Mejorar la experiencia del usuario
- Validar y estructurar correctamente los datos enviados
- Detectar y notificar errores de manera clara
- Enviar datos en formatos predecibles

---

## 🧱 Estructura básica del formulario

(etiqueta) (form)

- Elemento de bloque
- Acepta atributos como (method), (action), (enctype)
- Puede contener múltiples tipos de campos (inputs, botones, selects)

(backticks)html  
(form action="/ruta-de-envio" method="POST")

  <!-- Inputs y otros elementos -->

(/form)  
(backticks)

---

## ✉️ Métodos de envío

### GET

- Envía datos en la URL como parámetros (?nombre=valor&...)
- Límite de tamaño (~500 bytes)
- No permite adjuntar archivos
- Visibles en la barra del navegador
- Útil para búsquedas o filtros

Ejemplo de URL:  
https://www.ejemplo.com/registro?nombre=Juan&edad=30

### POST

- Envía los datos de forma oculta en el cuerpo de la petición
- Permite enviar muchos datos
- Soporta archivos adjuntos (multipart/form-data)
- Se usa para operaciones de tipo CRUD: Create, Update, Delete

---

## 🌐 ¿Qué es una URL?

Formato de acceso a recursos en la web.  
Incluye: protocolo + dominio + puerto (opcional) + ruta + parámetros.

Ejemplo:  
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2

---

## 🔤 Etiqueta (input)

Campo de entrada que permite al usuario ingresar datos.

### Atributos importantes:

- (type): define el tipo de dato (text, number, email, etc.)
- (name): nombre del campo (clave para el backend)
- (value): valor predefinido del input
- (placeholder): texto guía dentro del campo vacío

### Tipos comunes de input:

| Tipo     | Descripción                                  |
| -------- | -------------------------------------------- |
| text     | Campo de texto                               |
| number   | Solo acepta números                          |
| email    | Valida formato de correo electrónico         |
| password | Texto oculto                                 |
| url      | Valida una dirección web                     |
| date     | Selector de fecha                            |
| range    | Selector tipo slider (rango de valores)      |
| file     | Para subir archivos                          |
| checkbox | Casilla de verificación                      |
| radio    | Opción de selección única dentro de un grupo |
| hidden   | Campo oculto con datos invisibles            |
| submit   | Botón para enviar el formulario              |
| reset    | Botón para limpiar todos los campos          |
| button   | Botón genérico                               |

---

## 📌 Importancia de (name) y (value)

- El (name) es la clave que el backend usa para identificar los datos enviados.
- El (value) es lo que el usuario ingresó o el valor predefinido del campo.

Ejemplo:  
(backticks)html  
(input type="text" name="usuario" value="hernan")  
(backticks)

---

## 🧠 Reflexión

Esta clase sienta las bases para la interacción real con el usuario en la web.  
Aprendí que los formularios no solo son visuales, sino que están pensados para facilitar el envío de datos estructurados, y que la elección de GET o POST tiene implicaciones prácticas y de seguridad.

---

📅 Fecha: 29/09/2025  
✍️ Autor: Hernán Geller
