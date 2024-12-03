

def d01():
    lines = open(f"inputs\\d01.txt").read().strip().split("\n")

    left_list = []
    right_list = []
    distances = 0
    similarity_score = 0

    for line in lines:
        numbers = line.split()
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))
    
    left_list.sort()
    right_list.sort()

    for left_num, right_num in zip(left_list, right_list):
        distances += abs(left_num - right_num)

    print(f"Part 1: {distances}")

    for left_num in left_list:
        similarity_score += (left_num * right_list.count(left_num))
    
    print(f"Part 2: {similarity_score}")


def _test():
     print("File shall not be run standalone")
     assert int('1') == 1

if __name__ == '__main__':
    _test()