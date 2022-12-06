# AOC 2022 - DAY 5 

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 5{Style.RESET_ALL}")

# load data test
with open('./input/input_day5_test.txt') as f:
    data_test = f.read().split('\n')

# load data complete 
with open('./input/input_day5.txt') as f:
    data = f.read().split('\n')

# phase 1

def getNumberStacks(data):
    isnotstacksnumbers = True
    line = 0
    result = None
    while isnotstacksnumbers is True:
        if True in [char.isdigit() for char in data[line]]:
            result = max([int(x) if x.isdigit() else 0 for x in data[line].split(' ')])
            isnotstacksnumbers = False
        elif data[line] == '':
            break
        else:
            line += 1
    return(result)    

def getInitialHeight(data):
    isnotstacksnumbers = True
    line = 0
    while isnotstacksnumbers is True:
        if True in [char.isdigit() for char in data[line]]:
            isnotstacksnumbers = False
        elif data[line] == '':
            break
        else:
            line += 1    
    return(line)

def getCarts(data):
    initial_height = getInitialHeight(data)
    raw_carts = data[:initial_height]
    result_carts = []
    x = 0
    while x < len(raw_carts[0])-2: 
        result_carts.append([s[x:x+3] for s in raw_carts])
        x = x + 4
    result_carts = [[z.replace('[', '').replace(']', '').replace(' ', '') for z in s] for s in result_carts]
    result_carts = [[z for z in s if z] for s in result_carts]
    return(result_carts)
    
def getRearrangement(data):
    result = []
    index_procedures = data.index('') + 1
    for line in range(index_procedures, len(data)):
        procedure = ([int(p) for p in data[line].split(' ') if p.isdigit()])
        procedure = {'move':procedure[0],'from':procedure[1],'to':procedure[2]}
        result.append(procedure)
    return(result)

def getMessage(carts):
    result = ''
    for cart in carts:
        result += cart[0]
    return(result)

def setProcedure(carts, procedure):
    carts_to_move = carts[procedure['from']-1][0:procedure['move']]
    carts[procedure['from']-1] = carts[procedure['from']-1][procedure['move']:]
    carts[procedure['to']-1] = list(reversed(carts_to_move)) + carts[procedure['to']-1]
    return(carts)

def solution_part1(data):
    carts = getCarts(data)
    procedures = getRearrangement(data)
    for procedure in procedures:
        carts = setProcedure(carts, procedure) 
    result = getMessage(carts)
    return(result)

## test 

solution_phase1_test_d5 = solution_part1(data_test)
print(f"solution {Fore.BLUE}day 5{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d5}{Style.RESET_ALL}")

## submission 

solution_phase1_d5 = solution_part1(data)
print(f"solution {Fore.BLUE}day 5{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d5}{Style.RESET_ALL} ⭐")

# phase 2

def setProcedureV2(carts, procedure):
    carts_to_move = carts[procedure['from']-1][0:procedure['move']]
    carts[procedure['from']-1] = carts[procedure['from']-1][procedure['move']:]
    carts[procedure['to']-1] = carts_to_move + carts[procedure['to']-1]
    return(carts)

def solution_part2(data):
    carts = getCarts(data)
    procedures = getRearrangement(data)
    for procedure in procedures:
        carts = setProcedureV2(carts, procedure) 
    result = getMessage(carts)
    return(result)

## test 

solution_phase2_test_d5 = solution_part2(data_test)
print(f"solution {Fore.BLUE}day 5{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d5}{Style.RESET_ALL}")

## submission 

solution_phase2_d5 = solution_part2(data)
print(f"solution {Fore.BLUE}day 5{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d5}{Style.RESET_ALL} ⭐")


