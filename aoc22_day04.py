# AOC 2022 - DAY 4 

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 4{Style.RESET_ALL}")

# load data test
with open('./input/input_day4_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day4.txt') as f:
    data = f.read().split('\n')

# phase 1

def assignement(rawdata):
    ass_elf1, ass_elf2 = rawdata.split(',')
    ass_elf1_range = [int(x) for x in ass_elf1.split('-')]
    ass_elf2_range = [int(x) for x in ass_elf2.split('-')]
    ass_elf1 = set(range(min(ass_elf1_range), max(ass_elf1_range)+1))
    ass_elf2 = set(range(min(ass_elf2_range), max(ass_elf2_range)+1))
    return(ass_elf1, ass_elf2)

def overlap(assignements):
    if assignements[0].issubset(assignements[1]) or assignements[1].issubset(assignements[0]):
        return(True)
    else:
        return(False)
    
assignements_test = [assignement(rawdata) for rawdata in data_test]
overlaped_test = [overlap(ids) for ids in assignements_test]

assignements = [assignement(rawdata) for rawdata in data]
overlaped = [overlap(ids) for ids in assignements]

## test 

solution_phase1_test_d4 = sum(overlaped_test)
print(f"solution {Fore.BLUE}day 4{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d4}{Style.RESET_ALL}")

## submission 

solution_phase1_d4 = sum(overlaped)
print(f"solution {Fore.BLUE}day 4{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d4}{Style.RESET_ALL} ⭐")

# phase 2

def overlapV2(assignements):
    if assignements[0].intersection(assignements[1]):
        return(True)
    else:
        return(False)

assignements_test = [assignement(rawdata) for rawdata in data_test]
overlaped_test = [overlapV2(ids) for ids in assignements_test]

assignements = [assignement(rawdata) for rawdata in data]
overlaped = [overlapV2(ids) for ids in assignements]

## test 

solution_phase2_test_d4 = sum(overlaped_test)
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d4}{Style.RESET_ALL}")

## submission 

solution_phase2_d4 = sum(overlaped)
print(f"solution {Fore.BLUE}day 3{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d4}{Style.RESET_ALL} ⭐")


