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
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()
