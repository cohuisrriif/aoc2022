# AOC 2022 - DAY 1 

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint
from itertools import groupby

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 2{Style.RESET_ALL}")

# load data test 
with open('./input/input_day1_test.txt') as f:
    data_test = f.read().split('\n')

# load data complete 
with open('./input/input_day1.txt') as f:
    data = f.read().split('\n')

# phase 1 

data_test = [int(calories) if calories else 0 for calories in data_test]
data_test = [sum(list(calories)) for emptychar, calories in groupby(data_test, key=bool) if emptychar]

data = [int(calories) if calories != '' else '' for calories in data]
data = [sum(list(calories)) for emptychar, calories in groupby(data, key=bool) if emptychar]

## test 

solution_phase1_test_d1 = max(data_test)
print(f"solution {Fore.BLUE}day 1{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d1}{Style.RESET_ALL}")

## submission 

solution_phase1_d1 = max(data)
print(f"solution {Fore.BLUE}day 1{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d1}{Style.RESET_ALL} ⭐")

# phase 2

data_test.sort()
data.sort()

## test 

solution_phase2_test_d2 = sum(data_test[-3:])
print(f"solution {Fore.BLUE}day 1{Style.RESET_ALL} phase 2 test : {Fore.RED}{solution_phase2_test_d2}{Style.RESET_ALL}")

## submission 

solution_phase2_d2 = sum(data[-3:])
print(f"solution {Fore.BLUE}day 1{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d2}{Style.RESET_ALL} ⭐")
