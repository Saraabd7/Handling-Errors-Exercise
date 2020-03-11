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
        food_list.append(food_order)
        order_counter = order_counter + 1

    elif user_choice == '3':
        print(f'Enjoy your food: {food_list}')

        break

    else:
        print('Oops! That was no valid number, please Try again')


