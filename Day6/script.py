def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n\n')
    groupsum = 0
    for group in lines:
        group_lines = ''.join(group.split('\n'))
        group_answers = []
        for letter in group_lines:
            if letter not in group_answers:
                group_answers.append(letter)
        groupsum += len(group_answers)
    print(groupsum)


if __name__ == "__main__":
    main()
