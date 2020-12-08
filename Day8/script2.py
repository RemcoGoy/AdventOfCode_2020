def run_line(index, lines, acc, visited, change):
    if index in visited:
        return None
    elif index >= len(lines):
        return acc
    else:
        command = lines[index].split(' ')[0]
        if index == change:
            command = 'jmp' if command == 'nop' else 'nop'
        sign = lines[index].split(' ')[1][0]
        nr = lines[index].split(' ')[1][1:]
        visited.append(index)
        if command == 'nop':
            return run_line(index + 1, lines, acc, visited, change)
        elif command == 'acc':
            if sign == '+':
                acc += int(nr)
            else:
                acc -= int(nr)
            return run_line(index + 1, lines, acc, visited, change)
        elif command == 'jmp':
            if sign == '+':
                return run_line(index + int(nr), lines, acc, visited, change)
            else:
                return run_line(index - int(nr), lines, acc, visited, change)


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    nops = []
    jmps = []
    for i, line in enumerate(lines):
        command = line.split(' ')[0]
        if command == 'nop':
            nops.append(i)
        elif command == 'jmp':
            jmps.append(i)

    for i in nops:
        visited = []
        ret = run_line(0, lines, 0, visited, i)
        if ret != None:
            print(ret)
            break

    for i in jmps:
        visited = []
        ret = run_line(0, lines, 0, visited, i)
        if ret != None:
            print(ret)
            break


if __name__ == "__main__":
    main()
