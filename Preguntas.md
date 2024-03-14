# • ¿Qué es un condicional?

Un condicional es una estructura de control que permite ejecutar cierto bloque de código basado en una condición booleana. 
Permite que un programa tome decisiones y realice diferentes acciones según el resultado de una evaluación lógica.

## Beneficios de los condicionales:

- Permiten que los programas tomen decisiones basadas en condiciones lógicas.
  
- Facilitan la implementación de lógica condicional en el código.

### Sintaxis:

```python

if condicion:
    # Bloque de código a ejecutar si la condición es verdadera
else:
    # Bloque de código a ejecutar si la condición es falsa

``` 

#### Ejemplo:

```python

edad = 18

if edad >= 18:
    print("Tienes acceso")
else:
    print("Acceso denegado")

```

# • ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En Python, hay principalmente dos tipos de bucles: el bucle 'for' y el bucle 'while':
	
• Bucle 'for': Se utiliza para iterar sobre una secuencia o cualquier otro objeto iterable, ejecutando un bloque de código una vez para cada elemento de la secuencia.

## Sintaxis:

```python

for elemento in secuencia:
    # Bloque de código a ejecutar

```

### Ejemplo

```python

colores = ["azul", "amarillo", "rojo"]

for color in colores:
    print(color)

```

• Bucle 'while': Se ejecuta mientras una condición sea verdadera, permitiendo la repetición de un bloque de código hasta que la condición ya no se cumpla.

## Sintaxis:

```python

while condicion:
    # Bloque de código a ejecutar

```

### Ejemplo:

```python

contador = 0

while contador < 6:
    print(contador)
    contador += 1

```

#### Beneficios de los Bucles:

- Automatizan tareas repetitivas.
  
- Procesan datos de manera eficiente.

# • ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una forma concisa y elegante de crear listas en Python. 
Permite la construcción rápida de listas aplicando una expresión a cada elemento de una secuencia.

## Beneficios de las Listas por Comprensión:

- Facilitan la creación rápida y concisa de listas.
  
- Mejoran la legibilidad del código.

### Sintaxis

```python

[expresion for elemento in secuencia]

```

#### Ejemplo:

```python

cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

```

# • ¿Qué es un argumento en Python?

Un argumento es un valor que se pasa a una función cuando se llama. 
Las funciones pueden aceptar cero o más argumentos, y se utilizan para proporcionar datos a la función para que pueda realizar su tarea.

## Sintaxis:

```python

def nombre_de_funcion(argumento):
    # Cuerpo de la función

```

### Ejemplo:

```python

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ander")

```

#### Beneficios de los Argumentos:

- Permiten que las funciones sean más flexibles y reutilizables.

- Facilitan la modularización del código.

# • ¿Qué es una función Lambda en Python?

Es una función anónima y pequeña que se define sin un nombre utilizando la palabra clave 'lambda'. 
Son útiles para operaciones simples y pueden usarse en cualquier lugar donde se requiera una función.

## Sintaxis

```python

lambda argumentos: expresion

```

### Ejemplo:

```python

doble = lambda x: x * 2
print(doble(5))

```

#### Beneficios de las Funciones Lambda:

- Permiten definir funciones de forma rápida y concisa.
  
- Son útiles para operaciones simples en las que no es necesario definir una función completa.

# • ¿Qué es un paquete pip?

PIP es el instalador de paquetes de Python.
Un paquete pip es un conjunto de archivos que se distribuyen junto con metadatos que describen el paquete. 

PIP se utiliza para instalar, actualizar y administrar paquetes de software escritos en Python que no forman parte de la biblioteca estándar de Python.

## Ejemplo:

```python

pip install nombre_paquete

```