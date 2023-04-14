nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]



#INCISO B

def promedioAlumno(notasCompletas):
    promedios = dict(map(lambda alumno: (alumno, sum(notasCompletas[alumno]) / 2), notasCompletas))
    return promedios


#INCISO C

def promedioGeneral(notasCompletas):
    notas = list(map(lambda alumno: sum(notasCompletas[alumno]) / 2, notasCompletas))
    promedioG = round(sum(notas) / len(notas),2)
    return f"El promedio general de los alumnos es: {promedioG}"


#INCISO D

def mejorPromedio(notasCompletas):
    promedios = list(map(lambda alumno: sum(notasCompletas[alumno]) / len(notasCompletas[alumno]), notasCompletas))
    mejor_promedio = max(promedios)
    mejor_alumno = list(filter(lambda alumno: sum(notasCompletas[alumno]) / len(notasCompletas[alumno]) == mejor_promedio, notasCompletas))
    return f"El alumno con mejor Promedio es: {mejor_alumno[0]} con un promedio de: {mejor_promedio}"


#INCISO E

def alumnoPeorNota(notasCompletas):
    peor_nota = min(list(map(lambda alumno: min(notasCompletas[alumno]),notasCompletas)))
    alumnoPN = [alumno for alumno in notasCompletas if min(notasCompletas[alumno]) == peor_nota]
    return f"El alumno con peor nota es: '{alumnoPN[0]}' con una nota de {peor_nota}"

#INCISO A

alumnos = tuple(nombres.replace("'","").replace("\n","").split(","))
notasCompletas = dict(map(lambda x, y: (x, y), alumnos, zip(notas_1, notas_2)))

# print(notasCompletas) #INCISO A
# print(promedioAlumno(notasCompletas))  #  INCISO B
print(promedioGeneral(notasCompletas)) #INCISO C
# print(mejorPromedio(notasCompletas)) #INCISO D
# print(alumnoPeorNota(notasCompletas)) #INCISO E
