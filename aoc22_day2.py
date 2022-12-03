# AOC 2022 - DAY 2

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 2{Style.RESET_ALL}")

# load data test
with open('./input/input_day2_test.txt') as f:
    data_test = [tuple(s.split(' ')) for s in f.read().split('\n')]

# load data complete 
with open('./input/input_day2.txt') as f:
    data = [tuple(s.split(' ')) for s in f.read().split('\n')]

# phase 1



score = {
    ('A', 'X'): 3 + 1,
    ('A', 'Y'): 6 + 2,
    ('A', 'Z'): 0 + 3,
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,
    ('C', 'X'): 6 + 1,
    ('C', 'Y'): 0 + 2,
    ('C', 'Z'): 3 + 3,
}

scores_test = [score[fight] for fight in data_test]
scores = [score[fight] for fight in data]

## test 

solution_phase1_test_d2 = sum(scores_test)
print(f"solution {Fore.BLUE}day 2{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d2}{Style.RESET_ALL}")

## submission 

solution_phase1_d2= sum(scores)
print(f"solution {Fore.BLUE}day 2{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d2}{Style.RESET_ALL} ⭐")

# phase 2

change_strategy = {
    ('A', 'X'):('A', 'Z'),
    ('A', 'Y'):('A', 'X'),
    ('A', 'Z'):('A', 'Y'),
    ('B', 'X'):('B', 'X'),
    ('B', 'Y'):('B', 'Y'),
    ('B', 'Z'):('B', 'Z'),
    ('C', 'X'):('C', 'Y'),
    ('C', 'Y'):('C', 'Z'),
    ('C', 'Z'):('C', 'X'),
}

data_test_changed = [change_strategy[fight] for fight in data_test]
scores_test_phase2 = [score[fight] for fight in data_test_changed]

data_changed = [change_strategy[fight] for fight in data]
scores_phase2 = [score[fight] for fight in data_changed]

## test 

solution_phase2_test_d2 = sum(scores_test_phase2)
print(f"solution {Fore.BLUE}day 2{Style.RESET_ALL} phase 2 test : {Fore.RED}{solution_phase2_test_d2}{Style.RESET_ALL}")

## submission 

solution_phase2_d2 = sum(scores_phase2)
print(f"solution {Fore.BLUE}day 2{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d2}{Style.RESET_ALL} ⭐")
