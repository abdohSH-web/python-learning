# print("""

# ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
# ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
# ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
# ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
# ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
# ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
# """)        
# door = input("""Welcome to my island!
# There are two doors in front of you
# Which door do you want to open?
# [The red door 🔴🚪] [The blue door 🔵🚪]
# \n""").lower()
# if door == 'red':
#     print("""You opened the door that has crocodiles!!
#     🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊🐊""")
# elif door == 'blue'    :
#     box = input("""Alright, you entered a room that has three boxes!
#     [a white box 📦] [a black box 📦] [a brown box 📦]
#     which box do you choose? \n
#     """).lower()
#     if box == 'white':
#         print("""You opened the box that contains snakes!!
#         🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍""")
#     elif box == 'black':
#         print("""You opened the box that contains spiders!!
#         🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️🕷️
#         """) 
#     elif box == 'brown':
#         print("""You found the treasure!!!
#         🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙
#         """)  
#     else:
#         print('Invalid choice. Please choose only from the given boxes.\nTry again')         
# else:
#     print('Sorry, choose only between the two given doors.\nTry again')    
# import random
# print('Welcome to the coin guessing game!')
# choice = input('''Choose a methon to toss the coin
# 1. Using random.random.
# 2. Using random.randint.
# Enter your choice (1 or 2)\n
# ''')
# if choice == "1":
#     random_number = random.random()
#     if random_number >= 0.5:
#         computer_choice = "Heads"
#     else:
#         computer_choice = "Tails"  
# elif choice == "2":
#     if random.randint(0,1) == 0:
#         computer_choice = "Heads"
#     else:
#         computer_choice = "Tails"    
# else:
#     print("Unvalid choice. Please choose [1] or [2]")
# user_choice = input("Enter your quess, choose [Heads] or [Tails]\n")
# if user_choice.lower() == computer_choice.lower():
#     print("Congratulations! You won")
#     print(f'The computer choose was {computer_choice} too!')
# else:
#     print("Sorry. You lost. Try again!")    
#     print(f"The computer choise was: {computer_choice}")    
# family = ['Salem', 'Ruqayah', 'Abdullah', 'Mohammed', 'Maryam', 'Tasneem', 'Omer']
# import random
# choice = random.randint(0,6)
# if choice == 1:
#     print(family[0])
# elif choice == 2:
#     print(family[1])    
# elif choice == 3:
#     print(family[2])    
# elif choice == 4:
#     print(family[3]) 
# elif choice == 5:
#     print(family[4]) 
# elif choice == 6:
#     print(family[5]) 
# else:
#     print(family[6])                
# colors = []
# favorite = input("What's your favorite color?\n")
# colors.append(favorite)
# another_favorite = input("Do you like another color too? [Yes] or [No]\n").lower()
# if another_favorite == 'yes':
#     favorite2 = input("What's your second favorite color\n")
#     colors.append(favorite2)
#     print(f'Your favorite colors are: {colors}')
# elif another_favorite == 'no':
#     print(f'Your favorite color is: {colors}')  
# else:
#     print("Follow the instructions please")   
# books = []
# first_owned_book = input('Enter the name of a book you own:\n').lower()
# books.append(first_owned_book)
# second_owned_book = input('Enter the name of another book you own (or press "enter" to skip)\n').lower()
# if second_owned_book:
#     books.append(second_owned_book)
#     print(f'Your library:{books}')
# else:
#     print(f'Your library:{books}')
# wish_list = []    
# wished_book1 = input('Enter the name of a book you wish to have in the future:\n').lower()
# wish_list.append(wished_book1)
# wished_book2 = input("Enter the name of another book you wish to have in the future (or press 'Enter to skip') \n").lower()
# if wished_book2:
#     wish_list.append(wished_book2)
#     print(f"Your wishlist is:{wish_list}")
# else:
#     print(f'Your wishlist is:{wish_list}')    
# acquired_book = input("Enter the name of the book from your wishlist that you've acquired (or press 'Enter' to skip):\n").lower()    
# if acquired_book:
#     if acquired_book in wish_list:
#         wish_list.remove(acquired_book)
#         books.append(acquired_book)
#         print(f"""
#         Update: Your library:{books}
#         Update: Your wishlist:{wish_list}
#                 """)
#     else:
#         print("This book isn't in your wishlist.")   
# else:
#     print(f"""
#     Update: Your library:{books}
#     Update: Your wishlist:{wish_list}
#             """)
# book_to_donate = input("Enter the name of a book from your library that you want to donate (or press 'Enter' to skip):\n").lower()
# if book_to_donate:
#     if book_to_donate in books:
#         books.remove(book_to_donate)
#         print("Final updated library: {books}")
#     else:
#         print("This book isn't in your library")   
# else:
#     print("Final updated library: {books}")
# import random
# print("Welcome to 'Whose wallet?'")
# print("You will give me a list of names, and I will pick a person to pay")
# splited_names = input("Enter a list of names separated by comma.....")
# names = splited_names.split(", ")
# print(f'Please ask {random.choice(names)} to take out his wallet. Dinner on him')
# print("Welcome to 'Place the Rabbit'")
# filed = [['🌿','🌿','🌿'],['🌿','🌿','🌿'],['🌿','🌿','🌿']]
# print(f"\n{filed[0]}\n{filed[1]}\n{filed[2]}\n")
# print("Where should the rabbit go?🐇")
# position = input("Please enter a row and a column:\n")
# row = int(position[0])
# column = int(position[1])
# filed[row-1][column-1] = '🐇'
# print(f"\n{filed[0]}\n{filed[1]}\n{filed[2]}\n")
# import random
# print("Welcome to Rock, Paper, Scissors")
# input("Please type 'enter' to continue")
# game = ['Rock', 'Paper', 'Scissors']
# computer_choice = random.randint(0,2)
# if computer_choice == 0:
#     choice1 = "👊"
# elif computer_choice == 1:
#     choice1 = "🫱"   
# else:
#     choice1 = "✌️"     
# player_choice = input("Please enter your choice [Rock] [Paper] [Scissors]\n").capitalize()
# if player_choice in game:
#     if player_choice == "Rock":
#         choice = "👊"
#     elif player_choice == "Paper"  :
#         choice = "🫱"  
#     else:
#         choice = "✌️"    
# else:
#     print("Invalid choice. Please choose [Rock] [Paper] [Scissors]")   
# input("Downloading....\n")      
# if computer_choice == 0 and player_choice == 'Rock' or computer_choice == 1 and player_choice == 'Paper' or computer_choice == 2 and player_choice == 'Scissors':
#     print(f'computer choise is {choice1}\n')
#     print(f'Your choice is {choice}')
#     print("\n\nDraw")
# elif computer_choice == 0 and player_choice == 'Scissors' or computer_choice == 1 and player_choice == 'Rock' or computer_choice == 2 and player_choice == 'Paper':   
#     print(f'computer choise is {choice1}\n')
#     print(f'Your choice is {choice}')
#     print("\n\nYou Lost!") 
# else:
#     print(f'computer choise is {choice1}\n')
#     print(f'Your choice is {choice}')
#     print("\n\nYou Won!")
# items = []
# price = []    
# print("***Welcome to iShop Calculator***\n")  
# items_number = int(input("How many items are there in your basket today? "))
# print("Let's get to counting them....")

