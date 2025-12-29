from database import get_connection, create_tables, add_book, get_all_books, delete_book

MENU_PROMPT = """" -- READING TRACKER --
Chose one option from menu:

1) Add reading
2) Add reading status
3) List readings
4) Delete reading
5) Filter by status
6) close
 """

def init_app():
    create_tables(get_connection)

    while True:
        user_input = int(input(MENU_PROMPT))
        if user_input == 1:
            promp_add_book()
        elif user_input == 2:
            pass
        elif user_input == 3:
            promp_list_books()
        elif user_input == 4:
            promp_delete_book()
        elif user_input == 5:
            pass
        elif user_input == 6:
            print('bye!')
            break
        else:
            print('Invalid format, try again!')
            continue
    
    

def promp_add_book():
    user_reading = input('Add your current reading and information separetaded by commas (ex: title, author, year): ')
    reading = [item.strip() for item in user_reading.split(',')]
    print(reading)
    add_book(get_connection, reading[0], reading[1], int(reading[2]))
    print('Added!')

def promp_list_books():
    print(get_all_books(get_connection))

def promp_delete_book():
    promp_list_books()
    reading_id = input('Which book do you want to deleteby ID?')
    book = delete_book(get_connection, reading_id)
    print( f'\nDone the {book} is deleted')
    

init_app()
  