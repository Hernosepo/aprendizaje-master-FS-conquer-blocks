
# 🧪 Pruebas adicionales – Sprint 3

Durante el testeo del método `agregar_caminos_falsos`, se observaron varios comportamientos esperados y otros que requieren seguimiento.

---

## ✅ Ejemplos de caminos válidos donde el marcador `4` se muestra correctamente:

### Ejemplo 1 – Camino vertical con desvío lateral
```python
laberinto = Laberinto(6, 6, (0, 1), (5, 1))
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (2, 1), falsa_salida = (2, 3))
```

### Ejemplo 2 – Camino diagonal con desvío lateral bajo
```python
laberinto = Laberinto(6, 6, (0, 0), (5, 5))
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (4, 2), falsa_salida = (4, 4))
```

### Ejemplo 3 – Camino en L con desvío desde fila inferior
```python
laberinto = Laberinto(6, 6, (1, 0), (4, 4))
laberinto.generar_ruta()
laberinto.agregar_caminos_falsos(falso_inicio = (5, 3), falsa_salida = (5, 4))
```

---

## ⚠️ Estado actual

- Algunos caminos falsos no finalizan en `4` debido a la validación de celdas vecinas en el condicional.
- El `if` actual impide marcar `4` si la celda `falsa_salida` tiene vecinos `0`, incluso si fueron parte del mismo camino falso.
- En algunos casos, la celda `falsa_salida` es modificada dentro del bucle, por lo tanto no se cumple `self.matriz[falsa_salida] == 1`.

---

## 🔧 Próximos pasos

- Refinar la validación para que considere solo `0`s externos, no del propio camino falso.
- Implementar una forma de guardar las coordenadas del camino falso durante el trazado.
- Considerar tolerancia o flags para permitir que ciertos vecinos sean `0` sin invalidar la escritura del `4`.

---

📌 Nota: Este punto se mantiene **en fase de depuración** y será revisado en el Sprint 3.5 o 4.
