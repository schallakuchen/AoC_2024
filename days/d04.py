

def is_valid(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def search_from(matrix, word, x, y, direction_x, direction_y):
    for distance in range(len(word)):
        next_x = x + distance * direction_x
        next_y = y + distance * direction_y
        if not is_valid(matrix, next_x, next_y) or matrix[next_x][next_y] != word[distance]:
            return False
    return True

def find_occurrences(matrix, word):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    occurrences = []
    
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == word[0]:
                for dx, dy in directions:
                    if search_from(matrix, word, x, y, dx, dy):
                        occurrences.append((x, y, dx, dy))
    return occurrences

def d04():
    lines = open(f"inputs\\d04_example.txt").read().strip().split("\n")
    matrix = [list(line) for line in lines]

    search_word = "XMAS"
    found_positions_part1 = find_occurrences(matrix, search_word)  

    # print(f"Occurrences of {search_word}:")
    # for position in found_positions_part1:
    #     print(f"Start at ({position[0]}, {position[1]}) in direction (dx={position[2]}, dy={position[3]})")

    print(f"Part 1: {len(found_positions_part1)}")


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
