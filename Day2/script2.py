import math

def find_letters(min, max, letter, pw):
    if pw[int(min) - 1] == letter and pw[int(max) - 1] != letter or pw[int(min) - 1] != letter and pw[int(max) - 1] == letter:
        return 1
    else:
        return 0


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    valid = 0
    for line in lines:
        if line != '':
            split_lines = line.split(' ')
            valid += find_letters(split_lines[0].split('-')[0], split_lines[0].split('-')[1], split_lines[1].split(':')[0], split_lines[2])
    
    print(valid)


if __name__ == "__main__":
    main()
