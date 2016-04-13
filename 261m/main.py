from permutations import permutations


def is_magic(grid):
    """
    compute whether the input grid is a magic square: i.e. each row, column and major diagonal adds up to 15
    OPTIMIZATION: as others pointed out in the reddit thread, since we are rearranging rows, we know that
     the sum of each row and column is always correct. therefore, we only need to check diagonals.
    :param grid: input grid
    :return: boolean
    """
    n = len(grid)
    target = int(n * (n**2 + 1) / 2)

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


def num_possible_rearrangements(grid):
    num = 0
    new_list = [x for x in grid]

    for perm in permutations([i for i in range(0, len(grid))]):
        new_list = apply_permutation(grid, new_list, perm)
        if is_magic(new_list):
            num += 1

    return num


if __name__ == '__main__':
    tests = [
        [
            [15, 14, 1, 4],
            [12, 6, 9, 7],
            [2, 11, 8, 13],
            [5, 3, 16, 10]
        ],

        [
            [20, 19, 38, 30, 31, 36, 64, 22],
             [8, 16, 61, 53, 1, 55, 32, 34],
             [33, 60, 25, 9, 26, 50, 13, 44],
             [37, 59, 51, 4, 41, 6, 23, 39],
             [58, 35, 2, 48, 10, 40, 46, 21],
             [62, 11, 54, 47, 45, 7, 5, 29],
             [18, 57, 17, 27, 63, 14, 49, 15],
             [24, 3, 12, 42, 43, 52, 28, 56]
        ],

        [
            [111, 129, 27, 38, 119, 73, 30, 11, 123, 144, 6, 59],
            [33, 22, 118, 102, 51, 121, 79, 132, 15, 50, 42, 105],
            [14, 91, 41, 7, 85, 116, 60, 125, 128, 70, 71, 62],
            [69, 92, 87, 142, 4, 28, 103, 43, 37, 112, 76, 77],
            [136, 84, 115, 55, 137, 97, 17, 32, 13, 35, 16, 133],
            [2, 46, 68, 78, 141, 94, 47, 80, 81, 82, 58, 93],
            [108, 36, 20, 1, 65, 45, 143, 64, 113, 109, 56, 110],
            [99, 18, 12, 49, 100, 114, 72, 66, 107, 5, 138, 90],
            [95, 83, 57, 135, 67, 53, 31, 19, 39, 126, 140, 25],
            [8, 86, 130, 88, 44, 21, 131, 63, 101, 29, 117, 52],
            [89, 61, 75, 48, 54, 74, 23, 96, 104, 98, 124, 24],
            [106, 122, 120, 127, 3, 34, 134, 139, 9, 10, 26, 40]
        ]
    ]

    print("Testing find_square_by_rearranging...")
    for res in map(num_possible_rearrangements, tests):
        print(res)