# for i in range(1, items_number + 1):
#     item = input(f"Please tell me the name of item number {i} ")
#     items.append(item)
#     cost = float(input(f"What's the price of {item}?\n$"))
#     price.append(cost)
# confirming1 = input("Would you like to see your entire basket? [Yes or No] ").lower() 
# if confirming1 == 'yes':
#     print(items)    
# confirming2 = input("Would you like to see how much it'll cost? [Yes or No] ").lower()   
# if confirming2 == 'yes':
#     print(f"Buying these items will cost: ${sum(price)}")
# names = input("Enter the first and last names of your friends separated by a comma: ").split(", ")
# abbreviated_names = []
# for name in names:
#     name_parts = name.split()
#     print(name_parts)
#     first_name = name_parts[0]
#     last_name = name_parts[1]
#     first_initial = first_name[0]
#     last_initial = last_name[0]
#     abbreviation = first_initial + '.' + last_initial + '.'
#     abbreviated_names.append(abbreviation)    
# print('abbreviated names:')
# for x in abbreviated_names:
#     print(x)   
# sentence = input("Enter a sentence.. ").split()
# reveresed_words = sentence[::-1]
# reversed_sentence = ' '.join(reveresed_words)
# print(reversed_sentence)
# import string
# sentence = input("Enter a sentence: ")
# new_sentence = ""
# for i in sentence:
#     if i not in string.punctuation:
#         new_sentence += i
# print(f"Here is the sentence without punctuations:\n {new_sentence}")       
# import random
# import string 
# print("***Welcome to the Password Generator***\n")
# total_number = int(input("Enter the total number of characters in the password: "))
# number_of_letters = int(input("Enter the number of letters in the password: "))
# number_of_numbers = int(input("Enter the number of numbers in the password: "))
# number_of_symbols = int(input("Enter the number of symbols in the password: "))
# sum_of_characters = number_of_letters + number_of_numbers + number_of_symbols
# if total_number != sum_of_characters:
#     print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password's length")
# else:    
#     letters = random.choices(string.ascii_letters, k=number_of_letters)
#     numbers = random.choices(string.digits, k=number_of_numbers) 
#     symbols = random.choices(string.punctuation, k=number_of_symbols)
#     password_cha = letters + numbers + symbols
#     random.shuffle(password_cha)
#     print(''.join(password_cha))
# def welcome():
#     input("Say my name ")
# def wellfare():
#     print("Thanks for using the app")
# welcome()
# bye = input("Please press enter to exist from the app.....")  
# wellfare()  
# import random
# correct_number = random.randint(1,10)
# guessed_number = int(input("Guess a number between 1 and 10: "))
# while guessed_number != correct_number:
#     if guessed_number > correct_number:
#         guessed_number = int(input("Too high, try again "))
#     else:
#         guessed_number = int(input("Too low, try again "))
# print(f"Well done! You guessed the number {correct_number}")    
# import random
# words = ['yemen','mexico','turkey','russia']
# random_word = random.choice(words)
# display = []
# for i in random_word:
#     display.append('__')    
# print(display)
# number_of_trials = 5
# while '__' in display:
#     guessed_letter = input("\n\nPlease guess a letter  ").lower()
#     for position in range(len(random_word)):
#         if random_word[position] == guessed_letter:
#             display[position] = guessed_letter
#     print(display)    
# print(f"""
# *******
# You won
# *******
# the correct word is {random_word}
# """)     
# import random
# print("Welcome to Hang Man Game!\n") 
# words = ['JANUARY','FEBRUARY','APRIL','AUGUST']
# random_word = random.choice(words)
# display=['__'] * len(random_word)
# print(' '.join(display))    
# trials = 5
# while '__' in display and trials > 0:
#     guessed = input("Please guess a letter:  ").upper()
#     if guessed not in random_word:
#         trials -= 1
#     for position in range(len(random_word)):
#         if random_word[position] == guessed:
#             display[position] = guessed
#     print(' '.join(display))
#     print(f'You have {trials} more trials')   
# if trials == 0:
#     print('''
# ☠️ ☠️ You lost ☠️ ☠️
#  ___________.._______
# | .__________))______|
# | | / /      ||
# | |/ /       ||
# | | /        ||.-''.
# | |/         |/  _  \
# | |          ||  `/,|
# | |          (\\`_.'
# | |         .-`--'.
# | |        /Y . . Y\
# | |       // |   | \\
# | |      //  | . |  \\
# | |     ')   |   |   (`
# | |          ||'||
# | |          || ||
# | |          || ||
# | |          || ||
# | |         / | | \
# """"""""""|_`-' `-' |"""|
# |"|"""""""\ \       '"|"|
# | |        \ \        | |
# : :         \ \       : :  
# . .          `'       . .

