def split(word): 
    return [char for char in word]  

def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')[:-1]
    topology = []
    for line in lines:
        topology.append(split(line))
    tree_count = 1
    index_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for index in index_list:
        j = 0
        step = index[0]
        sub_tree_count = 0
        for i in range(0, len(topology), index[1]):
            if topology[i][j] == '#':
                sub_tree_count += 1
            j += step
            if j >= len(topology[0]):
                j = (j - len(topology[0]))
        print(index[1], step, sub_tree_count)
        tree_count *= sub_tree_count
    print(tree_count)
        


if __name__ == "__main__":
    main()
