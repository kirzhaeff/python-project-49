import random
import prompt


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and number % 2 == 0) and (answer == 'no' and number % 2 == 1):
            print('Correct!')
        elif (answer != 'yes' and number % 2 == 0):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet`s try again, {name}!")
            return
        elif (answer != 'no' and number % 2 == 1):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet`s try again, {name}")
            return
        index += 1

    print(f'Congratulations, {name}!')