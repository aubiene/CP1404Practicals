"""
When will a ValueError occur?
    ANSWER: when the user inputs anything other than a int

When will a ZeroDivisionError occur?
    ANSWER: When the user inputs a 0 as the denominator

Could you change the code to avoid the possibility of a ZeroDivisionError?
    ANSWER: No?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
