import random

user = input("Choose 'r' for rock, 'p' for paper and 's' for scissors: ")
computer = random.choice(['r', 'p', 's'])

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

if user == computer:
    print(f"The computer chose {computer}. It\'s a tie")

elif is_win(user, computer):
    print(f"The computer chose {computer}. You won!")

else:
    print(f"The computer chose {computer}. You lost!")