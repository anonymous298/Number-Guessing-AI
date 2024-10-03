import random
import time

def NumberGuessingAI():
    try:
        user = int(input('Enter your number 1-100: '))
        attempts = 0
        START = 1
        STOP = 100

        while True:
            computer = random.randint(START, STOP)
            if computer == user:
                print('Guessed It.')
                break

            if computer > user:
                print('Too high')      
                STOP = computer - 1

            elif computer < user:
                print('Too low')
                START = computer + 1

            attempts += 1 
            print(f"Range now: {START}-{STOP}\n")
            time.sleep(0.5)
            # print('Not guessed')

        print(f'Computer guessed it in {attempts} attempts!')

    except ValueError as e:
        print("Please enter a valid number between 1-100.") 

    except Exception as e:
        print(f"An error occurred: {e}")    

NumberGuessingAI()