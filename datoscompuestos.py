
"""list []- Listas se esciben dentro de los corchetes y se pueden modificar
tener en cuenta que el primer valor que se muestra es 0 y asi sucesivamente"""
list = ["name", "age", True, 1.68]
print(list[0])

"""tuple ()- tuplas no se pueden modificar y van en parentesis"""
tuple = ("name", "age", True, 1.68)
print(list[0])

"""conjunto (set){} - se pueden modificar y van en llaves
no se puede acceder a los elementos por el indice y no almacen datos duplicados"""
conjunto = {"name", "age", True, 1.68}
print(list[0])

"""creando un diccionario - (la estructura es key: value y separamos con comas)
para crear un dict va con llaves y se define el primer dato y su valor seguido de dos
 puntos y coma al final, menos coma al final de todo"""
diccionario = {"name": "Marlon",
                "age": 33,
                  "peso": 70,
                  "altura": 1.68}
print(diccionario["altura"])