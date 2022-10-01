import random

jackpot = random.randint(1, 100)

guess = int(input("Please guess a number. Sir!\n: "))
count = 1


while guess != jackpot:
    if guess < jackpot:
        print("\nChoose little bit higher number!")

    else:
        print("\nChoose little bit lower number!")

    guess = int(input(": "))

    count += 1


print(
    f"\nBingooo... Sir!!! in just {count} guess!\n Bingo! Bingo! Bingo! \n kamal kar diya Sir aapne to ekdam! \n Dil khush kar diya. \n Wah Sir!! Wah!!!")
