n = int(input("Please enter a number: "))  # say "4" enter kiye.

row = n
while (row >= 1):
    column = row
    while (column >= 1):
        print(column, end=" ")
        column -= 1

    row -= 1
    print("")
