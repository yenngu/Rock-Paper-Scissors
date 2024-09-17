import random

#Keep track of wins and losses
wins = 0
loss = 0

# Choices for rock/paper/scissors
choices = ['Rock', 'Paper', 'Scissors']

def print_score():
    print(f'Current Score: You: {wins}. Opponent: {loss}')

while True:
    # Ask User Input
    userInput = input("Enter Rock/Paper/Scissors (or '.' to quit): ").capitalize()
    
    # Stop Game Key
    if userInput == '.':
        break
    # Make sure choice is valid
    if userInput not in choices:
        print("Pick either Rock, Paper, or Scissors")
        continue
    
    # Randomize opponent choices
    opponent_random = random.randint(0, 2)
    opponent_choice = choices[opponent_random]
    
    # Print Choices
    print(f'You picked {userInput}. Opponent picked {opponent_choice}')
    
    # Determine Results
    if userInput == 'Rock':
        if opponent_choice == 'Rock':
            print("Tie!")
        elif opponent_choice == 'Paper':
            print("Lose!")
            loss += 1
        elif opponent_choice == 'Scissors':
            print("Win!")
            wins += 1

    elif userInput == 'Scissors':
        if opponent_choice == 'Rock':
            print("Lose!")
            loss += 1
        elif opponent_choice == 'Paper':
            print("Win!")
            wins += 1
        elif opponent_choice == 'Scissors':
            print("Tie!")

    elif userInput == 'Paper':
        if opponent_choice == 'Rock':
            print("Win!")
            wins += 1
        elif opponent_choice == 'Paper':
            print("Tie!")
        elif opponent_choice == 'Scissors':
            print("Lose!")
            loss += 1

    # Print Current Score
    print_score()

    # End game and show results
    if wins + loss >= 5:
        print(f"Final Score: Wins: {wins}, Losses: {loss}")
        if wins > loss:
            print("User Wins!")
        elif loss > wins:
            print("Opponent Wins!")
        else:
            print("It's a Tie!")
        break
