from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
cant_correctos = 0
cant_incorrectos = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!.")
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    operator = choice(operators)
#Se descartá que una operación sea x/0
    if operator == "/": 
        number_2 = randrange(1,10)
    else:
        number_2 = randrange(10)
# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
# Le pedimos al usuario el resultado
    result = input("resultado: ")
    if operator == "+":
        if float (result) == (number_1 + number_2):
            print("El resultado es correcto.")
            cant_correctos+=1
        else:
            print("El resultado es incorrecto")
            cant_incorrectos+=1
    elif operator == "-":
        if float (result) == (number_1 - number_2):
            print("El resultado es correcto.")
            cant_correctos+=1
        else:
            print("El resultado es incorrecto")
            cant_incorrectos+=1
    elif operator == "*":
        if float (result) == (number_1 * number_2):
            print(f"El resultado es correcto.")
            cant_correctos+=1
        else:
            print("El resultado es incorrecto")
            cant_incorrectos+=1
    elif operator == "/":
        if round(float(result), 2) == round((number_1 / number_2), 2): #Si la division es decimal infinita, redondeamos el resultado.
            print("El resultado es correcto.")
            cant_correctos += 1
        else:
            print("El resultado es incorrecto")
            cant_incorrectos += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print (f"La cantidad de respuestas correctas son: {cant_correctos}")
print (f"La cantidad de respuestas incorrectas son: {cant_incorrectos}")