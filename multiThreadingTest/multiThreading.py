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

# threading.Thread(target=tarefa1).start()
# threading.Thread(target=tarefa2).start()

def volume_cube(a):
    print ("Volume of Cube:", a*a*a)

def volume_square(a):
    print ("Volume of Square:", a*a)

t1 = threading.Thread(target=volume_cube(1), args=(2))
t2 = threading.Thread(target=volume_square(2), args=(3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")