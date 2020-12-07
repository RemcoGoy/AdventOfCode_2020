import numpy as np


def can_hold_gold(bag_map, bag):
    if 'shiny gold' in ' '.join(bag_map[bag]):
        return True
    else:
        if 'no other bags.' in bag_map[bag]:
            return False
        else:
            can_hold = False
            for new_bag in bag_map[bag]:
                new_bag = ' '.join(new_bag.strip().split(' ')[1:3])
                can_hold = can_hold_gold(bag_map, new_bag) or can_hold
            return can_hold


def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    bag_map = {}
    hold_gold = []
    for line in lines:
        first = " ".join(line.split(" ")[:2])
        rest = " ".join(line.split(' ')[4:]).split(',')
        bag_map[first] = rest

    for line in lines:
        first = " ".join(line.split(" ")[:2])
        rest = " ".join(line.split(' ')[4:]).split(',')
        if can_hold_gold(bag_map, first):
            hold_gold.append(first)

    print(len(hold_gold))


if __name__ == "__main__":
    main()
