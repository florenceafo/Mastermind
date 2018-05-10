import random

num_guess = 0
print('\n')
print('Welcome to my random number guessing game!', end='')
print('\n')
print('I have a four digit number in mind and it is up to you to guess what it is!')
print('\n')
print('After each guess I will give you one biscuit for every correct digit and a rotten egg for the incorrect ones. Keep going until you guess my number :)')
print('\n')

def random_number_generator():
    rand_num = []
    for i in range(4):
        rand_num += str(random.randint(0,9))
    print(rand_num)
    num_guess = 0
    rand_num = user_guess(rand_num, num_guess)


def user_guess(rand_num, num_guess):

    guess = 0
    print('Enter a number between 0000 and 9999:')
    print('\n')
    guess = input()

    guess = [list(x) for x in guess.split(',')]


    guess.append(guess[0][0])
    guess.append(guess[0][1])
    guess.append(guess[0][2])
    guess.append(guess[0][3])
    guess = guess[1:]
    rand_num = rand_num
    guess = game(guess, rand_num, num_guess)



def game(guess, rand_num, num_guess):

    num_guess += 1
    if guess != rand_num:
        biscuits = 0
        eggs = 0
        for i in range(4):
            if guess[i] == rand_num[i]:
                biscuits += 1
            else:
                eggs += 1
        print('Biscuits: ' + str(biscuits) + ' and eggs: ' + str(eggs) + ',')
        print('\n')
        if biscuits == 3:
            print('You are so close!')
            print('\n')
        user_guess(rand_num, num_guess)
    else:
        print('CORRECT!')
        print('It took you ' + str(num_guess) + ' guesses.')




random_number_generator()
