import random


def create_rand_number(high):
    return random.randint(1, high)


def guess_game(high):
    rand_number = create_rand_number(high)
    print(rand_number)
    is_over = False
    while not is_over:
        guess = int(input(f'Guess a number between 1 and {high}\n'))
        if rand_number < guess:
            print(f'Sorry, guess again. Too high\n')
        elif rand_number > guess:
            print(f'Sorry, guess again. Too Low\n')
        else:
            print(f'Yay, you have guessed the number {rand_number} correctly!\n')
            is_over = True


def guess_the_number(x):
    low = 1
    high = x
    guess = 0
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Could also be high because high = low
        feedback = input(f'Is {guess} too high (H) or too low (L) or correct (C)\n')
        if feedback.lower() == 'h':
            high = guess - 1
        elif feedback.lower() == 'l':
            low = guess + 1
    print(f'Yay, you have guessed the number {guess} correctly!\n')


def play_game():
    play = input('Hello there, Do you want to play random number guessing game? Y or N\n')
    while play.lower() == 'y':
        strategy = input('Hello there, Do you want to guess (M) or the computer to guess (C)?\n')
        if strategy.lower() == 'm':
            guess_game(1000)
        elif strategy.lower() == 'c':
            guess_the_number(1000)
        play = input('Hello there, Do you want to play random number guessing game? Y or N\n')


play_game()
