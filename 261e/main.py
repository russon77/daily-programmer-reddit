import functools


def is_magic(grid):
    """
    compute whether the input grid is a magic square: i.e. each row, column and major diagonal adds up to 15
    :param grid: input grid
    :return: boolean
    """
    n = len(grid)
    target = int(n * (n**2 + 1) / 2)

    # check row-wise
    for row in grid:
        if sum(row) != target:
            return False

    # check column wise
    for col in range(0, len(grid)):
        if sum([grid[row][col] for row in range(0, len(grid[col]))]) != target:
            return False

    # check diagonals
    if sum([grid[k][k] for k in range(0, len(grid))]) != target:
        return False

    if sum([grid[k][len(grid) - 1 - k] for k in range(0, len(grid))]) != target:
        return False

    return True


def all_unique(grid):
    """
    test whether every entry in this grid is unique, and return accordinly
    :param grid: input rowxcol grid
    :return: boolean: true if every entry is unique
    """
    entries = {}
    for row in grid:
        for num in row:
            if num in entries:
                return False

            entries[num] = True

    return True


def possibly_magic(grid):
    """
    given a grid of Rows x Cols, such that Rows = (Cols - 1): return True if the grid could be a magic square and False
    otherwise
    :param grid: almost-square grid, where # rows = # cols - 1
    :return: boolean
    """
    n = len(grid[0])
    target = int(n * (n ** 2 + 1) / 2)

    last_row = []

    # for each column, find the number missing
    for col in range(0, n):
        val = functools.reduce(lambda x, y: x + y, [grid[row][col] for row in range(0, len(grid))])
        last_row.append(target - val)

    grid.append(last_row)
    if all_unique(grid) and is_magic(grid):
        return True

    return False


if __name__ == '__main__':
    tests = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],  # true
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],  # true
        [[3, 5, 7], [8, 1, 6], [4, 9, 2]],  # false
        [[8, 1, 6], [7, 5, 3], [4, 9, 2]],  # false
        [[11, 24, 7, 20, 3], [4, 12, 25, 8, 16], [17, 5, 13, 21, 9], [10, 18, 1, 14, 22], [23, 6, 19, 2, 15]],  # true
        [[6, 32, 3, 34, 35, 1], [7, 11, 27, 28, 8, 30], [19, 14, 16, 15, 23, 24],
            [18, 20, 22, 21, 17, 13], [25, 29, 10, 9, 26, 12], [36, 5, 33, 4, 2, 31]]  # true
    ]

    tests_possible = [
        [[8, 1, 6], [3, 5, 7]],  # true
        [[3, 5, 7], [8, 1, 6]],  # false
        [[11, 24, 7, 20, 3], [4, 12, 25, 8, 16], [17, 5, 13, 21, 9], [10, 18, 1, 14, 22]],  # true
        [[6, 32, 3, 34, 35, 1], [7, 11, 27, 28, 8, 30], [19, 14, 16, 15, 23, 24],
         [25, 29, 10, 9, 26, 12], [18, 20, 22, 21, 17, 13]]  # false
    ]

    print("Running test: is_magic")
    for res in map(is_magic, tests):
        print(res)

    print("Running test: all_unique")
    for res in map(all_unique, tests):
        print(res)

    print("Running test: possibly_magic")
    for res in map(possibly_magic, tests_possible):
        print(res)

