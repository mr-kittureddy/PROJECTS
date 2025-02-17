import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    while abs(user_score or computer_score) < 5:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result, score = determine_winner(user_choice, computer_choice)
        print(result)
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1
        print(f"Score: User {user_score} - {computer_score} Computer")
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_game()
