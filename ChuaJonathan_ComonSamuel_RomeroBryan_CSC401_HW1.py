# Jonathan Chua
# Samuel Comon
# Bryan Romero
# Homework #1 Stable Matching & Gale Shapley Algorithm

import sys
import random

#Person object definition
class Person:
    def __init__(self, name, married, list) -> None:
        self.name = name
        self.married = married
        self.list = list
    
    #toPrint method to unbox
    def toPrint(self):
        print("\n" + self.name +" is married to " + str(self.married))
        print("Preference: ", self.list)


#Generates a list of men for sampling
def generateMen(n):
    list = []

    for x in range(1,n+1):
        list.append('Man#' + str(x))

    return list

#Generates a list of women for sampling
def generateWomen(n):
    list = []

    for x in range(1,n+1):
        list.append('Woman#' + str(x))

    return list

#Generates a list of Persons with list of opposite sex
def generateObjectList(n, type):
    list = []

    if(type == "man"):
        women = generateWomen(n)
        for x in range(1, n+1):
            name = ('Man#' + str(x))
            list.append(Person(name, None, random.sample(women, n)))
    else:
        men = generateMen(n)
        for x in range(1, n+1):
            name = ('Woman#' + str(x))
            list.append(Person(name, None, random.sample(men, n)))
            
    return list

#Tool to print the Person list
def printPersonList(list):
    for person in list:
        person.toPrint()

x = int(sys.argv[1])
listOfMen = generateObjectList(x, "man")
listOfWomen = generateObjectList(x, "woman")
printPersonList(listOfMen)
printPersonList(listOfWomen)


    