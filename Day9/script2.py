def main():
    filepath = 'input.txt'
    text_file = open(filepath, "r")
    lines = text_file.read().split('\n')
    search_nr = 27911108
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            test_list = []
            test_list = lines[i:j+1]
            test_list = [int(i) for i in test_list]
            if sum(test_list) == search_nr:
                print(test_list)
                break


if __name__ == "__main__":
    main()
