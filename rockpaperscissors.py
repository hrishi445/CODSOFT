import random


while True:
    user_choice = input("enter your choice(rock/papers/scissors): ")
    
    random_actions = ["rock", "paper", "scissors"]
    
    computer_choice = random.choice(random_actions)
    
    print(f"your choice was {user_choice} and the computer's choice was {computer_choice}")

    
    if user_choice == computer_choice:
        print("It is a tie!")
    
    
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock beats Scissors you win!, computer lost")
        else:
            print("Paper beats rock you lost, computer wins!")
    
    
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper beats rock you win!, computer lost")
        else:
            print("Scissors beats Paper you lost, computer wins!")
    

    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors beats Paper you win!, computer lost")
        else:
            print("Rock beats Scissors you lost, computer wins!")

    restart = input("Restart(y/n):")
    
    if restart.lower() != "y":
        break