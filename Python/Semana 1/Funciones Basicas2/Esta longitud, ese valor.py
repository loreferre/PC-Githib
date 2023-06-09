"""escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y 
devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]"""

def length_and_value (size, value):
    return [value] * size

size1=length_and_value(4,7)
print(size1)
size2=length_and_value(6,2)
print(size2)
size3=length_and_value(9,10)
print(size3)