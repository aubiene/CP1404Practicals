import random

# line 1
print(random.randint(5, 20))

# line 2
print(random.randrange(3, 10, 2))

# line 3
print(random.uniform(2.5, 5.5))
# 4.051403211858381

"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

   ANSWER:  smallest number = 5 largest number = 20

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

   ANSWER:  smallest number = 3 largest number = 9
            line 2 could not have produced a 4

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

    ANSWER: smallest number = 2.5 largest number = 5.4"""

# TODO Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 10))
