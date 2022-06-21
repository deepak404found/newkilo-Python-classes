import random

users = []
play = 'yes'

while(play=='yes'):
    username = input("enter the username: ")
    num = random.randint(0, 10)
    
    attempt = 3
    while attempt >= 0:
    
        user_input = int(input('Enter Number: '))
        print(attempt)
        if user_input == num:
            print('You Won!')
            break
        elif attempt == 0:
            print(f'\nRemaining attempts: {attempt}.')
            print('You Lost!')
            break
        elif user_input > num:
            print(f'{user_input} is greater.\nRemaining attempts: {attempt}.')
            attempt -= 1

        elif user_input < num:
            print(f'{user_input} is smaller.\nRemaining attempts: {attempt}.')
            attempt -= 1
        else:
            print('Something went wrong!')
            break
            
    users.append({'username':username,'score':attempt+1})
    play = input('Do you want to play again? (yes/no): ')
    
# show scoreboard
print(users)
print('\nScoreboard:')
print('Username\tScore')
print('-'*10)
print('\n'.join(f'{user["username"]}\t\t{user["score"]}' for user in users))
print('\n')