import threading, time

def thread_test():
    while True:
        print("FROM Function 1")
        time.sleep(1)

def thread_test2():
    while True:
        print("From Function 2")
        time.sleep(3)

def routes():
    run_event = threading.Event()
    run_event.set()
    t1 = threading.Thread(target=thread_test)
    t2 = threading.Thread(target=thread_test2)
    try:
        t1.start()
        t2.start()
    except KeyboardInterrupt:
        print("Interupting")
        t1.join()
        t2.join()
        run_event.clear()
    except Exception as e:
        print(e)