todos = []

while True:
    # eliminates any trailing spaces
    user_action = input("Type add, show or exit:").strip()
    # match case statement is a block
    match user_action:
        case "add":
            todo = input("Add a todo:")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                # each first letter in each string is capitalized
                item = item.title()
                print(item)
        case "exit":
            break
            print(todos)
        case _:
            print("Unknown command entered")

print("Bye!")