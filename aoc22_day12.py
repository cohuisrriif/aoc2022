# AOC 2022 - DAY 12

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint
import string

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 12{Style.RESET_ALL}")

# load data test
with open('./input/input_day12_test.txt') as f:
    data_test = [list(x)  for x in f.read().split('\n')]
    
# load data complete 
with open('./input/input_day12.txt') as f:
    data = [list(x)  for x in f.read().split('\n')]


lvl = {}
i = 1
for y in list(string.ascii_lowercase):
    lvl[y] = i
    i += 1
lvl['E'] = 26
lvl['S'] = 1

edges = [[list(string.ascii_uppercase)[y] + str(x) for x in range(len(data_test[0]))] for y in range(len(data_test))]

for y in range(len(data_test)):
    for x in range(len(data_test[0])): 
        if data_test[y][x] == "E":
            edges[y][x] ="E"
        if data_test[y][x] == "S":
            edges[y][x] = "S"
            
edges_info  ={}
for y in range(len(data_test)):
    for x in range(len(data_test[0])): 
        edges_info[edges[y][x]] = (x, y, data_test[y][x], lvl[data_test[y][x]])
        
            
def flatten(l):
    return [item for sublist in l for item in sublist] 

def get_neighboors(x, y, x_dim, y_dim):
    neighboors = []
    if x != 0 and y !=0 and x!= x_dim-1 and y!= y_dim-1:
        neighboors.append((x, y-1))
        neighboors.append((x, y+1))
        neighboors.append((x+1, y))
        neighboors.append((x-1, y))
    elif x!=0 and x!= x_dim-1 and y == 0:
        neighboors.append((x-1, y))
        neighboors.append((x+1, y))
        neighboors.append((x, y+1))
    elif x!=0 and x!= x_dim-1 and y == y_dim-1:
        neighboors.append((x-1, y))
        neighboors.append((x+1, y))
        neighboors.append((x, y-1))
    elif y!=0 and y!= y_dim-1 and x == 0:
        neighboors.append((x, y-1))
        neighboors.append((x, y+1))
        neighboors.append((x+1, y))
    elif y!=0 and y!= y_dim-1 and x == x_dim-1:
        neighboors.append((x, y-1))
        neighboors.append((x, y+1))
        neighboors.append((x-1, y))
    elif 
    return(neighboors)

print(get_neighboors(2,2,5,5))
    
    
    
    


graph = {}
for edge in flatten(edges):
    edge_neighboor = []
    x, y = edges_info[edge][0], edges_info[edge][1]
    lvl_edge = edges_info[edge][3]
    if y != 0 and y != len(edges) and x != 0 and x != len(edges[0]):
        
        edges_info[edges[y][x]]
"""

    
for y in range(len(data_test)):
    for x in range(len(data_test[0])):  
        

"""

    
"""

        
        
        





# phase 1

def solution_phase1(data):
    return(None)

## test 

solution_phase1_test_d12 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 12{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d12}{Style.RESET_ALL}")

## submission 

solution_phase1_d12 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 12{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d12}{Style.RESET_ALL} ⭐")

# phase 2

def solution_phase2(data):
    return(None)

## test 

solution_phase2_test_d12 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 12{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d12}{Style.RESET_ALL}")

## submission 

solution_phase2_d12 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 12{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d12}{Style.RESET_ALL} ⭐")
"""

