import random

MIN = 1
MAX = 45
NUMBER_PER_LINE =  6


def main():
    number_of_picks = int(input("How many quick pick? "))
    while number_of_picks < 0:
        print("Enter number: ")
        number_of_picks = int(input("How many quick pick? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBER_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number)for number in quick_pick))


main()
