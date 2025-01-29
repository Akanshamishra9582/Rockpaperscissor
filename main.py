import random 

def get_computer_choice():
    # ransomly return rock paper scissor
    choices = ["rock","paper","scissor"]
    return random.choice(choices)

def get_user_choice():
    user_input = input("Enter rock , paper, or scissor").lower()
    while user_input not in ("rock","paper","scissor","q"):
        user_input = input("invalid choice , enter rock paper or scissor :").lower()
    return user_input

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(user_choice == "rock" and computer_choice == "scissor") or \
          (user_choice == 'paper' and computer_choice == "rock") or \
          (user_choice == "scissor"and computer_choice == "paper"):
        return "you win"
    else:
        return "computer wins!"
    
def play_game():
    while True :
        user_choice = get_user_choice()
        if user_choice == 'q' :
            break
        computer_choice = get_computer_choice()
        print(f"\n You choose {user_choice},computer choose {computer_choice}")
        result  = determine_winner(user_choice , computer_choice)
        print(result)


play_game()