import random


EXPLAIN = 'Answer "yes" if the number is even, otherwise answer "no".'
START_NUM = 1
END_NUM = 100


def generate_round():
    number = random.randint(START_NUM, END_NUM)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
