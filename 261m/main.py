

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


def apply_permutation(original_list, new_list, p):
    """
    given two lists of the same size, rearrange the new list as a permutation (as defined by p) of the original list
    :param original_list:
    :param new_list:
    :param p:
    :return:
    """
    for i in range(0, len(p)):
        new_list[i] = original_list[p[i]]

    return new_list


def get_permutation(len):
    starting_point = [x for x in range(0, len)]
    yield starting_point

    current = [x for x in range(0, len)]  # placeholder for our current value to change

    while True:
        for x in range(0, len - 1):
            current[x], current[x + 1] = current[x + 1], current[x]  # make the swap

            if current == starting_point:  # exit condition
                return

            yield current


def find_square_by_rearranging(grid):
    new_list = [x for x in grid]

    for permutation in get_permutation(len(grid)):
        new_list = apply_permutation(grid, new_list, permutation)
        if is_magic(new_list):
            return new_list

    return False


if __name__ == '__main__':
    tests = [
        [[15, 14, 1, 4], [12, 6, 9, 7], [2, 11, 8, 13], [5, 3, 16, 10]],
        [[20, 19, 38, 30, 31, 36, 64, 22],
         [8, 16, 61, 53, 1, 55, 32, 34],
         [33, 60, 25, 9, 26, 50, 13, 44],
         [37, 59, 51, 4, 41, 6, 23, 39],
         [58, 35, 2, 48, 10, 40, 46, 21],
         [62, 11, 54, 47, 45, 7, 5, 29],
         [18, 57, 17, 27, 63, 14, 49, 15],
         [24, 3, 12, 42, 43, 52, 28, 56]]
    ]

    # print("Running test: get_permutation")
    # for res in get_permutation(8):
    #     print(res)

    for i in range(2, 10):
        print(str(i) + ": " + str(len([x for x in get_permutation(i)])))

    # print("Running test: all_unique")
    # for res in map(find_square_by_rearranging, tests):
    #     print(res)

