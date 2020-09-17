from prac_06.guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 2003.2)

    print("{} get_age() - Expected 98. got {}".format(guitar.name, guitar.get_age()))
    print("{} get_age() - Expected 7. got {}".format(another_guitar.name, another_guitar.get_age()))

    print("{} is_vintage() - Expected True. got {}".format(guitar.name, guitar.is_vintage()))
    print("{} is_vintage() - Expected False. got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
