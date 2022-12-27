import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"guess an numbre betweeen 1 and {x}: "))
        if guess < random_number:
            print("sorry. guess again , too low")
        elif guess > random_number:
            print("sorry. guess again , too high")

    print(f"yeey , congrats you have guessd the number {random_number}")  

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could be also high bcz low=high    
        feedback = input(f' is {guess} too high(H), too low (L) , or correct(C)??').lower()   
        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'h':
            low = guess +1

    print(f'yeey , the computer guessed your number {guess}, correctly')
computer_guess(10)