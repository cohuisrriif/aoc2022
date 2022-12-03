# AOC 2022 - DAY 3

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint
import string

# load data test
with open('./input/input_day3_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day3.txt') as f:
    data = f.read().split('\n')

# phase 1

def getitempriority(item):
    list_of_letters = list(string.ascii_lowercase + string.ascii_uppercase)
    priority = list_of_letters.index(item) + 1
    return(priority)

def getcommonitem(rucksack):
    compartiment1 = set(rucksack[:int(len(rucksack)/2)])
    compartiment2 = set(rucksack[int(len(rucksack)/2):])
    return(compartiment1.intersection(compartiment2).pop())

## test 

solution_phase1_test_d3 = sum([getitempriority(getcommonitem(rucksack)) for rucksack in data_test])
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d3}{Style.RESET_ALL}")

## submission 

solution_phase1_d3 = sum([getitempriority(getcommonitem(rucksack)) for rucksack in data])
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d3}{Style.RESET_ALL} ⭐")

# phase 2

def getcommonitemV2(rucksacks):
    r1 = set(rucksacks[0])
    r2 = set(rucksacks[1])
    r3 = set(rucksacks[2])
    item = r1.intersection(r2).intersection(r3).pop()
    return(item)

## test 

solution_phase2_test_d3 = sum([getitempriority(getcommonitemV2(data_test[r:r+3])) for r in range(0, len(data_test), 3)])
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d3}{Style.RESET_ALL}")

## submission 

solution_phase2_d3 = sum([getitempriority(getcommonitemV2(data[r:r+3])) for r in range(0, len(data), 3)])
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d3}{Style.RESET_ALL} ⭐")


