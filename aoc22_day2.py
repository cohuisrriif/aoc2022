# AOC 2022 - DAY 2

"""
ennemy --  
A : rock
B : paper
C : scissors 
me -- 
X : rock
Y : paper
Z : scissors 

my_score = my_hand_score + outcome_score
score_hand = {'X':1,'Y':2,'Z':3}
outcome_score = (draw = 3; lost = 0; win = 6) 
i win if : 
(A, Y) (B, Z) (C, X)
"""

# load data test
with open('./input/input_day2_test.txt') as f:
    data_test = [tuple(s.split(' ')) for s in f.read().split('\n')]

# load data complete 
with open('./input/input_day2.txt') as f:
    data = [tuple(s.split(' ')) for s in f.read().split('\n')]
del data[-1]



# phase 1

## test 

score_hand = {'X':1,'Y':2,'Z':3}

def score(fight):
    # fight[1] is my hand
    if fight in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]:
        my_score = 3 + score_hand[fight[1]]
    elif fight in [('A', 'Y'), ('B', 'Z'), ('C', 'X')]:
        my_score = 6 + score_hand[fight[1]]
    else:
        my_score = 0 + score_hand[fight[1]]
    return(my_score)

scores_test = [score(fight) for fight in data_test]

solution_phase1_test_d2 = sum(scores_test)
print(f'solution day 2 phase 1 test : {solution_phase1_test_d2}')

## submission 

scores = [score(fight) for fight in data]

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
scores_test_phase2 = [score(fight) for fight in data_test_changed]

solution_phase2_test_d2 = sum(scores_test_phase2)
print(f'solution day 2 phase 2 test : {solution_phase2_test_d2}')

## submission 

data_changed = [change_strategy[fight] for fight in data]
scores_phase2 = [score(fight) for fight in data_changed]

solution_phase2_d2 = sum(scores_phase2)
print(f'solution day 2 phase 2 : {solution_phase2_d2}')
