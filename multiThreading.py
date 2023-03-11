import threading

def tarefa1():
    x = 0
    while x < 10:
        print("tarefa 1")
        x += 1

def tarefa2():
    x = 0
    while x < 10:
        print("tarefa 2")
        x += 1

threading.Thread(target=tarefa1).start()
threading.Thread(target=tarefa2).start()