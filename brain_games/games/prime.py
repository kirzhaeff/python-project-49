from random import randint


EXPLAIN = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    return True


def brain():
    number = randint(1, 100)
    question = f'Question: {number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
