import re


def flatten(t): return [item for sublist in t for item in sublist]


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n\n')[:-1]
    valid_props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_props.sort()
    valid_count = 0
    for line in lines:
        obj = []
        line = line.split('\n')
        for subline in line:
            subline = subline.split(' ')
            obj.append(subline)

        obj = flatten(obj)
        props = []
        for subline in obj:
            props.append(subline.split(":")[0])

        if 'cid' in props:
            props.remove('cid')
        props.sort()
        if (props == valid_props):
            valid = True
        else:
            valid = False

        for subline in obj:
            prop = subline.split(":")[0]
            key = subline.split(":")[1]
            if prop == 'byr':
                if not (len(key) == 4 and int(key) >= 1920 and int(key) <= 2002):
                    valid = False
            elif prop == 'iyr':
                if not (len(key) == 4 and int(key) >= 2010 and int(key) <= 2020):
                    valid = False
            elif prop == 'eyr':
                if not (len(key) == 4 and int(key) >= 2020 and int(key) <= 2030):
                    valid = False
            elif prop == 'hgt':
                if key[-2:] == 'cm':
                    if not (int(key[:-2]) >= 150 and int(key[:-2]) <= 193):
                        valid = False
                elif key[-2:] == 'in':
                    if not (int(key[:-2]) >= 59 and int(key[:-2]) <= 76):
                        valid = False
                else:
                    valid = False
            elif prop == 'hcl':
                if not (re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', key)):
                    valid = False
            elif prop == 'ecl':
                if not (key in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    valid = False
            elif prop == 'pid':
                if not (len(key) == 9 and key.isnumeric()):
                    valid = False

        if valid:
            valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()
