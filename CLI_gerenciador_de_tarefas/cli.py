# Gerenciador de tarefas (CLI) Ok
# Adicionar, listar, remover e concluir tarefas OK
# Verificar e tratar dados inseridos incorretamente OK
# Salvar em arquivo .txt
# Extras:
    # Filtro por status (pendente/concluída)
    # Implementar um banco de dados SQLite

from db import add_task_db, get_all_task_db, remove_by_id_db, update_status_by_add, get_task_by_status_db
    


task_list = ['amorinha']

def initApp():
    user_input = input('What do you want to do? add, check, list, remove, status or save: (close to end program) ').lower()
    if user_input == 'add':
        add()
    elif user_input == 'list':
        list_task()
    elif user_input == 'remove':
        remove_task()
    elif user_input == 'check':
        checked_task()
    elif user_input == 'save':
        save_task()
    elif user_input == 'status':
        filter_status()
    elif user_input == 'close':
        return
    else:
        print('Choose one option')
        initApp()

def add():

    add_info = input('Write the task: ("exit" for menu) ')

    if add_info == '' or add_info == 'exit':
        list_task()
    else:
        add_task_db(add_info)
        print('task added\n')
        add()

def list_task(ret= False): #return : ret
    task_list_db = get_all_task_db()
    if len(task_list_db) == 0:
        print("To do list is empty \nLet's start!")
    else:
        for task in task_list_db:        
            if task.status == False:
                print(f'ID: {task.id}: {task.task} [ ]')
            elif task.status == True:
                print(f'ID: {task.id}: {task.task} [X]') 
    if ret:            
        return task_list_db 
    else:         
        initApp()

def remove_task():
    remove_task_id = input('What is the task ID? ')
    
    if remove_task_id.isdigit():
        remove_task_id_Num = int(remove_task_id)
    elif remove_task_id == '' or remove_task_id == 'exit':
        initApp()
    else:
        print("Task doesn't exist. Try again!")
        remove_task()

    removed_task = remove_by_id_db(remove_task_id_Num)
    if not removed_task:
        print("Task doesn't exist. Try again!")
        remove_task()

    print('Done')
    list_task()

def checked_task():
    checked_task_Id = input('What is the task index? ')
    
    if checked_task_Id.isdigit():
        checked_task_Id = int(checked_task_Id)
        task_update = update_status_by_add(checked_task_Id)
        if not task_update:
            print('Invalid index range. Try again!')
            checked_task()
        else:
            list_task()
    elif checked_task_Id == '' or checked_task_Id.lower() == 'exit':
        initApp()
    else:
        print('Choose a valid index')
        checked_task()


def filter_status ():
    status = input('which tasks do you want to see? Done or To do: ').lower()
    status_Bol = None
    if status == 'done':
        status_Bol = True
    elif status == 'to do':
        status_Bol = False
    else:
        print('type \'Done\' or \'To do\'')
        filter_status()

    status_list = get_task_by_status_db(status_Bol)
    
    for task in status_list:
        checkbox = '[X]' if status_Bol else '[ ]'
        print(f'ID: {task.id}: {task.task} {checkbox}')
            
    initApp()

def save_task():
    task_doc = 'Gerenciador de Tarefas.txt'
    with open(task_doc, 'w') as file:
        file.write('GERENCIADOR DE TAREFAS\n')

        task_list_all = list_task(True)

        for task in task_list_all:
            checkbox = '[X]' if task.status == True else '[ ]'
            
            msg_task = f' {task.id}: {task.task} {checkbox}\n'
            
            file.writelines(msg_task)
    print("Saved as 'Gerenciador de Tarefas.txt'\n")
    initApp()

           
        

initApp()