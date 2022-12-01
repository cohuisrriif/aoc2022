# AOC 2022 - DAY 1 

from itertools import groupby

# phase 1

## test 
with open('./input_day1_test.txt') as f:
    data = f.read().split('\n')

data_test = [int(calories) if calories != '' else '' for calories in data]
data_test = [sum(list(calories)) for emptychar, calories in groupby(data_test, key=bool) if emptychar]

solution_part1_test = max(data_test)
print(f'solution test part 1 : {solution_part1_test}')

## submission 
with open('./input_day1_1.txt') as f:
    data = f.read().split('\n')
    
data = [int(calories) if calories != '' else '' for calories in data]
data = [sum(list(calories)) for emptychar, calories in groupby(data, key=bool) if emptychar]

solution_part1_day1 = max(data)
print(f'solution day 1 part 1 : {solution_part1_day1}')

# phase 2

## test 
data_test.sort()
solution_part2_test = sum(data_test[-3:])
print(f'solution test part 1 : {solution_part2_test}')

## submission 
data.sort()
solution_part2_day1 = sum(data[-3:])
print(f'solution test part 1 : {solution_part2_day1}')










