n = int(input("Please enter a number: "))

for row in range(n):

    for column in range(row+1):

        print(row+1, end=" ")

    print("")

    # type "column" instead of "* ". if you confused and dry run the program in copy.

    # On line 10 : By default Python‘s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without a newline.
    # So, Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be identified by whitespace and not a newline.

    # And thats why we didn't passed newline statement "\n" to the print function on line 12.
