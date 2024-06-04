def write_todos(todos_arg,filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
