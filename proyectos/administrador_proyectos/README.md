# 🗂 Administrador de Proyectos

Este proyecto fue desarrollado como parte del Máster Full Stack en Conquer Blocks, dentro del Tema 6: Diccionarios en Python.  
Su objetivo es gestionar tareas y personas, asignando responsables y equipos de trabajo mediante estructuras dinámicas y control de flujo validado.

---

## 🚀 Funcionalidades principales

- ✅ Agregar tareas con nombre, descripción y cantidad de integrantes requeridos
- ✅ Agregar personas con nombre y apellido, generando un ID incremental único
- ✅ Asignar un responsable por tarea desde la lista de personas disponibles
- ✅ Seleccionar un equipo de trabajo para cada tarea según lo requerido
- ✅ Validaciones múltiples: existencia de tareas, existencia de IDs, no duplicación
- ✅ Flujo de navegación controlado, sin uso de `break`, mediante banderas booleanas

---

## 📦 Estructura de datos

Las tareas y personas se gestionan a través de dos diccionarios principales:

```python
almacenador_tareas = {
    'tarea1': {
        'descripcion': '...',
        'responsable': '...',
        'equipo_nro': 3,
        'equipo': ['P2', 'P3', 'P5']
    },
    ...
}

personal_agregado = {
    'P1': {'nombre': 'Juan', 'apellido': 'Perez'},
    ...
}
```

---

## 🧠 Aprendizajes consolidados

- Diccionarios anidados y gestión de múltiples niveles de acceso
- Uso de banderas booleanas para validación y control sin `break`
- Flujo completo con estructuras `while`, `for`, `if`, `else` y `continue`
- Comparación efectiva de claves vs. valores
- Organización modular del código por funciones específicas
- Registro de errores conceptuales y solución basada en análisis del flujo

---

## 📘 Documentación adicional

- 📄 [Bitácora de desarrollo](./Bitacora_Tema6_Administracion_Proyectos.md)
- 📄 [Informe técnico completo](./Informe_Admin_Proyectos_Tema6.md)

---

## 👨‍💻 Autor

**Hernán Geller**  
[GitHub: @Hernosepo](https://github.com/Hernosepo)

---

## 🎯 Comentario final

Este proyecto representa un hito técnico y personal dentro de mi proceso de formación.  
Con trabajo, esfuerzo y tratando de entender el control del flujo de la información, este ejercicio se transformó en una pieza sólida del trabajo que quiero realizar algun día de manera profesional.  
Más que un script, es una muestra real de evolución en lógica, práctica y pensamiento programático.
