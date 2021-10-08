import random


"""def guess_random_number(tries, start, stop):

    random_number = random.randint(start, stop)

    while tries != 0:
        print("Number of tries left:", tries)

        guess_number = float(input('Guess a number between 0 and 10: '))
        # print("Guess a number between 0 and 10:", guess_number)

        if guess_number == random_number:
            print('You guessed the correct number!')
            return
        if guess_number < random_number:
            # print("Guess a number between 0 and 10:", random_number)
            print('Guess Higher!')
        if guess_number > random_number:

            print('Guess lower!')
        tries -= 1

    print("You have failed to guess the number:", random_number)


guess_random_number(5, 0, 10)"""


"""def guess_random_num_linear(tries, start, stop):

   # while tries >= 0:
    random_number = random.randint(start, stop)

    print("The number for the program to guess is: ", random_number)

    for x in range(start, tries):
        if x == random_number:

            print("The program is guessing...", x)

            print('The program has guessed the correct number!')

            return

        if x != random_number:

            print("Number of tries left:", tries)
            print("The program is guessing...", x)

        tries -= 1
    print("The program has failed to guess the correct number")


guess_random_num_linear(5, 0, 10)"""


def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)

    print("Random number to find:", target)
    while tries > 0:
        pivot = int(start + stop) // 2

        if pivot > target:
            stop = pivot - 1
            print("Guessing higher!", pivot)

        if pivot < target:
            start = pivot + 1

            print("Guessing lower!", pivot)
            tries -= 1
        if pivot == target:
            print("found it!", pivot)
            return pivot
    print("Your program failed to find the number")


guess_random_num_binary(5, 0, 100)
