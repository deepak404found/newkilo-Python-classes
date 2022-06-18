import random

num = random.randint(0, 10)

attempt = 4
while attempt > 0:
   
    user_input = int(input('Enter Number: '))
    if user_input == num:
        print('You Won!')
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