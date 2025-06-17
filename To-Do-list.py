Task = []
num = int(input("How many tasks do you want to add? "))

for i in range(num):
    ADD = input(f"Enter task {i + 1}: ")
    Task.append(ADD)

for index, Task in enumerate(Task, start=1):
    print(f"Task {index}: ",Task)
