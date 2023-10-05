import os


def load_dataset(path: str):
    if path is None:
        print("Please specify an input file with --file=")
        quit()
    elif not os.path.isfile(path):
        print(path + " file not found")
        quit()

    with open(path, mode="r") as f:
        list_of_lines = f.readlines()

    list_of_lines.reverse()

    return [(line.split('\t')[0], float(line.split('\t')[1]))
            for line in list_of_lines]
