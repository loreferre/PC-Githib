def countdown (num):
    resultado = []
    while num >=-10:
        resultado.append(num)
        num-=1
    return resultado

lista1=countdown(0) 
lista2=countdown(5)
lista3=countdown(10)

print(lista1)
print(lista2)
print(lista3)
