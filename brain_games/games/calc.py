import random


EXPLAIN = 'What is the result of the expression?'
START_NUM = 1
END_NUM = 30


def calculate(num_1, num_2, operator):

    if operator == '+':
        result = num_1 + num_2
    elif operator == '-':
        result = num_1 - num_2
    elif operator == '*':
        result = num_1 * num_2
    return result


def generate_round():
    operator = random.choice(['+', '-', '*'])
    num_1 = random.randint(START_NUM, END_NUM)
    num_2 = random.randint(START_NUM, END_NUM)
    question = f'Question: {num_1} {operator} {num_2}'
    correct_answer = str(calculate(num_1, num_2, operator))
    return question, correct_answer
