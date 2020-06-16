LF = '\n'
BLACK = '#'
WHITE = '_'
TO_NUMBER = BLACK + WHITE + WHITE

def add_sentinels(grid: [str]) -> [str]:
    size = len(grid[0])
    sentinels = [BLACK + row + BLACK for row in grid]
    sentinels.append(BLACK * (size + 2))
    sentinels.insert(0, BLACK * (size + 2))
    return sentinels

def number(grid: [str]) -> [(int, int)]:
    clue_numbers = set()
    for row, line in enumerate(grid[1:]):
        for col, cell in enumerate(line):
            if line[col - 1: col + 2] == TO_NUMBER:
                clue_numbers.add((row + 1, col))
            if grid[row - 1][col] + grid[row][col] + grid[row + 1][col] == TO_NUMBER:
                clue_numbers.add((row, col))
    return list(sorted(clue_numbers))

new_grid = add_sentinels([line.strip() for line in open("cwd.txt")])
print(number(new_grid))
