import json

def main():
    mydict = {
        'name': 'David',
        'age': 25,
        'line': 54321,
        'friends': ['LBJ', 'KOBE'],
        'cars': [
            {'brand': 'BMW', 'max_speed': 150},
            {'branch': 'Benz', 'max_speed': 150}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('save completed')


if __name__ == '__main__':
    main()