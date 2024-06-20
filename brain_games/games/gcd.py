from math import gcd
import random

EXPLAIN = 'Find the greatest common divisor of given numbers.'
START_NUM = 1
END_NUM = 100


def generate_round():
    num_1 = random.randint(START_NUM, END_NUM)
    num_2 = random.randint(START_NUM, END_NUM)
    question = f"Question: {num_1} {num_2}"
    correct_answer = str(gcd(num_1, num_2))
    return question, correct_answer
