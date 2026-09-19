import os
import random

def clear_screen():
    # os.name بتكون 'nt' لو النظام ويندوز، وغير كذا تكون 'posix' (ماك/لينكس)
    os.system('cls' if os.name == 'nt' else 'clear')

# توليد رقم عشوائي بين 1 و 10
secret_number = random.randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number between 1 and 10'))
        
        if guess == secret_number:
            print("Corret! You won")
            break
        else:
            # مسح الشاشة قبل التكرار التالي
            clear_screen()
            print("Wrong! Try again\n")
            
    except ValueError:
        clear_screen()
        print("Please enter a valid number!\n")