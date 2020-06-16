LF = '\n'
BLACK, WHITE = '#', '_'
TO_NUMBER = BLACK + WHITE + WHITE

def add_sentinels(grid: [str]) -> [str]:
    size = len(grid[0])
    sentinel_grid = [BLACK + row + BLACK for row in grid]
    sentinel_grid.append(BLACK * (size + 2))
    sentinel_grid.insert(0, BLACK * (size + 2))
    return sentinel_grid

def clue_numbers(grid: [str], orientation = 'ACROSS') -> [str]:
    width = len(grid[0])
    one_line_grid = ''.join(grid)
    start = 0
    clue_starts = []
    at = one_line_grid.find(TO_NUMBER, start)
    while at != -1:
        if orientation == 'ACROSS':
            clue_starts.append(divmod(at + 1, width))
        else:
            clue_starts.append(divmod(at + 1, width)[::-1])
        start = at + 1
        at = one_line_grid.find(TO_NUMBER, start)
    return clue_starts

new_grid = add_sentinels([line.strip() for line in open("cwd.txt")])
clues_across = clue_numbers(new_grid)
clues_down = clue_numbers([''.join(x) for x in zip(*new_grid)], 'DOWN')
clues = list(sorted(set(clues_across) | set(clues_down)))
print(clues)
