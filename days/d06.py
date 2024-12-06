import time


def d06():

    lines = open(f"inputs\\d06_example.txt").read().strip().split("\n")
    map = [list(line) for line in lines]

    sum_part1 = 0
    sum_part2 = 0
    walked_distance = 0
    turn_points = []
    possible_loop_positions = []

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = 0
    position = (0, 0)

    def detect_obstacle(map, position, directions, direction):
        row, column = position
        dx, dy = directions[direction]
        if map[row + dy][column + dx] == '#':
            return True
        return False

    def detect_end_of_map(map, position):
        row, column = position
        if row <= 0 or row >= len(map) - 1 or column <= 0 or column >= len(map[0]) - 1:
            return True
        return False
    
    def update_position(position, directions, direction):
        row, column = position
        dx, dy = directions[direction]
        return (row + dy, column + dx)
    
    def print_map(map):
        for row in range(len(map)):
            for column in range(len(map[0])):
                print(map[row][column], end="")
            print()
    
    def show_progress(map, speed):
        print(f"Current position: {position}")
        print_map(map)
        time.sleep(speed)

    def is_path_clear(map, start_point, end_point):
        start_row, start_column = start_point
        end_row, end_column = end_point
        
        if start_row == end_row:
            col_range = range(min(start_column, end_column) + 1, max(start_column, end_column))
            for column in col_range:
                if map[start_row][column] == '#':
                    return False
        elif start_column == end_column:
            row_range = range(min(start_row, end_row) + 1, max(start_row, end_row))
            for row in row_range:
                if map[row][start_column] == '#':
                    return False
        else:
            return False
        return True

    for row in range(len(map)):
        for column in range(len(map[0])):
            print(map[row][column], end="")
            if map[row][column] == '^':
                position = (row, column)
        print()
    end_of_map = False
    while not end_of_map:
        if detect_obstacle(map, position, directions, direction):
            direction  = (direction + 1) % len(directions)
            turn_points.append(position)
        row, column = position
        map[row][column] = 'X'
        walked_distance += 1
        # show_progress(map, 0.5)
        position = update_position(position, directions, direction)
        end_of_map = detect_end_of_map(map, position)
    
    row, column = position
    map[row][column] = 'X'
    print()
    print_map(map)
    print(f"End was reached at {position}")

    for row in range(len(map)):
        for column in range(len(map[0])):
            if map[row][column] == 'X':
                sum_part1 += 1

    for i, turn in enumerate(turn_points[2:]):
        print(i)
        c_point = turn
        a_point = turn_points[i]
        if(i % 2 == 0):
            d_point = (c_point[0], a_point[1])
        else:
            d_point = (a_point[0], c_point[1])
        block_position = update_position(d_point, directions, (i - 1) % len(directions))
        print(f"C: {c_point} | A: {a_point} | D: {d_point} | Block: {block_position}")
        print()
        
        if is_path_clear(map, c_point, d_point):
            possible_loop_positions.append(block_position)
            map[block_position[0]][block_position[1]] = i

    print()
    print_map(map)
    print()
    print(turn_points)
    print(possible_loop_positions)
    print(f"Part 1: {sum_part1}")
    print(f"Part 2: {len(possible_loop_positions)}")

def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
