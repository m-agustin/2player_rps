#Two player rock, paper, and scissors game
import sys

#Introduction, variables for the 2 players and rps
print('Welcome to the two player rock, paper, scissors game!')
rps = ['r', 'p', 's']
user1 = input('Insert name player 1')
print('Player 1 = ' + user1)
user2 = input('Insert name player 2')
print('Player 2 = ' + user2)
u1_score = 0
u2_score = 0

#function for rps for each player
def r_p_s(input1, input2):
    if (input1 == 'r' and input2 == 's') or (input1 == 's' and input2 == 'p') \
        or (input1 == 'p' and input2 == 'r'):
            return input1
    elif (input2 == 'r' and input2 == 's') or (input2 == 's' and input1 == 'p') \
        or (input2 == 'p' and input1 == 'r'):
            return input2

#function to check if a user wants to end game for each round
def check_quit(userinput):
    if userinput == 'quit':
        print('Thanks for playing. Bye!')
        sys.exit()

playgame = 'yes'

#while playgame does not equal to no, game continues
while playgame != 'no':
    print('If you want to quit playing the game, type "quit" to quit the game')

    user1_choice = input(f'Input your choice {user1}').lower()
    check_quit(user1_choice)
    
    while user1_choice not in rps:
        print(f'Invalid input {user1}')
        user1_choice = input(f'Try again {user1}').lower()

    user2_choice = input(f'Input your choice {user2}').lower()
    check_quit(user2_choice)
        
    while user2_choice not in rps:
        print(f'Invalid input {user2}')
        user2_choice = input(f'Try again {user2}').lower()
        continue

    if user1_choice == user2_choice:
        print('It is a tie!')
    else:
        result = r_p_s(user1_choice, user2_choice)
        if user1_choice == result:
            print(f'You win {user1}!')
            u1_score += 1
            print(f'{user1}, you have {u1_score} points')
        else:
            print(f'You win {user2}!')
            u2_score += 1
            print(f'{user2}, you have {u2_score} points')
        
    playgame = input('Would you like to play again? yes or no').lower()


print('Thanks for playing. Bye!')