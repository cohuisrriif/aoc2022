# AOC 2022 - DAY 10

# load library 
from colorama import Fore
from colorama import Style
from pprint import pprint

print(f"{Fore.GREEN}ADVENT OF CODE - DAY 10{Style.RESET_ALL}")

# load data test
with open('./input/input_day10_test.txt') as f:
    data_test = f.read().split('\n')
    
# load data complete 
with open('./input/input_day10.txt') as f:
    data = f.read().split('\n')

def parsedata(x):
    y = x.split(' ')
    if len(y) == 1:
        return((y[0],))
    else:
        return((y[0], int(y[1])))

# phase 1

def solution_phase1(data):
    x = 1
    cycle = 0
    scores = []
    signals = [parsedata(x) for x in data]
    for signal in signals:
        cycle += 1
        if signal[0] == "noop":
            scores.append((cycle, x*cycle))
        else:
            scores.append((cycle, x*cycle))
            cycle += 1
            scores.append((cycle, x*cycle))
            x = x + signal[1]
    strength = sum([x[1] for x in scores if x[0] in (20, 60, 100, 140, 180, 220)])  
    return(strength)

## test 

solution_phase1_test_d10 = solution_phase1(data_test)
print(f"solution {Fore.BLUE}day 10{Style.RESET_ALL} phase 1 test : {Fore.RED}{solution_phase1_test_d10}{Style.RESET_ALL}")

## submission 

solution_phase1_d10 = solution_phase1(data)
print(f"solution {Fore.BLUE}day 10{Style.RESET_ALL} phase 1      : {Fore.RED}{solution_phase1_d10}{Style.RESET_ALL} ⭐")

"""
signals = [parsedata(x) for x in data]

sprite = "###....................................."
sprite = list(sprite)

print(f"Sprite position:  {''.join(sprite)}")
print(" ")

cycle = 0
position = 0
CRT = []
x = 1

for signal in signals:
        
        cycle += 1
        CRT.append(sprite[position % 40])
        
        if signal[0] == "noop":
            
            print(f"Start cycle  {cycle}: begin executing noop")
            print(f"During cycle {cycle}: CRT draws pixel in position {position}")
            #print(f"Current CRT row: {''.join(CRT)}")
            print("Current CRT row:")
            print(f"End of cycle {cycle}: finish executing noop")
            print(f" ")
            
            position += 1
            
        else:
            
            print(f"Start cycle   {cycle}: begin executing {signal[0]+' '+str(signal[1])}")
            print(f"During cycle  {cycle}: CRT draws pixel in position {position}")
            #print(f"Current CRT row: {''.join(CRT)}")
            print("Current CRT row:")
            print(f" ")
            
            x = x + signal[1]
            
            position += 1
            
            CRT.append(sprite[position % 40])

            print(x)
            
            sprite = ['.' for i in range(len(sprite))]
            sprite[(x-1) % 40] = "#"
            sprite[x % 40] = "#"
            sprite[(x+1) % 40] = "#"              
            
            cycle += 1
            
            print(f"During cycle  {cycle}: CRT draws pixel in position {position}")
            #print(f"Current CRT row: {''.join(CRT)}")
            print("Current CRT row:")
            print(f"End of cycle  {cycle}: finish executing {signal[0]+' '+str(signal[1])} (Register X is now {x})")
            print(f"Sprite position: {''.join(sprite)}")
            print(f" ")
            
            position += 1

print("-------------- CRT SCREEN----------------------------")
print(''.join(CRT[0:40]))
print(''.join(CRT[40:80]))
print(''.join(CRT[80:120]))
print(''.join(CRT[120:160]))
print(''.join(CRT[160:200]))
print(''.join(CRT[200:240]))
print("-------------- CRT SCREEN----------------------------")

"""

# phase 2

def solution_phase2(data):
    
    signals = [parsedata(x) for x in data]
    sprite = "###....................................."
    sprite = list(sprite)
    cycle = 0
    position = 0
    CRT = []
    x = 1

    for signal in signals:
        cycle += 1
        CRT.append(sprite[position % 40])        
        if signal[0] == "noop":
            position += 1
        else:
            x = x + signal[1]
            position += 1
            CRT.append(sprite[position % 40])
            sprite = ['.' for i in range(len(sprite))]
            sprite[(x-1) % 40] = "#"
            sprite[x % 40] = "#"
            sprite[(x+1) % 40] = "#"              
            cycle += 1
            position += 1

    print(f"{Fore.RED}-------------- CRT SCREEN--------------------{Style.RESET_ALL}")
    print(f"{Fore.RED}{''.join(CRT[0:40])}{Style.RESET_ALL}")
    print(f"{Fore.RED}{''.join(CRT[40:80])}{Style.RESET_ALL}")
    print(f"{Fore.RED}{''.join(CRT[80:120])}{Style.RESET_ALL}")
    print(f"{Fore.RED}{''.join(CRT[120:160])}{Style.RESET_ALL}")
    print(f"{Fore.RED}{''.join(CRT[160:200])}{Style.RESET_ALL}")
    print(f"{Fore.RED}{''.join(CRT[200:240])}{Style.RESET_ALL}")
    print(f"{Fore.RED}-------------- CRT SCREEN---------------------{Style.RESET_ALL}")
    
    return('')

## test 
print(f"solution {Fore.BLUE}day 10{Style.RESET_ALL} test phase 2 :")
solution_phase2(data_test)
print("⭐")

## submission 
print(f"solution {Fore.BLUE}day 10{Style.RESET_ALL} phase 2      :")
solution_phase2(data)
print("⭐")