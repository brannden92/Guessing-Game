import random

# You try to guess the number the CPU has picked
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    count = 1
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low, try again!')
            count +=  1
        elif guess > random_number:
            print('Too high, try again!')
            count +=  1
    print(f'Ayyyy, you guessed the number {random_number} correctly in {count} tries!')

# The CPU tries to guess the number you have picked
def cpu_guess(x):
    low = 1
    high = x
    count = 1     
    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), low (L), or correct (C?').lower() 
        if feedback == 'h':
            high = guess - 1
            count +=  1
        elif feedback == 'l':
            low = guess + 1
            count += 1
        else:
            break
    print(f'The computer has guessed your number {guess} correctly in {count} tries!')

selection = input('Do you wish to guess the computer\'s number (option: 1) or have the computer guess yours (option: 2)?')
if int(selection) == 1:
    x = int(input('How large of a range do you wish to guess between? 1 and : '))
    guess(x)
elif int(selection) == 2:
    x = int(input('How large of a range do you want the CPU to guess between? 1 and : '))
    cpu_guess(x)