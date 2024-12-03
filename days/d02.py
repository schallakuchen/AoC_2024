

def d02():
    lines = open(f"inputs\\d02.txt").read().strip().split("\n")

    reports = [list(map(int, line.split())) for line in lines]

    num_safe_reports = 0
    num_tolerated_reports = 0
    
    for report in reports:
        increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
        decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
        valid_difference = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
        
        if (increasing or decreasing) and valid_difference:
            num_safe_reports += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                increasing = all(modified_report[j] < modified_report[j + 1] for j in range(len(modified_report) - 1))
                decreasing = all(modified_report[j] > modified_report[j + 1] for j in range(len(modified_report) - 1))
                valid_difference = all(1 <= abs(modified_report[j] - modified_report[j + 1]) <= 3 for j in range(len(modified_report) - 1))
                if (increasing or decreasing) and valid_difference:
                    num_tolerated_reports += 1
                    break

    print(f"Part 1: {num_safe_reports}")
    print(f"Part 2: {num_safe_reports + num_tolerated_reports}")


def _test():
    print("File shall not be run standalone")
    assert int('1') == 1


if __name__ == '__main__':
    _test()
