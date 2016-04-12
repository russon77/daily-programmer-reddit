

def is_magic(grid):
    """
    compute whether the input grid is a magic square: i.e. each row, column and major diagonal adds up to 15
    :param grid: input grid
    :return: boolean
    """
    n = len(grid)
    target = n * (n**2 + 1) / 2

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

    for res in map(is_magic, tests):
        print(res)

