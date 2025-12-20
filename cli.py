# Gerenciador de tarefas (CLI) Ok
# Adicionar, listar, remover e concluir tarefas OK
# Verificar e tratar dados inseridos incorretamente OK
# Salvar em arquivo .txt
# Extras:
    # Filtro por status (pendente/concluída)
    # Ordenar por data


task_list = []

def initApp():
    user_input = input('What do you want to do? add, list, remove, check or save: ').lower()
    if user_input == 'add':
        add()
    elif user_input == 'list':
        listTask()
    elif user_input == 'remove':
        removeTask()
    elif user_input == 'check':
        checkedTask()
    elif user_input == 'save':
        saveTask()
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
        print("Task doesn't exist. Try again!")
        removeTask()

    if remove_task_id_Num > len(task_list) or remove_task_id_Num <= 0:
        print("Task doesn't exist. Try again!")
        removeTask()
    
    
    task_list.pop(remove_task_id_Num - 1)
    print('Done')
    listTask()

def checkedTask():
    checked_task_Id = input('What is the task index? ')
    
    if checked_task_Id.isdigit():
        checked_task_Id = int(checked_task_Id)
        if checked_task_Id <=0 or checked_task_Id > len(task_list):
            print('Invalid index range. Try again!')
            checkedTask()
        else:
            #ternary expression
            task_list[checked_task_Id - 1][1] = True if task_list[checked_task_Id - 1][1] == False else False 
            print('Done!\n')
            listTask()
    elif checked_task_Id == '' or checked_task_Id.lower() == 'exit':
        initApp()
    else:
        print('Choose a valid index')
        checkedTask()

def saveTask():
    task_doc = 'Gerenciador de Tarefas.txt'
    with open(task_doc, 'w') as file:
        file.write('GERENCIADOR DE TAREFAS\n')

        for el in range(len(task_list)):
            
            msg_task = f'{el + 1}: {task_list[el][0]} [ ]\n' if task_list[el][1] == False else f'{el + 1}: {task_list[el][0]} [X]\n'
            
            file.writelines(msg_task)
    print("Saved as 'Gerenciador de Tarefas.txt'\n")
    initApp()
        

initApp()