# ''')
# else:
#     print('''
# ********************    
# 🎉🎉 You won! 🎉🎉
# ********************
# ''')    
# import random
# print("""
# 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 ❞𝑯𝒂𝒏𝒈 𝑴𝒂𝒏❞
# """)
# words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
#          'coyote crow deer dog donkey duck eagle ferret fox frog goat '
#          'wombat zebra ').split()
# random_word = random.choice(words)
# display = ['__'] * len(random_word)
# print(' '.join(display))
# HANGMANPICS = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
# letters = []
# trials = 6
# print(HANGMANPICS[0])
# while '__' in display and trials > 0:
#     guessed = input("Please guess a letter.. ").lower()
#     if guessed in letters:
#         print(f"You have already chosen {guessed} before, try another letter")
#         continue
#     letters.append(guessed)
#     if guessed not in random_word:
#         trials -= 1
#         print(HANGMANPICS[6-trials])
#     for position in range(len(random_word)):
#         if random_word[position] == guessed:
#             display[position] = guessed
#     print(' '.join(display))
#     print(f"You have {trials} trials")    
# if trials == 0:
#     print(f'You lost\nthe correct word was: {random_word}\n{HANGMANPICS[-1]}')
# if '__' not in display:
#     print("You won")    
# import random
# print("""
#              𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 ❞𝑯𝒂𝒏𝒈 𝑴𝒂𝒏❞
# """)
# words = ('bread sugar milk water eggs bananas beaf').split()
# random_word = random.choice(words)
# display = ['__'] * len(random_word)
# print(' '.join(display))
# HANGMANPICS = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
# trials = 6
# letters = []
# print(f'\n{HANGMANPICS[0]}')
# while '__' in display and trials > 0:
#     guessed = input("Please guess a letter...  ").lower()
#     if guessed in letters:
#         print(f"You have already chosen {guessed}, please try again")
#         continue
#     letters.append(guessed)
#     if guessed not in random_word:
#         trials -= 1
#         print(f'{HANGMANPICS[6-trials]}')
#         print(f"You have {trials} more trials")
#     for position in range(len(random_word)):
#         if random_word[position] == guessed:
#             display[position] = guessed
#     print(' '.join(display)) 
# if trials == 0:
#     print(f'''
#          You lost!
#          {HANGMANPICS[-1]}
# ''')         
# if '__' not in display:
#     print(f'''
#          You won!
         
