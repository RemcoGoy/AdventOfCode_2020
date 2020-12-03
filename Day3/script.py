def split(word): 
    return [char for char in word]  

def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')[:-1]
    topology = []
    for line in lines:
        topology.append(split(line))
    tree_count = 0
    j = 0
    step = 3
    for i in range(len(topology)):
        if topology[i][j] == '#':
            tree_count += 1
        j += step
        if j >= len(topology[0]):
            j = (j - len(topology[0]))
    print(tree_count)
        


if __name__ == "__main__":
    main()
