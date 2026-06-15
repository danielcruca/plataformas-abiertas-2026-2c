# 📘 Introducción a Python y Programación Orientada a Objetos (POO)

## 🐍 ¿Qué es Python?

Python es un lenguaje de programación interpretado, de alto nivel y muy fácil de leer y escribir. Se utiliza ampliamente en desarrollo web, análisis de datos, automatización, inteligencia artificial y más.

### ✅ Características principales:

- Sintaxis sencilla
- Código legible y limpio
- Gran comunidad y muchas librerías disponibles
- Multiparadigma: soporta programación estructurada, orientada a objetos y funcional

---

## 📌 Sintaxis básica de Python

```python
# Esto es un comentario

# Variables
nombre = "Juan"
edad = 25

# Condicional
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Bucle
for i in range(5):
    print(i)
```

---

## 🧱 Introducción a Programación Orientada a Objetos (POO)

La programación orientada a objetos organiza el código en clases y objetos.

### ✨ Ejemplo básico:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto
persona1 = Persona("Ana", 30)
persona1.saludar()
```

---

## 📦 ¿Cómo importar desde otro archivo `.py`?

Supongamos que tienes la siguiente estructura:

```
mi_proyecto/
│
├── persona
│   ├── __init__.py
│   ├── persona.py
└── main.py
```

### `persona/persona.py`
```python
class Persona:
   #Usando constructor
   # def __init__(self, nombre):
   #     self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")
```

### `main.py`
```python
from persona.persona import Persona

p = Persona()
#p = Persona("Carlos") # si usamos el constructor
p.nombre = "Genghis Khan"
p.saludar()
```
### Ejecutar
Ejecutar el archivo con el siguiente comando `python main.py`

> ✅ Este seguro de que ambos archivos estén en la misma carpeta o configurar correctamente los módulos.

---

## 🎓 Recomendaciones

- Utilizar nombres descriptivos para las clases, funciones y variables.
- Usar plugins in vscode para mejorar la experiencia de desarrollo.
- Utilizar comentarios claros y explicativos.


## Ejemplos 

Vaya al folder ejemplos.

