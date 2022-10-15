n = int(input("Please inter a number: "))

row = 1
while (row <= n):
    column = 1

    while (column <= row):
        print(row, end=" ")
        column += 1

    row += 1
    print("")

    # On line 8 : By default Python‘s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without a newline.
    # So, Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be identified by whitespace and not a newline.

    # And thats why we didn't passed newline statement "\n" to the print function on line 12.
