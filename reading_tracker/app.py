#terminar de emplementar todas as features do CLI OK
#refatorar o codigo OK
#criar uma função SELECT_BY_ID no.db OK
#implementar o argpparse OK
#finalizar projeto OK

import argparse
from database import get_connection, create_tables, add_book, get_all_books, delete_book, get_books_by_status, update_status, get_books_by_id

parser = argparse.ArgumentParser('Reading_traker', usage= 'app.py -name <NAME> [Optional]', description= 'Allows you to keep tracking your readings. If you want to, you can pass your name as argument for a persol experience')
parser.add_argument('-name', help= 'Your name')
args = parser.parse_args()

MENU_PROMPT = f"""" -- READING TRACKER --
Hello{f' {args.name}!' if args.name else '!'} Chose one option from menu:

1) Add reading
2) Updating reading status
3) List readings
4) Delete reading
5) Filter by status
6) close
 """

ERROR_INVALID_ENTRY = 'Invalid Entry. Try again!\n'

def init_app():
    create_tables(get_connection)

    while True:
        user_input = int(input(MENU_PROMPT))
        if user_input == 1:
            promp_add_book()
        elif user_input == 2:
            promp_update_status()
        elif user_input == 3:
            promp_list_books()
        elif user_input == 4:
            promp_delete_book()
        elif user_input == 5:
            promp_filter_status()
        elif user_input == 6:
            print('bye!')
            break
        else:
            print(ERROR_INVALID_ENTRY)
            continue

def promp_add_book():
    READING_USER = input('Add your current reading and information separetaded by commas (ex: title, author, year): ')
    READING_DATA = [item.strip() for item in READING_USER.split(',')]    

    if READING_USER == '' or READING_USER == 'exit':
        init_app()
    elif len(READING_DATA) != 3 or not READING_DATA[2].isdigit():
        print(ERROR_INVALID_ENTRY)
        promp_add_book()
    else:
        BOOK_STATUS = promp_get_status_handler()
        add_book(get_connection, READING_DATA[0], READING_DATA[1], int(READING_DATA[2]), BOOK_STATUS)    
        print(f'\n\"{READING_DATA[0]}\" was added!\n')

def promp_list_books():
    for el in get_all_books(get_connection):
        print(f' [ID]: {el[0]} [Titulo]: {el[1]} [Author]: {el[2]}, [year]: {el[3]} [STATUS]: {el[4]}')

def promp_delete_book():
    promp_list_books()
    READING_ID = promp_get_id_handler()
    BOOK_BD = delete_book(get_connection, READING_ID)
    print( f'\nDone! The book \"{BOOK_BD[1]}\" by {BOOK_BD[2]} was deleted')

def promp_filter_status():
    FILTER_STATUS = promp_get_status_handler()     
    FILTERED_LIST_BD = get_books_by_status(get_connection, FILTER_STATUS)

    print(f'\n -- {FILTER_STATUS.upper()} LIST --')
    for el in FILTERED_LIST_BD:
        print(f'* {el[1]} by {el[2]} : {el[3]}')
    print ('----------------------------\n')

def promp_get_status_handler():
    USER_STATUS = input(
    '''Chose a status number: 
    1: reading
    2: want to read
    3: already read
    => ''')

    status = None
    
    if USER_STATUS == '' or USER_STATUS == 'exit':
        init_app()
    elif not USER_STATUS.isdigit() or int(USER_STATUS) > 3 or int(USER_STATUS) < 1:
        print(ERROR_INVALID_ENTRY)
        promp_get_status_handler()
    elif USER_STATUS == '1':
        status = 'Reading'
    elif USER_STATUS == '2':
        status = 'Want to read'
    elif USER_STATUS == '3':
        status = 'Already read'
    

    return status

def promp_get_id_handler():
    ID_USER = input('Select a book by ID? ')
    
    if ID_USER == '' or ID_USER.strip().lower() == 'exit':
        init_app()
    elif not ID_USER.isdigit() or get_books_by_id(get_connection, ID_USER) == None:
        print(ERROR_INVALID_ENTRY)
        promp_get_id_handler()
    
    return ID_USER 

def promp_update_status():
    promp_list_books()

    UPDATE_ID = promp_get_id_handler()
    NEW_STATUS = promp_get_status_handler()

    UPDATED_READING_BD = update_status(get_connection, NEW_STATUS, UPDATE_ID)
    print(f' {UPDATED_READING_BD[1]} UPDATED!')

init_app()
  