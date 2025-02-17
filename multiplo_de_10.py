"""
Determinar si un número dado es múltiplo de 10
Karen Durán
757136
Ingeniería Civil
Algoritmos y Programación 
ESI232B2
17/02/25
20 minutos 
"""
# Declaraciones 
MULTIPLO_10 = 10

# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
if numero % MULTIPLO_10 == 0:
    multiplo = True
else:
    multiplo = False

# Salidas
if multiplo: 
    print("El número", numero, "sí es múltiplo de 10")
else: 
    print("El número", numero, "no es múltiplo de 10")


