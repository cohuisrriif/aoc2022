# AOC 2022 - TEMPLATE
XX = day

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY XX{Style.RESET_ALL}")

# load data test
with open('./input/input_dayXX_test.txt') as f:
    data_test = None #f.read().split('\n')
    
# load data complete 
with open('./input/input_dayXX.txt') as f:
    data = None #f.read().split('\n')

# phase 1

"""
CODE OF PHASE 2    
"""

## test 

solution_phase1_test_dXX = None
print(f"solution {Fore.BLUE}day XX{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_dXX}{Style.RESET_ALL}")

## submission 

solution_phase1_d3 = sum([getitempriority(getcommonitem(rucksack)) for rucksack in data])
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_dXX}{Style.RESET_ALL} ⭐")

# phase 2

"""
CODE OF PHASE 2    
"""

## test 

solution_phase2_test_d3 = None
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_dXX}{Style.RESET_ALL}")

## submission 

solution_phase2_d3 = None
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_dXX}{Style.RESET_ALL} ⭐")


