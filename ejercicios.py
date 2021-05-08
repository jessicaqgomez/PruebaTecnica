import numpy as np
#1. how do you found the missing number in given integer array of 1 to 100
def ejercicio1(arreglo):
    completo = np.array(range(1,len(arreglo)+2))
    faltante= np.setdiff1d(completo,arreglo)   
    return faltante


#2. how do you find the duplicate number on a given interger array
def ejercicio2(arreglo):
    numeros = set()
    for i in range(len(arreglo)):
        if arreglo[i] in numeros:
            return arreglo[i]
        else:
            numeros.add(arreglo[i])
    
#3. how do you find de largest and smallest number in an unsorted interger array
'''
podemos tener dos opciones para realizar el ejercicio:
1. usando la función max y min de la librería numpy
2. organizando el arreglo y seleccionando la primera y la ultima posición
'''
def ejercicio3_1(arreglo):
    maximo = np.max(arreglo)
    minimo = np.min(arreglo)
    print (maximo)
    print (minimo)
    respuesta = [maximo,minimo]
    return respuesta

def ejercicio3_2(arreglo):
    arreglo.sort()
    print("el valor minimo es: ",arreglo[0]," y el valor máximo es: ",arreglo[len(arreglo)-1])
    respuesta = [arreglo[0], arreglo[len(arreglo)-1]]
    return respuesta

#4. how do you find all pairs of an integer array whose sum is equal to a given number.
def ejercicio4(arreglo,suma):
    pares = list()
    for i in range(0,len(arreglo)):
        for j in range(i+1, len(arreglo)):
            if ((arreglo[i]+arreglo[j])==suma):
                pares.append([arreglo[i],arreglo[j]])
    return pares
#5. how do you find a duplicate numbers in an array if it contains multiple duplicates
def ejercicio5(arreglo):
    numeros = set()
    duplicados = set()
    for i in range(len(arreglo)):
        if arreglo[i] in numeros:
            duplicados.add(arreglo[i])
        else:
            numeros.add(arreglo[i])
    return duplicados

#------------------------- arreglos para pruebas --------------------------------------#
prueba = [-1,2,454,6,3,5,7]
prueba3 = [1,2,3,4,6,7,8,9]
prueba4 = [1,2,3,2,4,5,6,9,7,8,7,10,9]
prueba2 = np.array(range(1,100))
print(ejercicio4(prueba4,4))
