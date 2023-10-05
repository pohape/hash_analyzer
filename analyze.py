from argparse import ArgumentParser
import os


if __name__ != "__main__":
    quit()

parser = ArgumentParser()
parser.add_argument("-f", "--file", default=None)
parser.add_argument("-b", "--bet", default=None)
args = parser.parse_args()


def get_line_by_key(key: int, data: list):
    return data[key] if len(data) > key else None


def get_success_rate_after_specified(data: list, number: float, bet: float):
    after_specified = get_numbers_after_specified(
        data=data,
        number=number
    )

    success = 0
    fail = []

    for (after_specified, first_line, second_line) in after_specified:
        if after_specified > bet:
            success += 1
        else:
            fail.append([first_line, second_line])

    return success / (success + len(fail)) * 100, success, fail


def get_numbers_after_specified(data: list, number: float):
    key = 0
    # results_count = 0

    after = []

    for line in data:
        if line[1] == number:
            # results_count += 1
            next_line = get_line_by_key(key + 1, data)

            if next_line is not None:
                after.append([next_line[1], line, next_line])

        key += 1

    return after


def generate_report(data: list, number: float, bet: float, with_details=True):
    results = get_success_rate_after_specified(
        data=list_of_lines,
        number=1,
        bet=bet
    )

    report = "Bet: {}".format(bet)
    report += "\nSuccess rate: {:.2f}%".format(results[0])

    if with_details is True:
        report += "\nFails: "

        for fail_lines in results[2]:
            report += "\n"

            for fail_line in fail_lines:
                report += '\n'
                report += '\t'.join(str(v) for v in fail_line)

    return report + '\n'


if args.file is None:
    print("Please specify an input file with --file=")
    quit()
elif not os.path.isfile(args.file):
    print(args.file + " file not found")
    quit()

with open(args.file, mode="r") as f:
    list_of_lines = f.readlines()

list_of_lines.reverse()
list_of_lines = [(line.split('\t')[0], float(line.split('\t')[1]))
                 for line in list_of_lines]

bets = []

if args.bet is not None:
    bets = [round(float(args.bet), 2)]
else:
    for bet in range(1, 100):
        bets.append(round(1 + bet/100, 2))

for bet in bets:
    print(generate_report(
        data=list_of_lines,
        number=1,
        bet=bet,
        with_details=False if args.bet is None else True
    ))
