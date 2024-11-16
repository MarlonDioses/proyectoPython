"""Definiendo varibles con snake_case"""
name = "marlon"

"""concatenar con + """
bienvenido = "hola" + name + "como estas?"
print(bienvenido)


"""concatenar con f string, 
sirve para concatenar y convertir un numero a texto y se agrega al inicio y con llaves"""

name = 5
bienvenido = f"hola {name} como estas?"
print(bienvenido)

"""operadores de pertenencia, (in not in) habla de como saber si un dato esta dentro de una variable
esto se hace directo en el print"""
name = 5
bienvenido = f"hola {name} como estas?"
print("hola" in bienvenido) #true - verdad

"""en esta parte da true o sea verdad 
ya que si se encuentra dentro de la variable bienvenido"""

name = 5
bienvenido = f"hola {name} como estas?"
print("hola" not in bienvenido) #false - verdad

"""en esta parte da true o sea verdad 
ya que si se encuentra dentro de la variable bienvenido"""