from threading import Thread
from program1 import prog1
from program2 import prog2
from program3 import prog3

def run_prog1():
    obj1 = prog1("Hello, World!")
    obj1.func()

def run_prog2():
    obj2 = prog2("Hello, UST!")
    obj2.func()

def run_prog3():
    obj3 = prog3("Hello!")
    obj3.func()

def main():
    # Create threads for each program
    thread1 = Thread(target=run_prog1)
    thread2 = Thread(target=run_prog2)
    thread3 = Thread(target=run_prog3)

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    print("All programs have finished running.")

if __name__ == "__main__":
    main()
