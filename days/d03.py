import re


def d03():
    input = open(f"inputs\\d03.txt").read().strip()
    
    sum_part1 = 0
    sum_part2 = 0

    # Part 1
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(mul_pattern, input)
    #print(matches)

    for match in matches:
        left_num, right_num = map(int, match)
        sum_part1 += left_num * right_num

    # Part 2
    mul_enabled = True
    enabler = "do()"
    disabler = "don't()"
    instruction = "mul"
    
    i = 0
    while i < len(input):
        if input[i:i+len(enabler)] == enabler:
            mul_enabled = True
            i += len(enabler)
        elif input[i:i+len(disabler)] == disabler:
            mul_enabled = False
            i += len(disabler)
        elif input[i:i+len(instruction)] == instruction:
            if mul_enabled:
                match = re.match(mul_pattern, input[i:])
                if match:
                    left_num, right_num = map(int, match.groups())
                    sum_part2 += left_num * right_num
                    i += len(match.group(0))
                else:
                    i += 1
            else:
                i += len(instruction)
        else:
            i += 1

    print(f"Part1: {sum_part1}")
    print(f"Part2: {sum_part2}")


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
