import random


rock = '''
                                                           
88888888ba                        88         
88      "8b                       88         
88      ,8P                       88         
88aaaaaa8P' ,adPPYba,   ,adPPYba, 88   ,d8   
88""""88'  a8"     "8a a8"     "" 88 ,a8"    
88    `8b  8b       d8 8b         8888[      
88     `8b "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88      `8b `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                              '''

paper = '''   
88888888ba                                                
88      "8b                                               
88      ,8P                                               
88aaaaaa8P' ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88""""""'   ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88          ,adPPPPP88 88       d8 8PP""""""" 88          
88          88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88          `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
                       88                                 
                       88                           '''
scissors = '''                                                                                 
 ad88888ba             88                                                       
d8"     "8b            ""                                                       
Y8,                                                                             
`Y8aaaaa,    ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
  `"""""8b, a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
        `8b 8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
Y8a     a8P "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
 "Y88888P"   `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
  '''
#rules
#Rock-0 wins against scissors-2.
#Scissors2 win against paper-1.
#Paper-1 wins against rock-0.
import random

# Define the options
list_choose = [rock, paper, scissors]



try:
    # Get user's choice
    user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    # Ensure the user choice is valid
    if 0 <= user_choose <= 2:
        print(f"You chose: {list_choose[user_choose]}")
    else:
        print("You typed an invalid number. You lose!")
        exit()  # Exit the game if input is invalid

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {list_choose[computer_choice]}")

    # Determine the outcome
    if user_choose == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choose == 2:
        print("You lose!")
    elif computer_choice > user_choose:
        print("You lose!")
    elif user_choose > computer_choice:
        print("You win!")
    else:
        print("It's a draw!")
except ValueError:
    print("Invalid input! Please enter a number between 0 and 2.")
