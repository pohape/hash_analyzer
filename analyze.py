from argparse import ArgumentParser
import functions


if __name__ != "__main__":
    quit()

parser = ArgumentParser()
parser.add_argument("-f", "--file", default=None)
parser.add_argument("-b", "--bet", default=None)
parser.add_argument("-t", "--target", default=None)
args = parser.parse_args()


def get_line_by_key(key: int, dataset: list):
    return dataset[key] if len(dataset) > key else None


def get_success_rate_after_specified(dataset: list, target: float, bet: float):
    after_specified = get_numbers_after_specified(
        dataset=dataset,
        target=target
    )

    success = 0
    fail = []

    for (after_specified, first_line, second_line) in after_specified:
        if after_specified >= bet:
            success += 1
        else:
            fail.append([first_line, second_line])

    if success == 0:
        return 0, success, fail

    return success / (success + len(fail)) * 100, success, fail


def get_numbers_after_specified(dataset: list, target: float):
    key = 0
    after = []

    for line in dataset:
        if line[1] == target:
            next_line = get_line_by_key(key + 1, dataset)

            if next_line is not None:
                after.append([next_line[1], line, next_line])

        key += 1

    return after


def generate_report(dataset: list, target: float, bet: float, with_details=True):
    results = get_success_rate_after_specified(
        dataset=dataset,
        target=target,
        bet=bet
    )

    report = "Bet: {}".format(bet)
    report = "\nTarget: {}".format(target)
    report += "\nSuccess rate: {:.2f}% ({}/{})".format(
        results[0],
        results[1],
        len(results[2])
    )

    if with_details is True:
        if len(results[2]) == 0:
            report += '\nNo fails!'
        else:
            report += "\nFails: "

            for fail_lines in results[2]:
                report += "\n"

                for fail_line in fail_lines:
                    report += '\n'
                    report += '\t'.join(str(v) for v in fail_line)

    return report + '\n'


dataset = functions.load_dataset(args.file)
bets = []

if args.target is not None:
    target = round(float(args.target), 2)
else:
    target = 1

if args.bet is not None:
    bets = [round(float(args.bet), 2)]
else:
    for bet in range(1, 100):
        bets.append(round(1 + bet/100, 2))

for bet in bets:
    print(generate_report(
        dataset=dataset,
        target=target,
        bet=bet,
        with_details=False if args.bet is None else True
    ))
