# AOC 2022 - DAY XX

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

def solution_phase1(data):
    return(None)

## test

solution_phase1_test_dXX = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day XX{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_dXX}{Style.RESET_ALL}")

## submission

solution_phase1_dXX = solution_phase1(data)
print(f"solution {Fore.BLUE}day XX{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_dXX}{Style.RESET_ALL} ⭐")

# phase 2

def solution_phase2(data):
    return(None)

## test

solution_phase2_test_dXX = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day XX{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_dXX}{Style.RESET_ALL}")

## submission

solution_phase2_dXX = solution_phase2(data)
print(f"solution {Fore.BLUE}day XX{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_dXX}{Style.RESET_ALL} ⭐")


