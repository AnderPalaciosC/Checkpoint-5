# • ¿Qué es un condicional?

#	 El condicional es un codigo que solo se ejecutará si la condición es verdadera (True)

edad = 18

if edad >= 18:
    print("Tienes acceso")
else:
    print("Acceso denegado")

# • ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

#	    Existe el bucle 'for' y el bucle 'while'.
	
#	    El bucle 'for' permite ejecutar un bloque de código una vez para cada elemento de la secuencia.

colores = ["azul", "amarillo", "rojo"]

for color in colores:
    print(color)

#	    El bucle 'while' es útil cuando no se sabe cuántas veces se debe ejecutar el bloque de código.

contador = 0

while contador < 6:
    print(contador)
    contador += 1

# • ¿Qué es una lista por comprensión en Python?

#       Permite crear listas de manera más elegante y eficiente

cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

# • ¿Qué es un argumento en Python?

#       Es un valor que se pasa a una función cuando se llama, las funciones pueden aceptar cero o más argumentos. 

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ander")

# • ¿Qué es una función Lambda en Python?

#       Es una función anónima y pequeña que se define sin un nombre utilizando la palabra clave lambda. Son útiles para operaciones simples y pueden usarse en cualquier lugar donde se requiera una función.

doble = lambda x: x * 2
print(doble(5))

# • ¿Qué es un paquete pip?

#       PIP es el instalador de paquetes de Python. Un paquete pip es un conjunto de archivos y se utiliza para instalar, actualizar y administrar paquetes de software escritos en Python que no forman parte de la biblioteca estándar de Python.

# pip install nombre_paquete