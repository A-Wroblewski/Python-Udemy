import json

def undo():
    if len(task_list) <= 0:
        print('\nThere is nothing to undo.')
        return

    return task_list_removed_items.append(task_list.pop())

def redo():
    if len(task_list_removed_items) <= 0:
        print('\nThere is nothing to redo.')
        return

    return task_list.append(task_list_removed_items.pop())

def add():
    if not user_input:
        print('\nYou must type something before adding it to your task list.')
        return

    return task_list.append(user_input)

def save_file():
    with open(file_saved_task_list, 'w', encoding='utf-8') as file:
        json.dump(task_list, file, indent=2)

file_saved_task_list = 'A122_lista_de_tarefas_com_desfazer_e_refazer.json'

def read_file(file):
    data = []
    
    with open(file_saved_task_list, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

task_list = read_file([])
task_list_removed_items = []

while True:
    print('Commands: [U]undo, [R]redo or [E]exit.')

    user_input = input('Type your task or command: ').strip()

    if user_input.lower() == 'u':
        undo()
        save_file()

    elif user_input.lower() == 'r':
        redo()
        save_file()

    elif user_input.lower() == 'e':
        break

    else:
        add()
        save_file()

    print('\nYOUR LIST:\n')
    print(*task_list, sep='\n')
    print()
