#1

def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())

#El resultado deberia ser 5 porque llama al numero de grupo alimentarios y al ejecutar eso vuelve a return que es 5. 

"""#2
def número_de_ramas_militares():
    return 5
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo() + número_de_ramas_militares())

#Faltan variables. Hay que poner el return en cada variables para ejecutarlo."""

def número_de_ramas_militares():
    return 5
def número_de_días_en_una_seman():
    return 7
def silicona_o_lados_del_triángulo():
    return 3

print(número_de_días_en_una_seman() + silicona_o_lados_del_triángulo() + número_de_ramas_militares())

"""#3
def número_de_libros_en_espera():
    return 5
    return 10
print(número_de_libros_en_espera())"""

# Para que se ejecuten el 5 y el 10 deberian estar jusnto (5, 10) en este caso solo quedara 5
#3
def número_de_libros_en_espera():
    return (5, 10)
print(número_de_libros_en_espera())

"""#4
def número_de_dedos():
    return 5
    print(10)
print(número_de_dedos())"""

#Para que esta función corra primero deberia estar el print(10) para que luego retorne y tome al 5 para terminar la función

def número_de_dedos():
    print(10)
    return 5

print(número_de_dedos())

"""#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
print(x)"""

#Esta funcióm, haria el primer print que es 5 y el sigueinte print no lo tomaria, quedando en nada. Se podria usar return y asignarle a (x) el valor de 5.

def número_de_lagos_grandes():
    return 5

x = número_de_lagos_grandes()
print(x)

#6
def add(b,c):
    return b+c
print (add(1,2) + add(2,3))

#El resultado seria 8, se  reemplaza (1+2) + (2+3)

#7
def concatenar(b,c):
    return str(b)+str(c)
print(concatenar(2,5))

#En esta función con srt los numeros se comportan como palabras y quedaria 25 junto.

"""#8
def número_de_océanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
    return 10
    return 7
print(número_de_oceános_o_dedos_o_continentes())"""

#Esta función tiene dos falsos por ende las itiraciones terminan en el 10 y no llegan al 7.
#se podria arreglar de la siguiente manera:

def número_de_océanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10, b
print(número_de_océanos_o_dedos_o_continentes())


"""#9
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3

print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3))
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))

"""



#Esta función tenia problemas con las variables que no eran identificadas, una vez corregido esto para que el nombre fuera igual en todo los casos, funcionó. Pero no tomó el return 3. 
#Para que fuera tomado se sugiere poner un elif y la función quedaria así:

def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b, c):
    if b < c:
        return 7
    elif b > c:
        return 14
    else:
        return 3
    
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3))
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))



#10
def addition(b,c):

    return b+c
    return 10
print(addition(3,5))

#En esta función la función termina en el primer return b+c. Para corregir esto, se puede cambiar el return 10 por otra condición.


"""
#11
b = 500
print(b)

def foobar():
    b ="operador de palabra clave from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)

"""

#Para la funcion foobar hayq que posicionar >=300 en un print para quede como 500>=300

b = 500
print(b)
def foobar():
    b ="operador de palabra clave from-rainbow" 
    print(b)
foobar()

print(b >= 300) 
print(b)


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#Esta función comienza en 500, luego foobar cambia b a 300, y al imprimir vuelva a 500.

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#Esta función comienza en 500 se mantiene el 500 y cambia foobar a 300 y termina en 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#Primero, foo imprime 1. Luego, foo llama a bar, que imprime 3. Al final, termina en 2.




#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10

def bar():
    print(3)
    return 5
y = foo()
print(y)

#Al igual que en la atenrio, la variable foo es 1, y llama a bar que seria 3. Al terminar esta función se aplica return que es 5 y al final es retunr 10. 