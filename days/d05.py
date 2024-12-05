

def d05():
    lines = open(f"inputs\\d05.txt").read().strip()

    rules_raw, page_lists_raw = lines.split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_raw.splitlines()]
    page_lists = [list(map(int, page_list.split(','))) for page_list in page_lists_raw.splitlines()]

    # print(rules)
    # print(page_lists)

    valid_page_lists = []
    invalid_page_lists = []
    corrected_page_lists = []
    sum_part1 = 0
    sum_part2 = 0

    for page_list in page_lists:
        violation = False
        for i, page in enumerate(page_list):
            after_list = []
            for rule in rules:
                if rule[0] == page:
                    after_list.append(rule[1])
            # print(f"After List for {page}: {after_list}")
            for after_num in after_list:
                if after_num in page_list[i+1:]:
                    continue
                elif after_num in page_list:
                    violation = True
                    break
        if not violation:
            valid_page_lists.append(page_list)
            sum_part1 += page_list[len(page_list)//2]
        else:
            invalid_page_lists.append(page_list)
            changed = True
            while changed:
                changed = False
                for i, page in enumerate(page_list):
                    after_list = []
                    for rule in rules:
                        if rule[0] == page:
                            after_list.append(rule[1])
                    for after_num in after_list:
                        if after_num in page_list[:i]:
                            page_list.remove(after_num)
                            page_list.insert(i + 1, after_num)
                            changed = True
            corrected_page_lists.append(page_list)
            sum_part2 += page_list[len(page_list) // 2]
            
    # print(valid_page_lists)
    # print(invalid_page_lists)
    # print(corrected_page_lists)

    print(f"Part1: {sum_part1}")
    print(f"Part2: {sum_part2}")

def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
