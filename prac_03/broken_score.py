import random


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))

# generates a random score and prints the result
    score = (random.randint(0, 100))
    print("{} is {}".format(score, determine_score(score)))


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
