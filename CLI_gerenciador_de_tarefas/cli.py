# Gerenciador de tarefas (CLI) Ok
# Adicionar, listar, remover e concluir tarefas OK
# Verificar e tratar dados inseridos incorretamente OK
# Salvar em arquivo .txt
# Extras:
    # Filtro por status (pendente/concluída)
    


task_list = []

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
        task_list.append([f'{add_info}', False])
        print('task added\n')
        add()

def list_task():
    if len(task_list) == 0:
        print("To do list empty \nLet's start!")
    else:
        for task in range(len(task_list)):
        
            if task_list[task][1] == False:
                print(f'{task + 1}: {task_list[task][0]} [ ]')
            elif task_list[task][1] == True:
                print(f'{task + 1}: {task_list[task][0]} [X]')
            
    initApp()

def remove_task():
    remove_task_id = input('What is the task index? ')
    
    if remove_task_id.isdigit():
        remove_task_id_Num = int(remove_task_id)
    elif remove_task_id == '' or remove_task_id == 'exit':
        initApp()
    else:
        print("Task doesn't exist. Try again!")
        remove_task()

    if remove_task_id_Num > len(task_list) or remove_task_id_Num <= 0:
        print("Task doesn't exist. Try again!")
        remove_task()
    
    
    task_list.pop(remove_task_id_Num - 1)
    print('Done')
    list_task()

def checked_task():
    checked_task_Id = input('What is the task index? ')
    
    if checked_task_Id.isdigit():
        checked_task_Id = int(checked_task_Id)
        if checked_task_Id <=0 or checked_task_Id > len(task_list):
            print('Invalid index range. Try again!')
            checked_task()
        else:
            #ternary expression
            task_list[checked_task_Id - 1][1] = True if task_list[checked_task_Id - 1][1] == False else False 
            print('Done!\n')
            list_task()
    elif checked_task_Id == '' or checked_task_Id.lower() == 'exit':
        initApp()
    else:
        print('Choose a valid index')
        checked_task()

def save_task():
    task_doc = 'Gerenciador de Tarefas.txt'
    with open(task_doc, 'w') as file:
        file.write('GERENCIADOR DE TAREFAS\n')

        for el in range(len(task_list)):
            
            msg_task = f'{el + 1}: {task_list[el][0]} [ ]\n' if task_list[el][1] == False else f'{el + 1}: {task_list[el][0]} [X]\n'
            
            file.writelines(msg_task)
    print("Saved as 'Gerenciador de Tarefas.txt'\n")
    initApp()

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
    
    for i,el in enumerate(task_list):
        if el[1] == status_Bol:
            if el[1] == False:
                print(f'{i + 1}: {el[0]} [ ]')
            elif el[1] == True:
                print(f'{i + 1}: {el[0]} [X]')
            
    initApp()
           
        

initApp()