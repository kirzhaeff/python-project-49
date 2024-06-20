from random import randint


EXPLAIN = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_NUM = 1
END_NUM = 100

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def generate_round():
    number = randint(START_NUM, END_NUM)
    question = f'Question: {number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
