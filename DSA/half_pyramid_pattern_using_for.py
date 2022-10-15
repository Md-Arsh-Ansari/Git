n = int(input("Please enter a number: "))  # say 4 enter kiye.

# is n me 4 assign hai. par wo 4 jo hai. 0 se shuru hoga. 0 1 2 3.
for row in range(n):
    # 0 se bhale hi shuru ho raha hai. lekin wo 4 baar hai.
    # aur 4 baar bhale hi chalega last baar me usme 3 assign hoga.

    # row + 1 karne ke baad ab jitne baar row chalega. column me bhi utna hi number assign hoga. to column bhi utna hi baar chalega.
    for column in range(row+1):
        print("*", end=" ")

    print("")

    # type "column" instead of "* ". if you confused and dry run the program in copy.

    # On line 10 : By default Python‘s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without a newline.
    # So, Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be identified by whitespace and not a newline.

    # And thats why we didn't passed newline statement "\n" to the print function on line 12.
