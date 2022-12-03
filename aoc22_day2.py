# AOC 2022 - DAY 2

# load data test
with open('./input/input_day2_test.txt') as f:
    data_test = [tuple(s.split(' ')) for s in f.read().split('\n')]

# load data complete 
with open('./input/input_day2.txt') as f:
    data = [tuple(s.split(' ')) for s in f.read().split('\n')]
del data[-1]

# phase 1

## test 

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

solution_phase1_test_d2 = sum(scores_test)
print(f'solution day 2 phase 1 test : {solution_phase1_test_d2}')

## submission 

scores = [score[fight] for fight in data]

solution_phase1_d2= sum(scores)
print(f'solution day 2 phase 1 : {solution_phase1_d2}')

# phase 2

"""
A : rock
B : paper
C : scissors 

X : i should lose 
Y : i need to draw
Z : i need to win
"""

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

## test 

data_test_changed = [change_strategy[fight] for fight in data_test]
scores_test_phase2 = [score[fight] for fight in data_test_changed]

solution_phase2_test_d2 = sum(scores_test_phase2)
print(f'solution day 2 phase 2 test : {solution_phase2_test_d2}')

## submission 

data_changed = [change_strategy[fight] for fight in data]
scores_phase2 = [score[fight] for fight in data_changed]

solution_phase2_d2 = sum(scores_phase2)
print(f'solution day 2 phase 2 : {solution_phase2_d2}')
