# AOC 2022 - TEMPLATE

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 6{Style.RESET_ALL}")

# load data test
with open('./input/input_day6_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day6.txt') as f:
    data = f.read().split('\n')

# phase 1

def get_marker(signal):
    ismarkerfound = False
    marker = 4
    while not ismarkerfound:
        if len(set(signal[(marker-4):marker])) == 4:
            ismarkerfound = True
        else:
            marker += 1   
    return(marker)

def solution_part1(data):
    signal = data[0]
    marker = get_marker(signal)
    return(marker)

## test 

solution_phase1_test_d6 = solution_part1(data_test)
print(f"solution {Fore.BLUE}day 6{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d6}{Style.RESET_ALL}")

## submission 

solution_phase1_d6 = solution_part1(data)
print(f"solution {Fore.BLUE}day 6{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d6}{Style.RESET_ALL} ⭐")

# phase 2

def get_markerV2(signal):
    ismarkerfound = False
    marker = 14
    while not ismarkerfound:
        if len(set(signal[(marker-14):marker])) == 14:
            ismarkerfound = True
        else:
            marker += 1   
    return(marker)

def solution_part2(data):
    signal = data[0]
    marker = get_markerV2(signal)
    return(marker)

## test 

solution_phase2_test_d6 = solution_part2(data_test)
print(f"solution {Fore.BLUE}day 6{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d6}{Style.RESET_ALL}")

## submission 

solution_phase2_d6 = solution_part2(data)
print(f"solution {Fore.BLUE}day 6{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d6}{Style.RESET_ALL} ⭐")


