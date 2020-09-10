def main():
    email_to_name = {}
    email_address = input("Email: ")

    while email_address != "":
        name = get_name_from_email(email_address)
        confirmation = input("Is your name {} ? (Y/N) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email_address] = name
        email_address = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email_address):
    prefix = email_address.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
