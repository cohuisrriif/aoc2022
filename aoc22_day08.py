# AOC 2022 - DAY 8

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 8{Style.RESET_ALL}")

# load data test
with open('./input/input_day8_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day8.txt') as f:
    data = f.read().split('\n')

# phase 1

def sublist(liste, index):
    return([item[index] for item in liste])
    
def is_visible(forest, position):
    N_ROW = len(forest)
    N_COL = len(forest[0])
    x = position[0]
    y = position[1]
    tree = forest[y][x]
    if x == 0 or x == N_COL - 1 or y == 0 or y == N_ROW - 1:
        return(1)
    else:
        if tree > max(forest[y][:x]) or \
            tree > max(forest[y][x+1:]) or \
            tree > max(sublist(forest, x)[:y]) or \
            tree > max(sublist(forest, x)[y+1:]):
            return(1)
        else:
            return(0)

def solution_phase1(data):
    forest = [list(map(int, list(x))) for x in data]
    N_ROW = len(forest)
    N_COL = len(forest[0])  
    positions =[(i,j) for i in range(0,N_ROW) for j in range(0,N_ROW)] 
    count = 0
    for position in positions: 
        count += is_visible(forest, position)
    return(count)

## test 

solution_phase1_test_d8 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 8{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d8}{Style.RESET_ALL}")

## submission 

solution_phase1_d8 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 8{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d8}{Style.RESET_ALL} ⭐")

# phase 2

def scenic_score(forest, position):
    x = position[0]
    y = position[1]
    y_trees = forest[y]
    x_trees = sublist(forest, x)

    y_south = y - 1
    y_north = y + 1
    x_east = x - 1
    x_west = x + 1
    
    view_east = 0
    view_west = 0
    view_north = 0
    view_south = 0
    
    if y == 0 or y == len(forest) or x == 0 or x == len(forest[0]):
        score = 0
    else:
        while y_south != -1: 
            if x_trees[y] > x_trees[y_south]:
                view_south += 1
            else:
                view_south += 1
                break
            y_south -= 1
        while y_north != len(forest):
            if x_trees[y] > x_trees[y_north]:
                view_north += 1
            else:
                view_north+= 1
                break
            y_north += 1
        while x_east != -1:
            if y_trees[x] > y_trees[x_east]:
                view_east += 1
            else:
                view_east += 1
                break
            x_east -= 1 
        while x_west != len(forest[0]):
            if y_trees[x] > y_trees[x_west]:
                view_west += 1 
            else:
                view_west += 1
                break
            x_west += 1
        score = view_east * view_west * view_south * view_north
    return(score)

def solution_phase2(data):
    forest = [list(map(int, list(x))) for x in data]
    N_ROW = len(forest)
    N_COL = len(forest[0])  
    positions =[(i,j) for i in range(0,N_ROW) for j in range(0,N_ROW)] 
    score = max([scenic_score(forest, position) for position in positions])
    return(score)

## test 

solution_phase2_test_d8 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 8{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d8}{Style.RESET_ALL}")

## submission 

solution_phase2_d8 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 8{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d8}{Style.RESET_ALL} ⭐")


