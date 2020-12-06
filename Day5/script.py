import math


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    highest = 0
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
        if seat_id > highest:
            highest = seat_id

    print(highest)


if __name__ == "__main__":
    main()
