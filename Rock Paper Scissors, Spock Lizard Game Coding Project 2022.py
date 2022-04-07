import random

lose = 0
win = 0
tie = 0

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n 'l for lizard or 'spock for spock)").lower()
    computer = random.choice (['r', 'p', 's', 'l', 'spock']).lower()
    if user == computer:
        global tied 
        tied += 1
        return "It's a tie!"

    if is_win(user, computer):
        global win
        win +=  1
        return 'You won the game!'
    else:
        global lose
        lose += 1
        return 'You lost the game!'

def is_win (player, opponent):
    if (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') \
    or (player == 'r' and opponent == 'l') or (player == 'l' and opponent == 'spock') \
    or (player == 'spock' and opponent == 's') or (player == 's' and opponent == 'l') \
    or (player == 'p' and opponent =='spock') or (player == 'spock' and opponent == 'r') \
    or (player == 'r' and opponent == 's') or (player == 'l' and opponent == 'p'):

        return True
continuethegame = input("Do you want to keep playing rock,paper scissors, lizard, spock? Y or N:").lower()
while continuethegame =='yes':
    print(play())
    contiunethegame = input("Do you want to keep playing rock, paper,scissors, lizard, spock? Y or N:").lower()
    if contiunethegame == 'no':
        print("You have stopped playing rock, paper, scissors, lizard, spock.")
        print("You won" + str(win)+ "the game.")
        print("You lost" + str(lose)+ "the game.")
        print("You tied" + str(tie)+ "the game.")