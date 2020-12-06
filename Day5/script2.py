import math


def missing_elements(L, start, end):
    if end - start <= 1:
        if L[end] - L[start] > 1:
            yield from range(L[start] + 1, L[end])
        return

    index = start + (end - start) // 2

    # is the lower half consecutive?
    consecutive_low = L[index] == L[start] + (index - start)
    if not consecutive_low:
        yield from missing_elements(L, start, index)

    # is the upper part consecutive?
    consecutive_high = L[index] == L[end] - (end - index)
    if not consecutive_high:
        yield from missing_elements(L, index, end)


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    highest = 0
    seat_list = []
    for line in lines:
        row = line[:7]
        row_nr = 0
        min = 0
        max = 127
        seat = line[7:10]
        seat_nr = 0
        for (i, letter) in enumerate(row):
            if i == len(row) - 1:
                row_nr = min if letter == 'F' else max
            else:
                if letter == 'F':
                    max = math.floor((max - min) / 2) + min
                elif letter == 'B':
                    min = math.ceil((max - min) / 2) + min

        min = 0
        max = 7
        for (i, letter) in enumerate(seat):
            if i == len(seat) - 1:
                seat_nr = min if letter == 'L' else max
            else:
                if letter == 'L':
                    max = math.floor((max - min) / 2) + min
                elif letter == 'R':
                    min = math.ceil((max - min) / 2) + min
        seat_id = row_nr * 8 + seat_nr
        seat_list.append(seat_id)

    sorted_list = sorted(seat_list)
    print(list(missing_elements(sorted_list, 0, len(sorted_list)-1)))


if __name__ == "__main__":
    main()
