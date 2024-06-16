import random


EXPLAIN = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
