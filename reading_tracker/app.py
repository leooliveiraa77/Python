#terminar de emplementar todas as features do CLI OK
#refatorar o codigo
#criar uma função SELECT_BY_ID no.db
#implementar o argpparse
#finalizar projeto

from database import get_connection, create_tables, add_book, get_all_books, delete_book, get_books_by_status, update_status

MENU_PROMPT = """" -- READING TRACKER --
Chose one option from menu:

1) Add reading
2) Updating reading status
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
            print('Invalid format, try again!')
            continue

def promp_add_book():
    user_reading = input('Add your current reading and information separetaded by commas (ex: title, author, year): ')
    reading = [item.strip() for item in user_reading.split(',')]    
    book_status = promp_get_status_handler()
    add_book(get_connection, reading[0], reading[1], int(reading[2]), book_status)    
    print(f'{reading[0]} was added!\n')

def promp_list_books():
    for el in get_all_books(get_connection):
        print(f' [ID]: {el[0]} [Titulo]: {el[1]} by {el[2]}, [year]: {el[3]} [STATUS]: {el[4]}')

def promp_delete_book():
    promp_list_books()
    reading_id = promp_get_id_handler()
    book = delete_book(get_connection, reading_id)
    print( f'\nDone the {book} is deleted')

def promp_filter_status():
    FILTER_STATUS = promp_get_status_handler()     
    filtered_list = get_books_by_status(get_connection, FILTER_STATUS)

    print(f' -- {FILTER_STATUS.upper()} LIST --')
    for el in filtered_list:
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
    
    if not USER_STATUS.isdigit() or int(USER_STATUS) > 3 or int(USER_STATUS) < 1:
        print('Invalid entry\n')
        init_app()
    elif USER_STATUS == '1':
        status = 'reading'
    elif USER_STATUS == '2':
        status = 'want to read'
    elif USER_STATUS == '3':
        status = 'already read'

    return status

def promp_get_id_handler():
    #Criar validação de dados
    id = input('Select a book by ID? ')
    return id 
def promp_update_status():
    promp_list_books()

    update_id = promp_get_id_handler()
    NEW_STATUS = promp_get_status_handler()

    updated_reading = update_status(get_connection, NEW_STATUS, update_id)
    print(f' {updated_reading} UPDATED!')

init_app()
  