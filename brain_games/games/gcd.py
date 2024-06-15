from math import gcd
import random

EXPLAIN = 'Find the greatest common divisor of given numbers.'


def brain():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = f"Question: {num_1} {num_2}"
    correct_answer = str(gcd(num_1, num_2))
    return question, correct_answer
