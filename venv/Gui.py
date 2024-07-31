import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key='Todo')
add_button=sg.Button("Add")
list_box=sg.Listbox(values = functions.get_todos(), key="Todos",
                    enable_events=True,size=[45, 10])
edit_button = sg.Button("Edit")

window=sg.Window("To do app",
                 layout=[[label], [input_box, add_button], [list_box, edit_button]],
                 font=('Helvetica',10))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos=functions.get_todos()
            new_todo=values['Todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
        case 'Edit':
            todos = functions.get_todos()
            todo_to_edit=values['Todos']
            new_todo=values['Todo']
            index = index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
        case 'Todos':
            window['Todo'].update(value = values['Todos'][0])

        case sg.WINDOW_CLOSED:
            break



window.close()