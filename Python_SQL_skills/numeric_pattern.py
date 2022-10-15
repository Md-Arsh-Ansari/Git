number = int(input("Please inter a number: "))


row = 1
while (row < number + 1):
    column = 1
    while (column < row):
        print("*")
        column = column + 1
    row = row + 1
