"""Do-from-scratch Exercises"""

out_file = open("name.txt", 'w')
name = input("Please enter name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", 'r')
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

in_file = open("numbers.txt", 'r')
number = int(in_file.readline())
number2 = int(in_file.readline())
print(number + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
total += number
in_file.close()
print("the sum is :", total)
