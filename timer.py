import threading


def func_timer():
    print('hello timer', threading.current_thread().name)
    global timer
    timer = threading.Timer(3, func_timer)
    timer.start()


if __name__ == '__main__':
    timer = threading.Timer(3, func_timer)
    threading.Thread().daemon
    timer.start()
