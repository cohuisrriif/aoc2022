# AOC 2022 - DAY 9 

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 9{Style.RESET_ALL}")

# load data test
with open('./input/input_day9_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day9.txt') as f:
    data = f.read().split('\n')

def generatesetup(instructions):
    
    x_init, y_init = (0, 0)
    x_min, x_max = (0, 0)
    y_min, y_max = (0, 0)
    x_current, y_current = (0, 0)
    
    for instruction in instructions:
        
        direction = instruction["direction"]
        distance = instruction["distance"]
        
        if direction == "L":
            x_current -= distance 
            if x_current < x_min:
                x_min = x_current 
        elif direction == "R":
            x_current += distance 
            if x_current > x_max:
                x_max = x_current 
        elif direction == "U":
            y_current -= distance
            if y_current < y_min:
                y_min = y_current 
        else:
            y_current += distance
            if y_current > y_max:
                y_max = y_current

    # setup the initial position 
    if x_min < 0:
        x_init = x_init - x_min
    if y_min <0 :
        y_init = y_init - y_min
    # setup the maps
    travelmap = [['.' for _ in range(x_max - x_min + 1)] for _ in range(y_max - y_min + 1)]
    visitmap = [[0 for _ in range(x_max - x_min + 1)] for _ in range(y_max - y_min + 1)]
    result = {"travelmap": travelmap, "visitmap": visitmap, "init": (x_init, y_init)}
    
    return(result)

def visualise(map):
    map = [[str(x) for x in y] for y in map]
    result = [''.join(x) for x in map]
    y = ""
    for x in result:
        y += x + "\n" 
    return(y)

def updatetravelH(travelmap, instruction):

    direction = instruction["direction"]
    distance = instruction["distance"]
    
    # current state
    
    for sublist in travelmap:
        if 'H' in sublist:
            y_h = travelmap.index(sublist)
            x_h = sublist.index('H')
            travelmap[y_h][x_h] = "."
            
    if direction == "L":
        x_h -= distance 
    elif direction == "R":
        x_h += distance
    elif direction == "U":
        y_h -= distance
    else:
        y_h += distance

    if travelmap[y_init][x_init] == '.' :
        travelmap[y_init][x_init] = "S"
    
    travelmap[y_h][x_h] = "H"
    return(travelmap)   

def updatetravelT(travelmap, instruction):

    direction = instruction["direction"]

    for sublist in travelmap:
        if 'H' in sublist:
            y_h = travelmap.index(sublist)
            x_h = sublist.index('H')

    for sublist in travelmap:
        if 'T' in sublist:
            y_t = travelmap.index(sublist)
            x_t = sublist.index('T')
            if travelmap[y_init][x_init] == '.':
                travelmap[y_init][x_init] = "S"
            else:
                travelmap[y_t][x_t] = "."
            
    if direction == "L":
        x_t = x_h + 1
        y_t = y_h
    elif direction == "R":
        x_t = x_h - 1
        y_t = y_h
    elif direction == "U":
        x_t = x_h
        y_t = y_h  + 1 
    else:
        x_t = x_h
        y_t = y_h - 1
    
    travelmap[y_t][x_t] = "T"      
            
    return(travelmap)   

def updatevisit(visitmap, travelmap):
    for sublist in travelmap:
        if 'H' in sublist:
            y = travelmap.index(sublist)
            x = sublist.index('H')
            visitmap[y][x] += 1
    return(visitmap)  

instructions = [{"direction": line.split(' ')[0], "distance": int(line.split(' ')[1])} for line in data_test]

# initial state
setup = generatesetup(instructions)
travelmap = setup['travelmap']
visitmap = setup['visitmap']
x_init, y_init = setup['init']
travelmap[y_init][x_init] = "H"
visualise(travelmap)
#visualise(visitmap, 'init')

import time
for instruction in instructions:
    travelmap = updatetravelH(travelmap, instruction)
    travelmap = updatetravelT(travelmap, instruction)
    print(f"instruction : {instruction} \n {visualise(travelmap)}", end="\r", flush=True)
    time.sleep(1)
    """
    print("", end="\r")
    print("==MAP==", end="\r")
    travelmap = updatetravelH(travelmap, instruction)
    print(visualise(travelmap), end="\r")
    travelmap = updatetravelT(travelmap, instruction)
    print("------", end="\r")
    print("T update", end="\r")
    print("------", end="\r")
    print(visualise(travelmap), end="\r")
    print("======", end="\r")
    time.sleep(1)
    visitmap = updatevisit(visitmap, travelmap)
    visualise(travelmap)
    #visualise(visitmap)
    """
#visualise(visitmap)





"""
# phase 1

def solution_phase1(data):
    return(None)

## test 

solution_phase1_test_d9 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 9{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d9}{Style.RESET_ALL}")

## submission 

solution_phase1_d9 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 9{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d9}{Style.RESET_ALL} â­")

# phase 2

def solution_phase2(data):
    return(None)

## test 

solution_phase2_test_d9 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 9{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d9}{Style.RESET_ALL}")

## submission 

solution_phase2_d9 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 9{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d9}{Style.RESET_ALL} â­")
"""

