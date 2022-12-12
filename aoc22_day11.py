# AOC 2022 - DAY 11

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint
from itertools import groupby
from math import floor
from fractions import Fraction
import time

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 11{Style.RESET_ALL}")

# load data test
with open('./input/input_day11_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day11.txt') as f:
    data = f.read().split('\n')
    
def parsedata(x):
    result = {
        "index":None,
        "items":[], 
        "operation":None, 
        "test":None,
        "index_true":None,
        "index_false":None,
        "count":0}
    result["index"] = int(x[0].replace(':', '').split(' ')[1])
    result["items"] = [int(y) for y in x[1].split(':')[1].split(',')]
    result["test"] = [int(y) for y in x[3].split('by')[1].split(',')][0]
    result["index_true"] = [int(y) for y in x[4].split('monkey')[1].split(',')][0]
    result["index_false"] = [int(y) for y in x[5].split('monkey')[1].split(',')][0]
    result["operation"] = [y for y in x[2].split('=')[1].split(' ') if y][1:] 
    return(result)



# phase 1

def solution_phase1(data):
    data = [x.strip() for x in data] 
    data =[list(group) for k, group in groupby(data, lambda x: x == '') if not k]
    monkeys = [parsedata(x) for x in data]
    
    i = 0
    while i < 20:
        for monkey in monkeys:
            monkey['count'] += len(monkey['items'])
            if monkey["items"]:
                if monkey["operation"][0] == "+":
                    if monkey["operation"][1] == "old":
                        monkey["items"] = [x + x for x in monkey["items"]] 
                    else:
                        monkey["items"] = [x + int(monkey["operation"][1]) for x in monkey["items"]] 
                else:
                    if monkey["operation"][1] == "old":
                        monkey["items"] = [x ** 2 for x in monkey["items"]] 
                    else:
                        monkey["items"] = [x * int(monkey["operation"][1]) for x in monkey["items"]]      
                monkey["items"] = [floor(x/3) for x in monkey["items"]]                               
                monkeys[monkey['index_true']]['items'] += [x for x in monkey["items"] if x % monkey["test"] == 0]
                monkeys[monkey['index_false']]['items'] += [x for x in monkey["items"] if x % monkey["test"] != 0]
                monkey["items"] = []     
        i = i + 1
    counts = sorted([monkey['count'] for monkey in monkeys])
    monkey_business = counts[-1] * counts[-2]
    return(monkey_business)

## test 

solution_phase1_test_d11 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 11{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d11}{Style.RESET_ALL}")

## submission 

solution_phase1_d11 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 11{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d11}{Style.RESET_ALL} ⭐")

# phase 2

def solution_phase2(data):
    data = [x.strip() for x in data] 
    data =[list(group) for k, group in groupby(data, lambda x: x == '') if not k]
    monkeys = [parsedata(x) for x in data]
    
    worry_divider = 1
    for monkey in monkeys:
        worry_divider *= monkey['test'] 
    i = 0
    while i < 10000:
        for monkey in monkeys:
            monkey['count'] += len(monkey['items'])
            if monkey["items"]:
                if monkey["operation"][0] == "+":
                    if monkey["operation"][1] == "old":
                        monkey["items"] = [x + x for x in monkey["items"]] 
                    else:
                        monkey["items"] = [x + int(monkey["operation"][1]) for x in monkey["items"]] 
                else:
                    if monkey["operation"][1] == "old":
                        monkey["items"] = [x * x for x in monkey["items"]] 
                    else:
                        monkey["items"] = [x * int(monkey["operation"][1]) for x in monkey["items"]]   
                monkey["items"] = [x % worry_divider for x in monkey["items"]] 
                monkeys[monkey['index_true']]['items'] += [x for x in monkey["items"] if x % monkey["test"] == 0]
                monkeys[monkey['index_false']]['items'] += [x for x in monkey["items"] if x % monkey["test"] != 0]
                monkey["items"] = []
        i = i + 1
    counts = sorted([monkey['count'] for monkey in monkeys])
    monkey_business = counts[-1] * counts[-2]
    return(monkey_business)

## test 

solution_phase2_test_d11 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 11{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d11}{Style.RESET_ALL}")

## submission 

solution_phase2_d11 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 11{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d11}{Style.RESET_ALL} ⭐")


