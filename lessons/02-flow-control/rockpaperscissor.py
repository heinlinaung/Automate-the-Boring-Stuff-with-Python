import random
print("Welcome to Rock, Paper, Scissors!")
choices = ["r", "p", "s"]
desc = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Enter (r)ock, (p)aper, or (s)cissors (or '(q)uit' to exit): ").lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {desc[choices.index(computer_choice)]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        print("You win!")
    else:
        print("You lose!")

