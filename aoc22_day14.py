# AOC 2022 - DAY 14

# load library
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 14{Style.RESET_ALL}")

# load data test
with open('./input/input_day14_test.txt') as f:
    data_test = None #f.read().split('\n')

# load data complete
with open('./input/input_day14.txt') as f:
    data = None #f.read().split('\n')



# phase 1

def solution_phase1(data):
    return(None)

## test

solution_phase1_test_d14 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 14{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d14}{Style.RESET_ALL}")

## submission

solution_phase1_d14 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 14{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d14}{Style.RESET_ALL} ⭐")

# phase 2

def solution_phase2(data):
    return(None)

## test

solution_phase2_test_d14 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 14{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d14}{Style.RESET_ALL}")

## submission

solution_phase2_d14 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 14{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d14}{Style.RESET_ALL} ⭐")


