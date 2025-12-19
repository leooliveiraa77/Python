# Gerenciador de tarefas (CLI) Ok
# Adicionar, listar, remover e concluir tarefas OK
# Verificar e tratar dados inseridos incorretamente OK
# Salvar em arquivo .json ou .txt
# Extras:
    # Filtro por status (pendente/concluída)
    # Ordenar por data


task_list = []

def initApp():
    user_input = input('What do you want to do? add, list, remove or check a task: ')
    if user_input == 'add':
        add()
    elif user_input == 'list':
        listTask()
    elif user_input == 'remove':
        removeTask()
    elif user_input == 'check':
        checkedTask()
    else:
        print('Choose one option')
        initApp()

def add():

    add_info = input('Write the task: ("exit" for menu) ')

    if add_info == '' or add_info == 'exit':
        listTask()
    else:
        task_list.append([f'{add_info}', False])
        print('task added\n')
        add()

def listTask():
    if len(task_list) == 0:
        print("To do list empty \nLet's start!")
    else:
        for task in range(len(task_list)):
        
            if task_list[task][1] == False:
                print(f'{task + 1}: {task_list[task][0]} [ ]')
            elif task_list[task][1] == True:
                print(f'{task + 1}: {task_list[task][0]} [X]')
            
    initApp()

def removeTask():
    remove_task_id = input('What is the task index? ')
    
    if remove_task_id.isdigit():
        remove_task_id_Num = int(remove_task_id)
    elif remove_task_id == '' or remove_task_id == 'exit':
        initApp()
    else:
        print("task doesn't exist. Try again!")
        removeTask()

    if remove_task_id_Num > len(task_list) or remove_task_id_Num <= 0:
        print("task doesn't exist. Try again!")
        removeTask()
    
    
    task_list.pop(remove_task_id_Num - 1)
    print('Done')
    listTask()

def checkedTask():
    checked_task_Id = int(input('What is the task index? '))
    #ternary expression
    task_list[checked_task_Id - 1][1] = True if task_list[checked_task_Id - 1][1] == False else False 
    listTask()


initApp()