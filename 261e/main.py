

def is_magic(grid):
    """
    compute whether the input grid is a magic square: i.e. each row, column and major diagonal adds up to 15
    :param grid: input grid
    :return: boolean
    """
    # check row-wise
    for row in grid:
        if sum(row) != 15:
            return False

    # check column wise
    for col in range(0, len(grid)):
        if sum([grid[row][col] for row in range(0, len(grid[col]))]) != 15:
            return False

    # check diagonals
    if sum([grid[k][k] for k in range(0, len(grid))]) != 15:
        return False

    if sum([grid[k][len(grid) - 1 - k] for k in range(0, len(grid))]) != 15:
        return False

    return True


if __name__ == '__main__':
    tests = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]], # true
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]], # true
        [[3, 5, 7], [8, 1, 6], [4, 9, 2]], # false
        [[8, 1, 6], [7, 5, 3], [4, 9, 2]], # false
    ]

    for res in map(is_magic, tests):
        print(res)

