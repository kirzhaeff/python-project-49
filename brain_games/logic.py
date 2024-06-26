import prompt


MAX_ROUND = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.EXPLAIN)
    index = 0
    while index < MAX_ROUND:
        question, correct_answer = game.generate_round()
        print(question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        index += 1
    print(f'Congratulations, {name}!')
