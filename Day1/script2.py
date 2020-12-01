import math


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    for i in range(len(lines)):
        for j in range(len(lines)):
            for k in range(len(lines)):
                if lines[i] != '' and lines[j] != '' and lines[k] != '':
                    if (int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020):
                        return int(lines[i]) * int(lines[j]) * int(lines[k])


if __name__ == "__main__":
    print(main())
