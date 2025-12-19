# Gerenciador de tarefas (CLI)
# Adicionar, listar, remover e concluir tarefas
# Verificar e tratar dados inseridos incorretamente
# Salvar em arquivo .json ou .txt
# Extras:
    # Filtro por status (pendente/concluída)
    # Ordenar por data


taskList = []

def initApp():
    userInput = input('What do you want to do? add, list, remove or check a task: ')
    if userInput == 'add':
        add()
    elif userInput == 'list':
        listTask()
    elif userInput == 'remove':
        removeTask()
    elif userInput == 'check':
        checkedTask()

def add():

    addInfo = input('Write the task: ("exit" for menu) ')

    if addInfo == '' or addInfo == 'exit':
        listTask()
    else:
        taskList.append([f'{addInfo}', False])
        print('task added\n')
        add()

def listTask():
    if len(taskList) == 0:
        print("To do list empty \nLet's start!")
    else:
        for task in range(len(taskList)):
        
            if taskList[task][1] == False:
                print(f'{task + 1}: {taskList[task][0]} [ ]')
            elif taskList[task][1] == True:
                print(f'{task + 1}: {taskList[task][0]} [X]')
            
    initApp()

def removeTask():
    removeTaskId = int(input('What is the task index? '))
    taskList.pop(removeTaskId - 1)
    print('Done')
    listTask()

def checkedTask():
    checkedTaskId = int(input('What is the task index? '))
    #ternary expression
    taskList[checkedTaskId - 1][1] = True if taskList[checkedTaskId - 1][1] == False else False 
    listTask()




initApp()