from random import randint
from time import time, sleep


def download_task(filename):
    print('start downloading%s...' % filename)
    time_to_download = randint(6, 10)
    sleep(time_to_download)
    print('download completed, 花費%s秒' % time_to_download)


def main():
    start = time()
    download_task('python101')
    download_task('Peking Hot.avi')
    end = time()
    print('總共花費%.2f秒' % (end - start))


if __name__ == '__main__':
    main()