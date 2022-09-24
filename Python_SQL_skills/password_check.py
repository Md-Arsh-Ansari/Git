#Code a Program to check email and password for a website. Basically make a Login authentification.

email = input("Please type your email here: ") 
passwd = input("Please type your password Here: ")

if '@' in email:
    if email == "mdarshansari2002@gmail.com" and passwd == "1234abcd":
        print("Welcome")

    elif email == "mdarshansari2002@gmail.com" and passwd != "1234abcd":
        print("Incorrect Password")
        passwd = input("Please type your password again_: ")
    
        if passwd == '1234abcd':
            print("Finally correct!")
        else:
            print("still incorrect!")

    else:
        print("Incorrect email!\nPlease Try again_")


else:
    print("Invalid email format")