# ░██╗░░░░░░░██╗███████╗██╗░░░░░██╗░░░░░  ██████╗░░█████╗░███╗░░██╗███████╗██╗
# ░██║░░██╗░░██║██╔════╝██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗████╗░██║██╔════╝██║
# ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░░░░  ██║░░██║██║░░██║██╔██╗██║█████╗░░██║
# ░░████╔═████║░██╔══╝░░██║░░░░░██║░░░░░  ██║░░██║██║░░██║██║╚████║██╔══╝░░╚═╝
# ░░╚██╔╝░╚██╔╝░███████╗███████╗███████╗  ██████╔╝╚█████╔╝██║░╚███║███████╗██╗
# ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝
# ''')
# def multiply(number):
#     for i in range(1, 11)  :
#         print(f'{i}x{number} = {number * i}')  
# multiply(6)    
# def information(age, name):
#     print(f'Your name is {name}, and you are {age} years old.')    
# information(age=20, name='Abdullah')            
# import string
# alphabet = string.ascii_lowercase + string.ascii_lowercase
# word = input("Enter a word  ").lower()
# encrypted_word =  ''
# for letter in word:
#     original_position = alphabet.index(letter)
#     new_position = original_position + 2
#     encrypted_word += alphabet[new_position]
# print(f'Here is the encrypted word: {encrypted_word}')   
# import string
# alphabet = string.ascii_lowercase
# word = input("Enter a word  ").lower()
# encrypted_word =  ''
# for letter in word:
#     if letter not in alphabet:
#         encrypted_word += letter
#         continue
#     original_position = alphabet.index(letter)
#     new_position = (original_position + 2) % 26
#     encrypted_word += alphabet[new_position]
# print(f'Here is the encrypted word: {encrypted_word}')    
# import string
# alphabet = string.ascii_letters + string.ascii_letters
# original_message = input('Enter a message:  ')
# shift_number = int(input("Enter a shift number:  "))
# encrypted_message = ''
# for letter in original_message:
#     if letter not in alphabet:
#         encrypted_message += letter
#         continue
#     original_position = alphabet.index(letter)
#     new_position = original_position + shift_number
#     encrypted_message += alphabet[new_position]
# print(encrypted_message) 


# import string 
# def encrypt(message, shift):
#     alphabet = string.ascii_letters + string.ascii_letters

#     encrypted_message = ''
#     for letter in message:
#         if letter not in alphabet:
#             encrypted_message += letter
#             continue
#         original_position = alphabet.index(letter)
#         new_position = original_position + shift
#         encrypted_message += alphabet[new_position]
#     print(encrypted_message)  

# message = input("Please enter a message:   ")
# shift_number = int(input('Enter a shift number:   '))
# encrypt(message=message, shift= shift_number)



# import string 
# def decrypt(message, shift):
#     alphabet = string.ascii_letters + string.ascii_letters

#     decrypted_message = ''
#     for letter in message:
#         if letter not in alphabet:
#             decrypted_message += letter
#             continue
#         original_position = alphabet.index(letter)
#         new_position = original_position - shift
#         decrypted_message += alphabet[new_position]
#     print(decrypted_message)  

