# AOC 2022 - DAY 13

# load library
from colorama import Fore
from colorama import Style
from pprint import pprint
from itertools import groupby
import json

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 13{Style.RESET_ALL}")

# load data test
with open('./input/input_day13_test.txt') as f:
    data_test = f.read().split('\n')

# load data complete
with open('./input/input_day13.txt') as f:
    data = f.read().split('\n')

data_test = [tuple(group) for k, group in groupby(data_test, lambda x: x == '') if not k]
data_test = [tuple([json.loads(x) for x in l]) for l in data_test]
data = [tuple(group) for k, group in groupby(data, lambda x: x == '') if not k]
data = [tuple([json.loads(x) for x in l]) for l in data]

def comparison(packets):
    left = packets[0]
    right = packets[1]

    x = type(left)
    y = type(right)

    if x == int and y == int:
        print(f"- Compare {left} vs {right}")
        if left < right or left == right:
            print("- Left side is smaller, so inputs are in the right order")
            return(True)
        else:
            print("- Right side is smaller, so inputs are not in the right order")
            return(False)
    elif x == list and y == list:
        print(f"- Compare {left} vs {right}")
        if len(left) == 0 and len(right) == 0:
            return(True)
        else:
            if comparison((left[0], right[0])):
                if len(left[1:]) == 0 and len(right[1:]) == 0:
                    return(True)
                else:
                    if len(left[1:]) == 0 or len(right[1:]) == 0:
                        return(False)
                    else:
                        return(comparison((left[1:], right[1:])))
            else:
                return(False)

    elif x == int and y == list:
        print(f"- Compare {left} vs {right}")
        left = [left]
        print(f"- Mixed types, conver left to {left} and retry comparison")
        return(comparison((left, right)))
    else:
        print(f"- Compare {left} vs {right}")
        right = [right]
        print(f"- Mixed types, conver left to {right} and retry comparison")
        return(comparison((left, right)))

i = 0
for x in data_test:
    i = i + 1
    print(f"== Pair {i} ==")
    print(f"testing : {x}")
    print(comparison(x))
    print(' ')
    print(' ')

# phase 1

def solution_phase1(data):
    return(None)

## test

solution_phase1_test_d13 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 13{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d13}{Style.RESET_ALL}")

## submission

solution_phase1_d13 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 13{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d13}{Style.RESET_ALL} ⭐")

# phase 2

def solution_phase2(data):
    return(None)

## test

solution_phase2_test_d13 = solution_phase2(data_test)
print(f"solution {Fore.BLUE}day 13{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d13}{Style.RESET_ALL}")

## submission

solution_phase2_d13 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 13{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d13}{Style.RESET_ALL} ⭐")


