# Gerenciador de tarefas (CLI)
# Adicionar, listar, remover e concluir tarefas
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

def add():
    addInfo = input('Write the task: ')
    taskList.append(f'{len(taskList) + 1} {addInfo}')
    print('task added')
    initApp()

def listTask():
    for task in range(len(taskList)):
        print(taskList[task])
        initApp()



initApp()