import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key='Todo')
add_button=sg.Button("Add")

window=sg.Window("To do app",
                 layout=[[label], [input_box, add_button]],
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
        case sg.WINDOW_CLOSED:
            break



window.close()