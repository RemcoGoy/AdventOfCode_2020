import numpy as np


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n\n')
    groupsum = 0
    for group in lines:
        group_lines = group.split('\n')
        group_answer = []

        for letter in group_lines[0]:
            every = True
            for i in range(1, len(group_lines)):
                if letter not in group_lines[i]:
                    every = False
            if every:
                group_answer.append(letter)
        print(np.unique(np.array(group_answer)))
        groupsum += len(np.unique(np.array(group_answer)))
    print(groupsum)


if __name__ == "__main__":
    main()
