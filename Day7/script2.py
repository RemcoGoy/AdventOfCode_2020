import numpy as np


def bags_to_hold(bag_map, bag):
    total = 0
    for additional in bag_map[bag]:
        additional = ' '.join(additional.strip().split(' ')[:3])
        if 'no other bags' in additional:
            return -1
        else:
            nr = int(additional.split(' ')[0])
            bag = ' '.join(additional.split(' ')[1:3])
            new_nr = bags_to_hold(bag_map, bag)
            if new_nr == -1:
                adding = nr
            else:
                adding = nr + nr*new_nr
            total += adding
    return total


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    bag_map = {}
    for line in lines:
        first = " ".join(line.split(" ")[:2])
        rest = " ".join(line.split(' ')[4:]).split(',')
        bag_map[first] = rest

    no_bags = bags_to_hold(bag_map, 'shiny gold')

    print(no_bags)


if __name__ == "__main__":
    main()
