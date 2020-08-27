MIN_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Please Enter Password! : ")
    while len(password) < MIN_LENGTH:
        print("Too short!")
        password = input("Please Enter Password! : ")
    return password


main()
