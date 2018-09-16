import threading
from time import ctime, sleep


def music(sname):
    for i in range(2):
        print(u'I was listening to %s. %s' % (sname, ctime()))
        sleep(1)


def movie(mname):
    for i in range(2):
        print(u'I was at the %s. %s\n' % (mname, ctime()))
        sleep(5)


if __name__ == '__main__':
    t1 = threading.Thread(target = music, args = (u'爱情买卖',))
    t2 = threading.Thread(target = movie, args = (u'阿凡达',))

    thrds = list()

    thrds.append(t1)
    thrds.append(t2)

    for thrd in thrds:
        thrd.setDaemon(True)
        thrd.start()
        thrd.join()

    print(u'all over %s.' % ctime())
