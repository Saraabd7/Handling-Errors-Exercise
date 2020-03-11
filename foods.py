
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
        with open('foods.txt', 'w') as order_foods:
           order_foods.write(foods)
    except FileNotFoundError as error:
        print('check your file')
        print(error)

    # finally:
    #     print('closing')




