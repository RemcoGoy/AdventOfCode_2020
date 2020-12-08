def run_line(index, lines, acc, visited):
    if not index >= len(lines) and index not in visited:
        command = lines[index].split(' ')[0]
        sign = lines[index].split(' ')[1][0]
        nr = lines[index].split(' ')[1][1:]
        visited.append(index)
        if command == 'nop':
            return run_line(index + 1, lines, acc, visited)
        elif command == 'acc':
            if sign == '+':
                acc += int(nr)
            else:
                acc -= int(nr)
            return run_line(index + 1, lines, acc, visited)
        elif command == 'jmp':
            if sign == '+':
                return run_line(index + int(nr), lines, acc, visited)
            else:
                return run_line(index - int(nr), lines, acc, visited)
    else:
        return acc


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    visited = []
    print(run_line(0, lines, 0, visited))


if __name__ == "__main__":
    main()
