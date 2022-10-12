def read_inputs():
    test_case = int(input())
    for i in range(test_case):
        row, col = input().split()

        if (row == "3" or row == "2") and (col == "3" or col == "2"):
            print("2 2")

        else:
            print("1 1")


if __name__ == '__main__':
    read_inputs()
