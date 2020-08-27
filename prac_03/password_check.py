MIN_LENGTH = 6

password = input("Please Enter Password! : ")
while len(password) < MIN_LENGTH:
    print("Invalid Password!")
    password = input("Please Enter Password! : ")
print("*" * len(password))
