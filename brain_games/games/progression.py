from random import randint


EXPLAIN = 'What number is missing in the progression?'
START_MIN = 1
START_MAX = 100
LENGTH_MIN = 9
LENGTH_MAX = 11
STEP_MIN = 3
STEP_MAX = 5


def generate_round():
    start_progression = randint(START_MIN, START_MAX)
    length_progression = randint(LENGTH_MIN, LENGTH_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    end_progression = start_progression + (step * length_progression)
    progression = list(range(start_progression, end_progression, step))
    random_number = randint(0, length_progression - 1)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    progression = ' '.join(map(str, progression))
    question = f'Question: {progression}'
    return question, correct_answer
