"""Not yet complete"""

LOWER = 33
UPPER = 127

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number < LOWER or number > UPPER:
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number)))

pass
