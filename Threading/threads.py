import threading
import time

run = True

def thread_func(nr: int):
    while(run):
        print(f"Thread{nr}")
        time.sleep(0.5)

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_func, args=(1,))
    t2 = threading.Thread(target=thread_func, args=(2,))
    print("Started")

    t1.start()
    time.sleep(0.25)
    t2.start()
    input()
    time.sleep(10)
    run = False
    
    t1.join()
    t2.join()
    print("Ended")