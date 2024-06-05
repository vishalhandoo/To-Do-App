import function
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter Todo", key="todos")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key = 'Display',
                      enable_events=True, size = [45, 10] )
edit_button = sg.Button("Edit")


window = sg.Window(title='My To-Do App',
                   layout=[[label],[input_box,add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todos']+"\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['Display'].update(values=todos)
        case "Edit":
            todo_to_edit = values['Display'][0]
            new_todo = values['todos']

            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            function.write_todos(todos)
            window['Display'].update(values=todos)
        case 'Display':
            window['todos'].update(value=values['Display'][0])
        case sg.WIN_CLOSED:
            break

window.close()

