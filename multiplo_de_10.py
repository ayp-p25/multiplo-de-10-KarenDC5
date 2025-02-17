"""
Determinar si un número dado es múltiplo de 10
Karen Durán
757136
Ingeniería Civil
Algoritmos y Programación 
ESI232B2
17/02/25
minutos 
"""
# Declaraciones 
MULTIPLO_10 = 10

# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
if numero % MULTIPLO_10 == 0:
    multiplo = 'si es múltiplo de 10' 
else:
    multiplo = 'no es múltiplo de 10' 

# Salidas
print("El número", numero, multiplo)

