def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    preamble = 25
    for l_index, line in enumerate(lines[preamble:]):
        nr = int(line)
        valid = False
        for i in range(l_index, l_index + preamble):
            for j in range(l_index, l_index + preamble):
                if not i == j and not i > j:
                    nr1 = int(lines[i])
                    nr2 = int(lines[j])
                    if nr1 + nr2 == nr:
                        valid = True
        if not valid:
            print(nr, l_index + preamble)
            break


if __name__ == "__main__":
    main()
