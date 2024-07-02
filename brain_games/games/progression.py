from random import randint


EXPLAIN = 'What number is missing in the progression?'
START_MIN = 1
START_MAX = 100
LENGTH_MIN = 9
LENGTH_MAX = 11
STEP_MIN = 3
STEP_MAX = 5


def get_progression(start_progression, step, length_progression):
    end_progression = start_progression + (step * length_progression)
    numbers = []
    for i in range(start_progression, end_progression, step):
        numbers.append(i)
    return numbers


def generate_round():
    start_progression = randint(START_MIN, START_MAX)
    length_progression = randint(LENGTH_MIN, LENGTH_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    progression = get_progression(start_progression, step, length_progression)
    random_number = randint(0, length_progression - 1)
    correct_answer = str(progression[random_number])
    progression[random_number] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'
    return question, correct_answer
