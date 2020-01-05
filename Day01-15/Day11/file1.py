def main():
    try:
        with  open("sunnyday.txt", 'r', encoding='utf-8') as f:
            print(f.read())
            f.close()
    except FileNotFoundError:
        print('無法打開指定文件')
    except LookupError:
        print('指定了未知編碼')
    except UnicodeDecodeError:
        print('讀取文件時解碼有誤')


if __name__ == '__main__':
    main()
