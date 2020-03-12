from foods import *

food_order = ' '
user_choice = ' '
food_list = []
order_counter = 1

while True:

    user_choice = input('Choose 1 to exit or Choose 2  to create a food order or Choose 3 to print an order:')
    if user_choice == '1':
        print('Exit')
        break
    elif user_choice == '2':
        food_order = input('What would you like to order? \n')
        open_and_write(food_order)
        # food_list.append(food_order)
        order_counter = order_counter + 1

    elif user_choice == '3':
        # open a file and read it
        file_to_open = input('what file do you want to open?')
        food_list = open_and_read(file_to_open)

        for item in food_list:
            print(item.strip('\n'))
        # either, the open and read function prints it
        # OR you iterate and print here

        # print(f'Enjoy your food: {food_list}') NOT what we want
        # because it is NOT reading from file

    else:
        print('Oops! That was no valid number, please Try again')


