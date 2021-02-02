import sys
import random

def match_maker(men,women):
    print("\nBegining the match making")
    print("------------------------------------------------------")
    matched_women = {}
    free_men = []
    for man in men:
        free_men.append([man,0])
    
    # free_men.append(["M3",0])

    while(free_men):
        current_woman = men[free_men[-1][0]][free_men[-1][1]]
        print(f"{free_men[-1][0]} is proposing to {current_woman}")

        if not (current_woman in matched_women):
            print(f"{current_woman} is Single and Accepts {free_men[-1][0]}")
            matched_women[current_woman] = free_men[-1][0]
            free_men.pop()

        else:
            ex_pos = find_pos(women[current_woman],matched_women[current_woman])
            new_pos = find_pos(women[current_woman],free_men[-1][0])

            if(ex_pos<new_pos):
                print(f"{free_men[-1][0]} you've been Rejected by {current_woman}")
                print(f"{current_woman} Prefers {matched_women[current_woman]}")

            else:
                print(f"{current_woman} Dumps {matched_women[current_woman]} because she prefers {free_men[-1][0]}")
                print(f"{current_woman} accepts {free_men[-1][0]}")
                
                ex_new_pos = find_pos(men[matched_women[current_woman]],current_woman) + 1
                current_man = free_men.pop()
                free_men.append([matched_women[current_woman],ex_new_pos])
                matched_women[current_woman] = current_man[0]

            free_men[-1][1] = free_men[-1][1] + 1

    print(matched_women)
        

# Function Populates list of men and women with random preference 
def populate(n):
    print("Populating the lovely contestants")
    men = {}
    women = {}

    for i in range(0,n):

        # Initializes an empty list inside of each of the men and women objects 
        men[f'M{i}'] = []
        women[f'F{i}'] = []

        # Populates men and women 0 through n
        for j in range(0,n):
            men[f'M{i}'].append(f'F{j}')
            women[f'F{i}'].append(f'M{j}')

        # Randomizes the order of the freshly added arrays
        men[f'M{i}'] = random.sample(men[f'M{i}'],n)
        women[f'F{i}'] = random.sample(women[f'F{i}'],n)
        # print(find_pos(women[f'F{i}'], 'M1'))
    
    for i, man in enumerate(men):
        print(man, end = " ")
        print(men[f"M{i}"])
    
    print(" ")

    for i, woman in enumerate(women):
        print(woman, end = " ")
        print(women[f"F{i}"])
    
    match_maker(men,women)
    return [men,women]

def find_pos(arr,name):
    return arr.index(name)


n = int(sys.argv[1])
populate(n)