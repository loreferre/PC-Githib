
def iterateDictionary(some_list):
    for diccionario in some_list:
        for key, value in diccionario.items():
            print(f"{key} - {value}, ", end="")
        print()

estudiantes = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'},
    {'first_name': 'Mark', 'last_name' : 'Guillen'},
    {'first_name': 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(estudiantes)

def iterateDictionary2(key_name, some_list)
