user_prompt = "Enter a todo:"

# create loop outside of loop
todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)