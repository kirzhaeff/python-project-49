from random import randint


EXPLAIN = 'What number is missing in the progression?'


def brain():
    start_progression = randint(1, 100)
    length_progression = randint(9, 11)
    step = randint(3, 5)
    end_progression = start_progression + (step * length_progression)
    progression = list(range(start_progression, end_progression, step))
    random_number = randint(0, length_progression - 1)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    question = f'Question: {progression}'
    return question, correct_answer
