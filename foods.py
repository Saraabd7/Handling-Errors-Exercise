
def open_file(name_file):
    try:
        with open(name_file, 'r') as file:
            line_list = file.readlines()
        for lines in line_list:
            print(lines.strip('\n').title)

    except FileNotFoundError as err:
        print('Check your files')
        print(err)


    finally:
        print('Error')



def open_and_write(foods):

    try:
        with open('foods.txt', 'a') as order_foods:
            # use forwad slash n to creat new lines when e write
            order_foods.write(f"{foods} \n")
    except FileNotFoundError as error:
        print('check your file')
        print(error)

    # finally:
    #     print('closing')



def open_and_read(corona):

    try:
        with open(corona , 'r') as order_foods:
            list_food = order_foods.readlines() # --> list
            return list_food


    except FileNotFoundError as error:
        print('Check your file')

