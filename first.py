import time
import function

now = (time.strftime("%b %d, %Y %H:%M:%S"))
print("It is", now)

while True:
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        file.close()

    user_action = input("Type Add, Show, Edit, Complete, or Exit: ")
    user_action = user_action.strip()
    user_action = user_action.capitalize()


    if user_action.startswith(('Add')):
        todo = user_action[4:]
        todos.append(todo + '\n')
        function.write_todos(todos)

    elif user_action.startswith(('Show')):
        for index, item in enumerate(todos):
            row = f"{index + 1} - {item.strip()}"
            print(row)
    elif user_action.startswith(('Edit')):
        try:
            number = int(user_action[5:])
            number -= 1
            if 0 <= number < len(todos):
                new_todo = input("Enter new todo: ") + "\n"
                todos[number] = new_todo
                function.write_todos(todos)
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith(('Complete')):
        try:
            number = int(user_action[9:])
            number -= 1
            if 0 <= number < len(todos):
                todos.pop(number)
                function.write_todos(todos)
            else:
                print("Invalid todo number.")
        except IndexError:
            print("There is no item with that number. ")
            continue
    elif user_action.startswith(('Exit')):
        break
    else:
        print("Command is not correct")

todoslen = len(todos)
print("Total number of tasks pending for today are: ", todoslen)
