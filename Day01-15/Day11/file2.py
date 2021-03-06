import time

def main():

    with open("sunnyday.txt", 'r', encoding='utf-8') as f:
        print(f.read())

    with open("sunnyday.txt", mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open("sunnyday.txt") as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()