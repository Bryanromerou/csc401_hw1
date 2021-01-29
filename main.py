import sys
import random

def match_maker(men,women):
    print("This is working")
    matched_women = {}
    available_men = []
    for man in men:
        available_men.append(man)
    while(available_men):
        print("working")
        print(available_men.pop())

def populate(n):
    men = {}
    women = {}

    for i in range(0,n):
        men[f'M{i}'] = []
        women[f'F{i}'] = []

        for j in range(0,n):
            men[f'M{i}'].append(f'F{j}')
            women[f'F{i}'].append(f'M{j}')

        random.shuffle(men[f'M{i}'])
        random.shuffle(women[f'F{i}'])
    
    for i, man in enumerate(men):
        print(man, end = " ")
        print(men[f"M{i}"])
    
    print(" ")

    for i, woman in enumerate(women):
        print(woman, end = " ")
        print(women[f"F{i}"])
    
    match_maker(men,women)
    return [men,women]

n = int(sys.argv[1])
populate(n)