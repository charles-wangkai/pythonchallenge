#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/rock/arecibo.html
# A: http://www.pythonchallenge.com/pc/rock/beer.html

import functools
import urllib.request
import webbrowser
import PC_Util

def search_partitions(partitions, size, remain, partition):
    if len(partition) == size:
        if remain == 0:
            partitions.append(list(partition))
        return
    
    for i in range(remain + 1):
        partition.append(i)
        search_partitions(partitions, size, remain - i, partition)
        del partition[-1]

@functools.lru_cache(maxsize=None)
def find_partitions(size, n):
    partitions = []
    search_partitions(partitions, size, n, [])
    return partitions

@functools.lru_cache(maxsize=None)
def build_candidates(size, numbers):
    spaces = [0] + [1] * (len(numbers) - 1) + [0]
    remain_space = size - sum(numbers) - sum(spaces)
    
    candidates = []
    for partition in find_partitions(len(spaces), remain_space):
        candidate = []
        for i in range(len(spaces)):
            candidate += [False] * (spaces[i] + partition[i])
            if i != len(spaces) - 1:
                candidate += [True] * numbers[i]
        candidates.append(candidate)
    return candidates

def find_same_value(candidates, index):
    for i in range(1, len(candidates)):
        if candidates[i - 1][index] != candidates[i][index]:
            return None
    return candidates[0][index]

def remove_candidates(candidates, index, value):
    i = 0
    while i < len(candidates):
        if candidates[i][index] == value:
            del candidates[i]
        else:
            i += 1

def simplify(board, row_candidates_list, col_candidates_list):
    size = len(board)
    while True:
        changed = False
        for r in range(size):
            for c in range(size):
                if board[r][c] != None:
                    continue
                
                same_value = find_same_value(row_candidates_list[r], c)
                if same_value != None:
                    changed = True
                    board[r][c] = same_value
                    remove_candidates(col_candidates_list[c], r, not same_value)
                    continue
                
                same_value = find_same_value(col_candidates_list[c], r)
                if same_value != None:
                    changed = True
                    board[r][c] = same_value
                    remove_candidates(row_candidates_list[r], c, not same_value)
        if not changed:
            break

def show(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            print('#' if board[i][j] else ' ', end='')
        print()
    print()
    
def solve_etch_a_sketch(url):
    txt_content = urllib.request.urlopen(url).read().decode()
    numbers_list = list(map(lambda line: tuple(map(int, line.split())), filter(lambda line: line and not line.startswith('#'), txt_content.splitlines())))
    
    size = numbers_list[0][0]
    board = [[None] * size for _ in range(size)]
    
    row_numbers_list, col_numbers_list = numbers_list[1:size + 1], numbers_list[size + 1:]
    
    row_candidates_list = [list(build_candidates(size, row_numbers_list[i])) for i in range(size)]
    col_candidates_list = [list(build_candidates(size, col_numbers_list[i])) for i in range(size)]

    simplify(board, row_candidates_list, col_candidates_list)
    
    show(board)

def main():
    PC_Util.configure_auth()
    
    solve_etch_a_sketch('http://www.pythonchallenge.com/pc/rock/warmup.txt')
    solve_etch_a_sketch('http://www.pythonchallenge.com/pc/rock/up.txt')
    
    webbrowser.open('http://www.gnu.org/philosophy/free-sw.en.html')

if __name__ == '__main__':
    main()
