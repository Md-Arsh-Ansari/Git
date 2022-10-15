n = int(input("Please enter a number: "))  # say "4" enter kiye.

for row in range(n, 0, -1):

    for column in range(0, row):
        # Pahle hi char le liya gaya hai to ab ye 4 baar print karega hi. isliye ulta nahi kiye "-1" laga ke.
        print("* ", end=" ")

    print("")
