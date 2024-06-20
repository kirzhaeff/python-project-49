import random


EXPLAIN = 'What is the result of the expression?'
START_NUM = 1
END_NUM = 30


def generate_round():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(START_NUM, END_NUM)
    num_2 = random.randint(START_NUM, END_NUM)
    question = f'Question: {num_1} {operator} {num_2}'
    if operator == '+':
        correct_answer = num_1 + num_2
    elif operator == '-':
        correct_answer = num_1 - num_2
    elif operator == '*':
        correct_answer = num_1 * num_2
    return question, str(correct_answer)
