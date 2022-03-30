import os
from pickle import TRUE
import random
from time import strftime
from classes import alphabet
from classes import language



def unionAlf(alp1, alp2):
    list1 = mainList[alp1]
    list2 = mainList[alp2]
    unionList = []
    for element in list1.getChainAlphabet():
        if element not in unionList:
            unionList.append(element)
    for element in list2.getChainAlphabet():
        if element not in unionList:
            unionList.append(element)
    return unionList


def alphabetDifference(alp1, alp2):
    list1 = mainList[alp1]
    list2 = mainList[alp2]
    differenceList = []
    for item in list1.getChainAlphabet():
        if item not in list2.getChainAlphabet():
            differenceList.append(item)
    if differenceList == []:
        return "λ"
    return differenceList


def alphabetIntersection(alp1, alp2):
    list1 = mainList[alp1]
    list2 = mainList[alp2]
    intersectionList = []
    for item1 in list1.getChainAlphabet():
        for item2 in list2.getChainAlphabet():
            if item1 in list2.getChainAlphabet() and item2 in list1.getChainAlphabet():
                intersectionList.append(item1)
    if intersectionList == []:
        return "λ"
    return set(intersectionList)


def alphabetLock(list, noWords):
    listLocked = ["λ"]
    for i in range(noWords):
        word = ""
        for j in range(random.randint(2, 5)):
            word += str(list[random.randint(0, len(list) - 1)])
            if word not in listLocked and len(listLocked) <= noWords:
                listLocked.append(word)
    return listLocked


def generateLanguage(lista,noWordsLeng):
    languageList=[]
    for i in range(noWordsLeng):
        word = ""
        for j in range(random.randint(1, 55)):
            word += str(lista[random.randint(0, len(lista) - 1)])
            if word not in languageList and len(languageList) < noWordsLeng:
                languageList.append(word)
    print(languageList)
    languageList.append(languageList)
    return languageList





def alpmenu():
    closeProgram = False
    while not closeProgram:
        option=int(input("""
    **********************************************************
    *Elija que operacion quiere hacer con su(s) alfabeto(s): *
    *    1 - Imprimir el(los) Alfabeto(s)                    *
    *    2 - Union de alfabetos                              *
    *    3 - Diferencia de alfabetos                         *
    *    4 - Intersección de alfabetos                       *
    *    5 - Cerradura de estrella de alfabeto               *
    *    6 - Generar lenguaje                                *
    
    *    0 - Salir                                           *
    **********************************************************
    Opción: """))
        match option:
            case 1:
                for i in range(alpQuantity):
                    print("Alfabeto " + str(i + 1) + ": ")
                    print(mainList[i])
                os.system("PAUSE")
                os.system("cls")
            case 2:
                index1 = int(input("Ingrese el primer alfabeto que quiere unir: "))
                index2 = int(input("Ingrese el segundo alfabeto que quiere unir: "))
                if index1 <= alpQuantity and index2 <= alpQuantity:
                    print ("La union de los alfabetos "+str(index1)+" y "+str(index2)+" es: ")
                    print(unionAlf(index1-1, index2-1))
                    os.system("PAUSE")
            case 3:
                index1 = int(input("Ingrese el primer alfabeto:"))
                index2 = int(input("Ingrese el alfabeto que quiere restar: "))
                if index1 <= alpQuantity and index2 <= alpQuantity:
                    print ("La Diferencia de los alfabetos "+str(index1)+" y "+str(index2)+" es: ")
                    print(alphabetDifference(index1-1, index2-1))
                    os.system("PAUSE")
            case 4:
                index1 = int(input("Ingrese el primer alfabeto:"))
                index2 = int(input("Ingrese el segundo alfabeto: "))
                if index1 <= alpQuantity and index2 <= alpQuantity:
                    print ("La interseccion de los alfabetos "+str(index1)+" y "+str(index2)+" es: ")
                    print(alphabetIntersection(index1-1, index2-1))
                    os.system("PAUSE")
                else:
                    print("Alfabetos ingresados invalidos")
                    os.system("PAUSE")
            case 5:
                index = int(input("Ingrese el alfabeto que quiere clausurar: "))
                quantity = int(input("Ingrese la cantidad de palabras que desea: "))
                if index <= alpQuantity:
                    print ("La clausura o cerradura de estrella del alfabeto "+str(index)+" es: ")
                    print(alphabetLock(mainList[index-1].getChainAlphabet(), quantity))
                    os.system("PAUSE")
            case 6:
                index = int(input("Ingrese el alfabeto sobre el que quiere generear el lenguaje: "))
                quantity = int(input("Ingrese la cantidad de palabras que desea generar en el lenguaje: "))
                if index <= alpQuantity:
                    langObejct = language(generateLanguage(
                        mainList[index - 1].getChainAlphabet(), quantity))
                    languageList.append(langObejct)
                    os.system("PAUSE")
            case 7:

            case 0:
                print("Programa cerrado con exito!")
                closeProgram = True
            case _:
                print("Ingrese una opcion correcta")
                os.system("PAUSE")




if __name__ == "__main__":
    flag = 0
    mainList = []
    languageList = []

    while flag == 0:
        alpQuantity = int(input("Ingrese la cantidad de alfabetos que va a ingresar: "))
        while alpQuantity < 1:
            print("Error ingrese un numero (minimo 2)")
            alpQuantity = int(input("Ingrese la cantidad de alfabetos que va a ingresar: "))
        for i in range(alpQuantity):
            alpCad = ""
            alpCad = input("ingrese su alfabeto número " + str(i + 1) + " separada por espacios: ").split(" ")
            if alpCad.__contains__(""):
                mainList.append(alphabet("λ"))
            else:
                alpObject = alphabet(alpCad)
                mainList.append(alpObject)
        flag = 1
        alpmenu()
