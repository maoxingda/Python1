import threading
import time

count = 0
clock = threading.Lock()


def inc():
    time.sleep(1)

    global count

    with clock:
        count += 1

        print(count)


if __name__ == '__main__':
    thrds = list()

    for i in range(10):
        thrds.append(threading.Thread(target = inc))

    for thrd in thrds:
        thrd.start()

    for thrd in thrds:
        thrd.join()
