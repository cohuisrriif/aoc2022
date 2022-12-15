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

# just to help the algorithm to catch all the data
data.append("$ cd ..")
data_test.append("$ cd ..")

# phase 1

"""
def solution_phase1(data):

    folders = []
    files = []

    k = 0
    while k < len(data):
        if '$ cd ' in data[k] and '$ cd .' not in data[k]:
            folders.append({"type":"dir", "name":data[k].split(' ')[2], "content": []})
        if data[k].split(' ')[0].isdigit():
            files.append({"type":"file", "name":data[k].split(' ')[1], "size": int(data[k].split(' ')[0])})
        k = k + 1

    folders = {v['name']:v for v in folders}.values()
    files = {v['name']:v for v in files}.values()

    for folder in folders:
        index = data.index('$ cd ' + folder['name'])
        print(index, folder['name'])
        i = 1
        while ('$ cd ' not in data[index + i] or index + i + 1 == len(data)) and index + i + 1  < len(data):
            if '$ ls' != data[index + i]:
                if 'dir ' in data[index + i]:
                    folder['content'].append({"type":"dir", "name": data[index + i].split(' ')[1], "parent": folder['name']})
                if data[index + i].split(' ')[0].isdigit():
                    folder['content'].append({"type":"file", "name":data[index + i].split(' ')[1], "size": int(data[index + i].split(' ')[0])})
            i = i + 1

    def computesize(folder, folders, size = 0):
        size = size
        for content in folder['content']:
            if content['type'] == 'file':
                size += content['size']
            else:
                children_folder = next(item for item in folders if item["name"] == content['name'])
                size += computesize(children_folder, folders, size = size)
        return(size)

    totalsize = 0
    for folder in folders:
        x = computesize(folder, folders)
        if x < 100001:
            totalsize += x

    return(totalsize)
"""

paths = []
i=0
while i < len(data_test):
    if '$ cd ' in data_test[i]:
        paths.append([data_test[i]])
        i = i + 1
    elif '$ ls' in data_test[i]:
        paths.append([data_test[i]])
        k = 0
        ls_folder = []
        while '$ cd ' not in data_test[i+k]:
            ls_folder.append(data_test[i+k])
            k = k + 1
        paths.append(ls_folder)
        i = i + k
    else:
        i = i + 1
paths = [[y for y in x if y != '$ ls'] for x in paths][:-1]
paths = [x for x in paths if x]
pprint(paths)
















"""
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

solution_phase2_test_d7 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 7{Style.RESET_ALL} test phase 2 : {Fore.RED}{solution_phase2_test_d7}{Style.RESET_ALL}")

## submission

solution_phase2_d7 = solution_phase2(data)
print(f"solution {Fore.BLUE}day 7{Style.RESET_ALL} phase 2      : {Fore.RED}{solution_phase2_d7}{Style.RESET_ALL} ⭐")

"""
