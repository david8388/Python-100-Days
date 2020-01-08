from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下載完成, 共花費%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python101', ))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('總共花費%.3f秒' % (end - start))


if __name__ == '__main__':
    main()