# message = input("Please enter the encrypted message:   ")
# shift_number = 5
# print("The shift number is [5] ")
# decrypt(message=message, shift= shift_number)
# the_red_queen_collection = {
#     'title':'Red Queen',
#     'author':'Aveyard',
#     'year':2015,
#     'pages': 383,
#     'is_many': True,
#     'rating': 4.1
# }
# print(the_red_queen_collection)
# print(the_red_queen_collection['title'])
# print(the_red_queen_collection.get('year'))
# print(the_red_queen_collection.keys())
# print(the_red_queen_collection.values())
# framework1 = {
#     'name': 'Abdullah',
#     'age': 20,
# }
# framework2 = {
#     'name': 'Muhammed',
#     'age': 17,
# }
# framework3 = {
#     'name': 'Tasneem',
#     'age': 8,
# }
# new_framework = {
#     'first': framework1,
#     'second': framework2,
#     'third': framework3,
# }
# print(framework1)
# print(framework2)
# print(framework3)
# print(new_framework)
# book = {
#     'title':'Red Queen',
#     'author':'Aveyard',
#     'year':2015,
#     'pages': 383,
#     'is_many': True,
#     'rating': 4.1
# }
# print(book)
# book.update({'status': 'done'})
# book.clear()
# b = book.copy()
# print(book)
# print(book.setdefault('complete year', 2026))
# print('=' * 40)
# allitems = book.items()
# book['status'] = 'good'
# # print(book.popitem())
# print('=' * 40)
# print(book)
# print(allitems)
# counting = ('my first key','my second key','my third key')
# item = 'x'
# print(dict.fromkeys(counting, item))
# class House:
#     room = ''
#     size = ''
# the_small_room = House()
# the_small_room.room = 'المحظرة الصغيرة'
# the_small_room.size = 'medium'

# the_large_room = House()
# the_large_room.room = 'المحظرة الكبيرة'
# the_large_room.size  = 'big'

# print(the_large_room.size)
# print(House())

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
# first_book = Book('the mother of dragons', 'Abdullah Shaaib')
# class Profile:
#     def __init__(self, user_name, email, learning_language):
#         self.user_name = user_name
#         self.email = email
#         self.learning_language = learning_language

# user1 = Profile('Abdulllah', 'abdohshoaib@gmail.com', 'Python')
# user2 = Profile('Muhammed', 'mo@gmail.com', 'C#')
# user3 = Profile('Ahmed', 'ahmed77@gmail.com', 'Html')

# print(
#     user1.user_name
    
# )
# #Homework2
# class Chit_Chat():
#     def __init__(self, sender, reciever, message, date):
#         self.sender = sender
#         self.reciever = reciever
#         self.message = message
#         self.date = date 

# class Product:
#     def __init__(self, name, price, description, rate):
#         self.name = name 
#         self.price = price 
#         self.description = description 
#         self.rate = rate 

# product1 = Product('laptop Lenovo Thinkpad L14', '$1200','laptop',7.2)

# class Movies:
#     def __init__(self, title, director, release_year, genre):
#         self.title = title 
#         self.director = director 
#         self.release_year = release_year
#         self.genre = genre 
#     def display(self):
#         print(f'the movie name is: {self.title}')    
#         print(f'the director: {self.director}')    
#         print(f'it was released on {self.release_year}')    
#         print(f'the genre: {self.genre}')    
#     def change_director(self, new_director):
#         self.director = new_director   
# first_movie = Movies('Inception','Christopher Nolan',2010 ,'Sci-Fi')     
# second_movie = Movies('The GodFather','Francis Ford Coppola',1927 ,'Crime')     
# third_movie = Movies('Parasite','Bong Joon-ho',2019 ,'Thriller') 
# print("Movies List")  
# print('=' * 50)  
# first_movie.display()
# second_movie.display()
# third_movie.display()
# print('=' * 50)
# first_movie.change_director('Shokry Sarhan')
# second_movie.change_director('Ajmed Mazhar')
# third_movie.change_director('Isamel Yassin')
# first_movie.display()
# second_movie.display()
# third_movie.display()

class User:
    def __init__(self, first_name, last_name, email, password, status = 'inactive'):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email 
        self.password = password 
        self.status = status
    def display(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(f"{'*' * len(self.password)}")

            
def create_user():
    first_name = input("What's your first name? ")
    last_name = input("What's your last name? ")
    email = input("Enter your email ")
    password = input("Choose a password ")
    return User(first_name, last_name, email, password, status='active')

user1 = create_user()
user1.display()













               









       

  



    

    

    








    















    


  

        

    




     



  

