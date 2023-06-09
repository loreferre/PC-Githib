"""
def  valores_mayores_que_el_segundo (lista):
    resultado = []
    
    if len (lista) >= 2:
        for numero in lista:
            if numero > lista[1]:
                resultado.append (numero)

    print(len(resultado))
    if len (resultado)<2:
        return False
    else:
        return resultado
    
lista1 = valores_mayores_que_el_segundo ([5,2,3,2,1,4])
print(lista1)
lista2 = valores_mayores_que_el_segundo([3,6])
print(lista2)
lista3 = valores_mayores_que_el_segundo ([5,4,8])
print(lista3)

"""

def valores_mayores_que_el_segundo(lista):
    if len(lista) < 4: 
        return False

    segundo_valor = lista[2]
    nueva_lista = [numero for numero in lista if numero > segundo_valor]

    print(len(nueva_lista))
    return nueva_lista

lista1= valores_mayores_que_el_segundo([5,2,3,2,1,4])
print(lista1)
lista2= valores_mayores_que_el_segundo([3])
print(lista2)
