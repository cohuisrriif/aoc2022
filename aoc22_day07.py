# AOC 2022 - DAY 7

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 7{Style.RESET_ALL}")

# load data test
with open('./input/input_day7_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day7.txt') as f:
    data = f.read().split('\n')

# phase 1




folders = []
files = []

i = 0 
while i < len(data):
    if '$ cd ' in data[i] and '$ cd .' not in data[i]:
        folders.append({"type":"dir", "name":data[i].split(' ')[2], "content": []})
    if data[i].split(' ')[0].isdigit():
        files.append({"type":"file", "name":data[i].split(' ')[1], "size": int(data[i].split(' ')[0])})
    i = i + 1

pprint(folders)
pprint(files)














"""
    

def solution_phase1(data):
    return(None)

## test 

solution_phase1_test_d7 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 7{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d7}{Style.RESET_ALL}")

## submission 

solution_phase1_d7 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 7{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d7}{Style.RESET_ALL} ⭐")

# phase 2

def solution_phase2(data):
    return(None)

## test 

solution_phase2_test_d7 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 7{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d7}{Style.RESET_ALL}")

## submission 

solution_phase2_d7 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 7{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d7}{Style.RESET_ALL} ⭐")

"""
