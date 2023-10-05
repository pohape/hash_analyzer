from argparse import ArgumentParser

from colorama import Back, Style
import functions

if __name__ != "__main__":
    quit()

parser = ArgumentParser()
parser.add_argument("-f", "--file", default=None)
parser.add_argument("-b", "--bet", default=None)
parser.add_argument("-a", "--stake", default=None)
parser.add_argument("-t", "--target", default=None)
parser.add_argument("-s", "--start-balance", default=None)
args = parser.parse_args()

dataset = functions.load_dataset(args.file)

if args.bet is None:
    print("Please specify --bet, for example --bet=1.01")
    quit()
elif args.stake is None:
    print("Please specify --bet-amount, for example --bet-amount=10")
    quit()
elif args.target is None:
    print("Please specify --target, for example --target=1")
    quit()
elif args.start_balance is None:
    print("Please specify --start-balance, for example --start-balance=100")
    quit()

balance = round(float(args.start_balance), 2)
target = round(float(args.target), 2)
stake = round(float(args.stake), 2)
bet = round(float(args.bet), 2)

current_bet = None

for line in dataset:
    if current_bet is not None:
        if line[1] >= current_bet:
            balance = round(balance + stake*current_bet, 2)
            print("{}We win, the number is {}, our stake was ${}, balance now: ${}.{}".format(
                Back.GREEN,
                line[1],
                stake,
                balance,
                Style.RESET_ALL
            ))
        else:
            print("{}We lost, the number is {}, our stake was ${}, balance now: ${}.{}".format(
                Back.RED,
                line[1],
                stake,
                balance,
                Style.RESET_ALL
            ))
        current_bet = None

    if line[1] == target:
        if balance < stake:
            print("Balance {} is less than the bet amount: {}, so we quit.".format(
                balance,
                stake
            ))
            quit()

        print("Our balance is ${}, last number is {}, so we stake ${}.".format(
            balance,
            line[1],
            stake
        ))
        balance -= stake
        current_bet = bet
