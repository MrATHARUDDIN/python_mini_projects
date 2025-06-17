Task = []
TotalTask=0
condition=True
def add():
    global TotalTask
    num = int(input("How many tasks do you want to add? "))
    for i in range(num):
        ADD = input(f"Enter task {i + 1}: ")
        Task.append(ADD)
        TotalTask += 1


def show_task():
    if(TotalTask > 0):
        for index, Task in enumerate(Task, start=1):
            print(f"Task {index}: ",Task)
    else:
        print("No Task Founded")

def remove():
     show_task()


while(condition):
    chose = int(input("Enter your choice (1=Add, 2=Show, 3=Remove): "))

    match chose:
        case 1:
            add()
        case 2:
            show_task()
        case 3:
            remove()
        case _:
            print("Lol Bro")
