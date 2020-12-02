import math

def find_letters(min, max, letter, pw):
    occ = 0
    for i in pw:
        if i == letter:
            occ += 1
    
    if occ >= int(min) and occ <= int(max):
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
