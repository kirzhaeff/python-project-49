import random


DESCRIPTION = 'What is the result of the expression?'


def brain():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(1, 30)
    num_2 = random.randint(1, 30)
    question = f'Question: {num_1} {operator} {num_2}'
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    elif operator == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
