import function
import FreeSimpleGUI as sg
import time

sg.theme('DarkTeal6')
label_date_time = sg.Text('',key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter Todo", key="todos")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key = 'Display',
                      enable_events=True, size = [45, 10] )
edit_button = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button("Exit")

window = sg.Window(title='My To-Do App',
                   layout=[[label_date_time],
                           [label],
                           [input_box,add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todos']+"\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['Display'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['Display'][0]
                new_todo = values['todos']

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                function.write_todos(todos)
                window['Display'].update(values=todos)
            except IndexError:
                sg.popup("Please Select the Input First From the List",font=("Helvetica", 10))
        case "Complete":
            try:
                todo_to_complete = values['Display'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['Display'].update(values=todos)
                window['todos'].update(value='')
            except IndexError:
                sg.popup("Please Select the Input First From the List", font=("Helventica", 10))
        case "Exit":
            break
        case 'Display':
            window['todos'].update(value=values['Display'][0])
        case sg.WIN_CLOSED:
            break

window.close()

